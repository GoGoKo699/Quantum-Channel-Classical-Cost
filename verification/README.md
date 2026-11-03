# Verification and reproduction

The universal claims are analytical. The [exact proof](../science/exact_classification.md) covers every qubit channel and every finite random menu of physical effects. The [lower](../science/amplitude_lower.md) and [upper](../science/amplitude_upper.md) proofs establish the amplitude-damping exponent. Finite numerical checks support the matrix conventions and the concrete error calculation; they do not substitute for those proofs.

## Run the matrix checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_science.py
```

The script uses NumPy, fixes seed `20261103`, reports its actual Python and NumPy versions, and exits unsuccessfully if an assertion fails. Run without Python's `-O` flag, which disables assertions. The reference execution used Python 3.12.14 and NumPy 2.3.5.

| Check | Independent comparison and purpose |
|---|---|
| Channel representation | Direct Kraus action versus affine Bloch action, including reset and identity endpoints |
| Output determinant | Matrix determinant versus the pure-input population formula |
| Bell effect | Direct two-qubit Bell probability versus the transposed single-qubit response; complex states detect omission of the transpose |
| Support geometry | Direct support function versus its rationalized deficit, plus a finite-angle check of the quartic coefficient |
| Reference preservation | Explicit measurement of an output tensor an entangled side-reference state, compared before and after regularization |
| Preparation averaging | Mixtures of physical pure states compared with their average density matrix after the same joint measurement |

The reference cases use both pure and mixed entangled side-reference states, a binary Bell POVM, and general complex POVMs with three and five outcomes. Tensor ordering is explicitly `A, B, R`. The script checks conditional reference blocks, their total marginal, total variation error, and the full classical-record/reference trace distance.

The committed [reference output](reference_output.json) records the completed run. Floating-point residuals can vary across platforms; the assertions use an absolute tolerance of `2e-12` for the exact matrix identities. The quartic check is at a nonzero angle with its own stated relative tolerance, so it includes a finite-angle correction.

The spectral mixtures used in this finite check depend on the input. They test linearity and error propagation, **not** the existence of a globally fixed message alphabet. The latter is proved by the adaptive-net and containment construction. The script does not enumerate all channels, certify infinite-dimensional randomness, establish optimal prefactors, or replace the asymptotic proof by a fitted slope.

## Reproduce the figure

```bash
python3 -m pip install -r verification/figure_requirements.txt
python3 verification/plot_geometry.py
```

This writes `figures/amplitude_geometry.svg`. The left panel plots exact output-ellipsoid meridians for survival probabilities 0.2, 0.5 and 0.8. The right panel evaluates the exact support deficit against the polar normal angle; its dashed fourth-power line is a visual slope reference. No protocol simulation, statistical estimation or fitted cost curve is involved. The generator uses the rationalized formula to avoid cancellation near the pure output.

## Proof audit route

For the exact converse, check the order of the two limits in the finite-random-effect lemma, then the pure-output Kraus form and its nonzero tangent. The lemma needs finiteness of the menu at each shared seed, not a uniform positive lower bound on its nonzero entries.

For the quantitative converse, check the cap Jacobian, the small-eigenvalue leakage, and the trace weights of decoder effects. Normalizing an effect for the area estimate does not impose a state-preparation decoder. Tonelli's theorem is applied to nonnegative jointly measurable quantities.

For the construction, check the global support inequality, cap and annular packing counts, and support domination in every normal direction. This proves containment for the whole channel image. The fixed vertex set determines the alphabet; the four-vertex Carathéodory decomposition for one input does not determine the global alphabet size.

Finally, check the operational boundary: error is uniform over known input descriptions and unknown side states, the upper bound is stable under a side reference, and only exact finite feasibility is transferred to finite interactive communication. No optimal quantitative interactive law is asserted.
