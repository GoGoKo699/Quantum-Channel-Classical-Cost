# Scientific overview

A channel can add noise while retaining one exactly pure output. That small part of its output set can determine whether a classical message can replace the channel in a joint measurement. This project asks how the entire output geometry controls the required communication.

Alice knows the input qubit's classical description. Bob holds an unknown physical quantum system and must combine it with the channel output in a requested measurement. Alice sends a message from a fixed finite alphabet. Shared randomness is unlimited but carries no input information. The [operational model](model.md) states the physical task, the uniform resource bound, and the two error criteria.

## From a physical task to an operator constraint

The unknown side input makes positivity useful. Consider just one possible request: a binary Bell-projector measurement on the channel output and Bob's side qubit. Every message and shared seed selects a physical response effect on that qubit. Agreement with the target for every unknown side state fixes the average effect to one half of the transposed channel output.

This is a necessary consequence of the full task, so it can prove lower bounds for arbitrary physical decoders. It does not assume that Bob prepares an output state. By contrast, a construction is free to prepare a state and perform the requested joint measurement. Trace-distance contractivity then controls both the outcome and its correlations with an untouched reference.

## Exact communication: two sufficient mechanisms and one obstruction

The [exact classification](exact_classification.md) proves that finite exact simulation exists precisely when a qubit channel has no pure output or is entanglement breaking.

If the output image stays strictly inside the Bloch ball, a finite polytope of physical pure-state vertices contains it. Alice expresses the desired output as a convex mixture and sends a sampled vertex label. If the channel is entanglement breaking, its finite measure-and-prepare representation supplies a different finite alphabet. The first mechanism can apply even when the channel preserves some entanglement on an unknown input, because Alice here receives a classical description and may use a nonlinear encoder.

For the remaining channels, choose coordinates at a pure output. Complete positivity gives a normal form whose surviving coherence is linear in a small input amplitude, while a transverse output population is quadratic. A finite random menu of positive effects cannot reproduce this tangent: as the transverse population vanishes, its squared coherence must vanish faster. This obstruction survives arbitrary input-independent shared randomness. A finite contingent-strategy reduction also transfers exact feasibility to uniformly finite public interaction trees.

## Finite error: why amplitude damping costs half a logarithm

The [geometry and examples](geometry_and_examples.md) state the quantitative theorem. For every fixed nontrivial survival probability, the optimal one-way alphabet grows as the inverse square root of the allowed error. Taking its binary logarithm gives half-logarithmic bit cost.

The [lower bound](amplitude_lower.md) examines a cap of nearly pure output directions. Positivity forces a definite response weight to be concentrated near each requested direction. Each available effect can serve only a small area accurately. Integrating the weights over the cap and shared randomness gives a lower bound on the global alphabet.

The [upper construction](amplitude_upper.md) slightly depolarizes the desired output and encloses the regularized image in a pure-state polytope. The output ellipsoid has quartic contact with the Bloch sphere near its pure output. The construction therefore uses a fine mesh near that point and progressively coarser meshes farther away. A support-function comparison proves containment for every output, and a measurable convex decomposition supplies the encoder.

These arguments match the error exponent without identifying all physical simulators with preparation protocols. The lower bound uses the weaker measurement-statistics error; the upper bound satisfies the stronger reference-stable criterion.

## Result ownership and reading route

| Question | Canonical source |
|---|---|
| What is supplied, what is charged, and what must be reproduced? | [Operational model](model.md) |
| Which qubit channels have finite exact cost? | [Exact classification](exact_classification.md) |
| What is the sharp approximate theorem and what does it mean? | [Geometry and examples](geometry_and_examples.md) |
| Why does arbitrary shared randomness fail to lower the exponent? | [Cap-area converse](amplitude_lower.md) |
| How does a single finite global alphabet achieve that exponent? | [Adaptive-net construction](amplitude_upper.md) |
| Which ingredients are inherited from prior research? | [Related work](../references/RELATED_WORK.md) |
| How can the matrix identities and error propagation be reproduced? | [Verification](../verification/README.md) |

The [Watrous bridge](../learning/ANCHOR.md) supplies a focused introduction and convention dictionary. The [30-milestone map](../learning/MILESTONES.md) assembles the background before following the proof mechanisms to their combined conclusion.

The quantitative theorem concerns one-way, uniform worst-case communication at a fixed damping parameter. Complete reset and identity have different limiting behavior. Optimal interactive cost, finite expected communication, and a uniform joint damping–accuracy crossover are separate questions. The numerical checks validate concrete identities and examples; the universal claims are established by the proofs above.
