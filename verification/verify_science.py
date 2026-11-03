#!/usr/bin/env python3
"""Finite matrix cross-checks for generic amplitude-damping simulation.

Numerical dependency: NumPy only. The seed is fixed and the installed NumPy
version is reported. These checks target normalization, transpose conventions,
tensor ordering, and the reference-stable error calculation. They do not prove
the asymptotic alphabet bounds or certify a finite global polytope construction.

The two-state spectral mixtures below check linearity of state preparation;
their input-dependent eigenstates are not a claimed global message codebook.
"""

import json
import platform

import numpy as np


SEED = 20261103
ATOL = 2e-12
RNG = np.random.default_rng(SEED)
I2 = np.eye(2, dtype=complex)
PAULIS = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)


def hermitian(matrix):
    return (matrix + matrix.conj().T) / 2


def pure(vector):
    vector = np.asarray(vector, dtype=complex)
    vector = vector / np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def random_density(dim):
    matrix = RNG.normal(size=(dim, dim)) + 1j * RNG.normal(size=(dim, dim))
    state = matrix @ matrix.conj().T
    return state / np.trace(state)


def random_unitary(dim):
    matrix = RNG.normal(size=(dim, dim)) + 1j * RNG.normal(size=(dim, dim))
    unitary, _ = np.linalg.qr(matrix)
    return unitary


def check_state(state):
    assert np.max(np.abs(state - state.conj().T)) <= ATOL
    assert abs(np.trace(state) - 1) <= ATOL
    assert np.linalg.eigvalsh(state).min() >= -ATOL


def amplitude_kraus(state, eta):
    k0 = np.diag([1.0, np.sqrt(eta)]).astype(complex)
    k1 = np.array([[0.0, np.sqrt(1 - eta)], [0.0, 0.0]], dtype=complex)
    assert np.max(np.abs(k0.conj().T @ k0 + k1.conj().T @ k1 - I2)) <= ATOL
    return k0 @ state @ k0.conj().T + k1 @ state @ k1.conj().T


def amplitude_affine(state, eta):
    bloch = np.array([np.trace(state @ pauli).real for pauli in PAULIS])
    output = np.array([
        np.sqrt(eta) * bloch[0],
        np.sqrt(eta) * bloch[1],
        1 - eta + eta * bloch[2],
    ])
    return (I2 + sum(component * pauli for component, pauli in zip(output, PAULIS))) / 2


def trace_distance(first, second):
    difference = first - second
    assert np.max(np.abs(difference - difference.conj().T)) <= ATOL
    return float(np.abs(np.linalg.eigvalsh(hermitian(difference))).sum() / 2)


def psd_sqrt(matrix):
    values, vectors = np.linalg.eigh(hermitian(matrix))
    assert values.min() >= -ATOL
    return (vectors * np.sqrt(np.clip(values, 0, None))) @ vectors.conj().T


def random_povm(dim, outcomes):
    raw = []
    for _ in range(outcomes):
        matrix = RNG.normal(size=(dim, dim)) + 1j * RNG.normal(size=(dim, dim))
        raw.append(matrix @ matrix.conj().T)
    values, vectors = np.linalg.eigh(sum(raw))
    assert values.min() > 0
    inverse_sqrt = (vectors * (1 / np.sqrt(values))) @ vectors.conj().T
    effects = [hermitian(inverse_sqrt @ effect @ inverse_sqrt) for effect in raw]
    assert np.max(np.abs(sum(effects) - np.eye(dim))) <= ATOL
    for effect in effects:
        eigenvalues = np.linalg.eigvalsh(effect)
        assert eigenvalues.min() >= -ATOL and eigenvalues.max() <= 1 + ATOL
    return effects


def partial_trace_ab(joint):
    # Ordering is A (2), B (2), R (2); group A B as one four-dimensional factor.
    return np.trace(joint.reshape(4, 2, 4, 2), axis1=0, axis2=2)


def partial_trace_b(side):
    # Side ordering is B (2), R (2).
    return np.trace(side.reshape(2, 2, 2, 2), axis1=0, axis2=2)


def instrument_blocks(state_a, side_br, effects):
    joint = np.kron(state_a, side_br)
    blocks = []
    for effect in effects:
        lifted = np.kron(psd_sqrt(effect), I2)
        block = hermitian(partial_trace_ab(lifted @ joint @ lifted.conj().T))
        assert np.linalg.eigvalsh(block).min() >= -ATOL
        blocks.append(block)
    assert abs(sum(np.trace(block) for block in blocks) - 1) <= ATOL
    return blocks


def cq_distance(first, second):
    # The outcome record is classical, so the joint record-reference state is block diagonal.
    return sum(trace_distance(left, right) for left, right in zip(first, second))


def negativity(side):
    partial_transpose = side.reshape(2, 2, 2, 2).transpose(2, 1, 0, 3).reshape(4, 4)
    eigenvalues = np.linalg.eigvalsh(hermitian(partial_transpose))
    return float(-eigenvalues[eigenvalues < 0].sum())


def support(eta, theta):
    return ((1 - eta) * np.cos(theta)
            + np.sqrt(eta * np.sin(theta) ** 2 + eta ** 2 * np.cos(theta) ** 2))


def rationalized_gap(eta, theta):
    denominator = (1 - (1 - eta) * np.cos(theta)
                   + np.sqrt(eta * np.sin(theta) ** 2 + eta ** 2 * np.cos(theta) ** 2))
    # The half-angle formula avoids cancellation in the quartic diagnostic.
    one_minus_cos = 2 * np.sin(theta / 2) ** 2
    return (1 - eta) * one_minus_cos ** 2 / denominator


def run():
    etas = (0.0, 0.13, 0.57, 0.91, 1.0)
    complex_pure = pure([1, 0.3 + 0.7j])
    inputs = [pure([1, 0]), pure([0, 1]), complex_pure, pure([1, 1j]),
              np.diag([0.31, 0.69]).astype(complex), random_density(2)]
    side_qubit = pure([1, -0.4 + 0.2j])
    phi = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    bell = np.outer(phi, phi.conj())
    affine_residual = bell_residual = wrong_transpose_gap = 0.0
    representation_cases = 0

    for eta in etas:
        for state in inputs:
            check_state(state)
            output = amplitude_kraus(state, eta)
            check_state(output)
            affine_residual = max(affine_residual,
                                  float(np.max(np.abs(output - amplitude_affine(state, eta)))))
            direct = float(np.vdot(phi, np.kron(output, side_qubit) @ phi).real)
            effect = float(np.trace((output.T / 2) @ side_qubit).real)
            wrong = float(np.trace((output / 2) @ side_qubit).real)
            bell_residual = max(bell_residual, abs(direct - effect))
            wrong_transpose_gap = max(wrong_transpose_gap, abs(direct - wrong))
            representation_cases += 1
    assert affine_residual <= ATOL and bell_residual <= ATOL
    assert wrong_transpose_gap > 1e-3, "Complex test states must detect omitting the transpose."

    determinant_residual = 0.0
    determinant_cases = 0
    for eta in etas:
        for z in (0j, 0.07 + 0.11j, -0.3 + 0.4j, 1.2 - 0.6j):
            output = amplitude_kraus(pure([1, z]), eta)
            excited_population = abs(z) ** 2 / (1 + abs(z) ** 2)
            expected = eta * (1 - eta) * excited_population ** 2
            determinant_residual = max(determinant_residual, abs(np.linalg.det(output) - expected))
            determinant_cases += 1
    assert determinant_residual <= ATOL

    support_residual = quartic_relative_error = 0.0
    support_cases = 0
    theta_small = 0.005
    for eta in (0.13, 0.57, 0.91):
        for theta in (0.0, 0.03, 0.15, 0.7, 1.0, 2.0, np.pi):
            support_residual = max(support_residual,
                                   abs(1 - support(eta, theta) - rationalized_gap(eta, theta)))
            support_cases += 1
        coefficient = (1 - eta) / (8 * eta)
        observed = rationalized_gap(eta, theta_small) / theta_small ** 4
        quartic_relative_error = max(quartic_relative_error, abs(observed / coefficient - 1))
    assert support_residual <= ATOL
    assert quartic_relative_error < 1e-3

    # Both side-reference states are entangled; local basis changes avoid a real-only test.
    schmidt = np.array([np.sqrt(0.7), 0, 0, np.exp(0.37j) * np.sqrt(0.3)])
    local_unitary = np.kron(random_unitary(2), random_unitary(2))
    entangled = local_unitary @ pure(schmidt) @ local_unitary.conj().T
    side_states = [entangled, 0.8 * entangled + 0.2 * np.eye(4) / 4]
    side_negativities = [negativity(side) for side in side_states]
    assert min(side_negativities) > 0.1
    povms = [[bell, np.eye(4) - bell], random_povm(4, 3), random_povm(4, 5)]
    epsilon = 0.037
    delta = 2 * epsilon
    reference_cases = 0
    max_local = max_cq = max_tv = max_ratio = 0.0
    max_product_residual = max_mixture_residual = max_marginal_residual = 0.0

    for eta in (0.27, 0.73):
        for state in (complex_pure, 0.65 * complex_pure + 0.35 * I2 / 2):
            target = amplitude_kraus(state, eta)
            regularized = (1 - delta) * target + delta * I2 / 2
            local_distance = trace_distance(target, regularized)
            assert 0 < local_distance <= epsilon + ATOL
            weights, vectors = np.linalg.eigh(regularized)
            prepared_states = [np.outer(vectors[:, k], vectors[:, k].conj()) for k in range(2)]
            assert np.max(np.abs(sum(weights[k] * prepared_states[k] for k in range(2))
                                 - regularized)) <= ATOL
            for side in side_states:
                check_state(side)
                reference = partial_trace_b(side)
                product_distance = trace_distance(np.kron(target, side), np.kron(regularized, side))
                max_product_residual = max(max_product_residual, abs(product_distance - local_distance))
                for effects in povms:
                    ideal_blocks = instrument_blocks(target, side, effects)
                    simulated_blocks = instrument_blocks(regularized, side, effects)
                    conditional = [instrument_blocks(prepared, side, effects) for prepared in prepared_states]
                    mixture_blocks = [sum(weights[k] * conditional[k][outcome] for k in range(2))
                                      for outcome in range(len(effects))]
                    max_mixture_residual = max(max_mixture_residual,
                                              max(float(np.max(np.abs(left - right)))
                                                  for left, right in zip(mixture_blocks, simulated_blocks)))
                    max_marginal_residual = max(max_marginal_residual,
                                               float(np.max(np.abs(sum(ideal_blocks) - reference))),
                                               float(np.max(np.abs(sum(simulated_blocks) - reference))))
                    cq_error = cq_distance(ideal_blocks, simulated_blocks)
                    tv_error = sum(abs(np.trace(left - right).real)
                                   for left, right in zip(ideal_blocks, simulated_blocks)) / 2
                    assert tv_error <= cq_error + ATOL
                    assert cq_error <= local_distance + ATOL
                    max_local = max(max_local, local_distance)
                    max_cq = max(max_cq, cq_error)
                    max_tv = max(max_tv, float(tv_error))
                    max_ratio = max(max_ratio, cq_error / local_distance)
                    reference_cases += 1

    assert max_product_residual <= ATOL
    assert max_mixture_residual <= ATOL
    assert max_marginal_residual <= ATOL
    assert max_cq > 1e-4, "The reference check must compare distinguishable output states."

    return {
        "status": "passed",
        "seed": SEED,
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "absolute_tolerance": ATOL,
        "kraus_affine_and_bell": {
            "cases": representation_cases,
            "max_affine_residual": affine_residual,
            "max_bell_transpose_residual": bell_residual,
            "max_error_if_transpose_omitted": wrong_transpose_gap,
        },
        "determinant": {"cases": determinant_cases, "max_residual": float(determinant_residual)},
        "support": {
            "cases": support_cases,
            "max_rationalization_residual": float(support_residual),
            "quartic_check_theta": theta_small,
            "max_quartic_coefficient_relative_error": float(quartic_relative_error),
        },
        "reference_contraction": {
            "cases": reference_cases,
            "epsilon": epsilon,
            "side_state_negativities": side_negativities,
            "max_local_trace_distance": max_local,
            "max_record_reference_trace_distance": max_cq,
            "max_classical_total_variation": max_tv,
            "max_record_reference_to_local_ratio": max_ratio,
            "max_product_distance_residual": max_product_residual,
            "max_prepared_mixture_residual": max_mixture_residual,
            "max_reference_marginal_residual": max_marginal_residual,
        },
        "scope": "Finite checks of independent matrix representations, preparation averaging, and reference-stable contraction; not an asymptotic proof or a global codebook test.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
