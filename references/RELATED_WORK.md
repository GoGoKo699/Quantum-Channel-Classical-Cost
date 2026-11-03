# Related work and attribution

The communication resource depends on what the sender knows, what the receiver physically receives, and which shared resources are free. The results here concern a known classical description of one qubit input, an unknown quantum side input at the receiver, free input-independent shared randomness, and a uniformly finite one-way message alphabet. The [model](../science/model.md) gives the full quantifiers.

## naik2026

**Sahil Gopalkrishna Naik, Mani Zartab, Nicolas Gisin, and Manik Banik.** *No-Go Theorem for Generic Simulation of Qubit Channels with Finite Classical Resources*. Proceedings of the Royal Society A **482**, 20250831 (2026). [DOI](https://doi.org/10.1098/rspa.2025.0831); [arXiv:2501.15807v2](https://arxiv.org/abs/2501.15807v2); [full arXiv text](https://arxiv.org/html/2501.15807v2).

This is the closest operational antecedent. It introduces generic simulation with an unknown quantum side system, proves exact finite-message impossibility for the identity channel, reduces finite public interaction to finite one-way strategies, and constructs finite simulations of depolarizing channels with nonzero noise. The side-input task, identity obstruction and finite-interaction reduction are inherited here.

The present [classification](../science/exact_classification.md) determines exact finite feasibility for every qubit-to-qubit channel. Its finite-random-effect lemma handles a coherent tangent at a pure output. The [amplitude-damping theorem](../science/geometry_and_examples.md) adds matching finite-error bounds, with a lower bound over unrestricted physical decoders and a constructive upper bound. The one-way error exponent is not obtained by transferring the qualitative interaction reduction.

## horodecki2003

**Michael Horodecki, Peter W. Shor, and Mary Beth Ruskai.** *Entanglement Breaking Channels*. Reviews in Mathematical Physics **15**, 629–641 (2003). [DOI](https://doi.org/10.1142/S0129055X03001709); [arXiv:quant-ph/0302031v2](https://arxiv.org/abs/quant-ph/0302031v2).

Theorem 4 supplies the standard equivalence among entanglement breaking, a separable Choi state, and a measure-and-prepare representation. That representation gives one sufficiency branch of the exact classification. The criterion for a pure-output qubit channel is proved explicitly in the [normal-form lemma](../science/exact_classification.md#structure-at-a-pure-output), using only positivity of the partial transpose as a necessary condition for separability.

## tang2026

**Ziao Tang, Chengkai Zhu, Ge Bai, and Xin Wang.** *Classical Capacity and Entanglement Cost of the Amplitude Damping Channel*. [arXiv:2609.28592v1](https://arxiv.org/abs/2609.28592v1), September 2026.

This work studies the same structural class of qubit channels admitting a pure output, including amplitude damping, and establishes additivity results for classical capacity and parallel entanglement cost. The structural overlap is relevant, but the resource tasks differ. Its entanglement-cost simulation acts on arbitrary unknown inputs over many channel uses with classical communication free. Here the input description is known, preshared entanglement is unavailable, and a single-use classical alphabet is charged. Those capacity and entanglement-cost formulas do not determine this alphabet or its accuracy exponent.

## liu2026

**Kai Liu and Deguang Han.** *Intermediate memory costs of quantum channel synthesis with a protected subsystem*. [arXiv:2610.20536v1](https://arxiv.org/abs/2610.20536v1), October 2026; [full text](https://arxiv.org/html/2610.20536v1).

Section V.4 gives an exact classical-program obstruction for two prescribed amplitude-damping branches under a protected-subsystem graph constraint. Distinct extreme channels require disjoint classical program supports, conflicting with the required overlap. Its resource counts the total intermediate carrier and permits no free side channel or shared randomness. The present task fixes one channel and varies a continuum of classically described inputs, with unrestricted input-independent shared randomness. A classical branch-program obstruction therefore does not supply the positive-effect tangent or cap-area converses used here.

## castellano2026

**Riccardo Castellano, Pavel Sekatski, and Nicolas Brunner.** *The cost of classically simulating quantum communication is as high as it could be*. [arXiv:2610.19060v1](https://arxiv.org/abs/2610.19060v1), October 2026.

This paper studies ordinary prepare-and-measure correlations: Alice receives a classical state description and Bob receives a classical measurement description. It distinguishes finite expected bits, expected alphabet size, and worst-case alphabet size, and treats bounded-alphabet approximation. Here Bob instead holds an unknown physical system. His response must be a positive affine functional of that system's state. A scalar response rule based on a fully known measurement description does not automatically define such a physical effect. The expected-bit results also do not settle the worst-case alphabet charged here.

## watrous2018

John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018). The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies the manuscript and individual chapters. This is the single educational anchor. The [learning bridge](../learning/ANCHOR.md) selects its operator, convexity, state, channel, measurement, distinguishability, and separability material and translates the conventions used here. The project-specific finite-menu obstruction and amplitude-damping bounds are developed in the scientific pages; the textbook is not cited as a source for those results.

## Contribution and source boundaries

The exact classification and matching fixed-channel amplitude-damping exponent are the results established in this repository. Standard channel representations, convex separation, Carathéodory's theorem, trace-distance contractivity and spherical area estimates supply mathematical tools. The geometric argument and the finite-effect converses are given in full rather than inferred from numerical examples.

The comparisons above use the stated arXiv versions. Naik et al.'s complete journal text was not available for a line-by-line version comparison; the full arXiv v2 was inspected. For Castellano et al., the primary arXiv abstract and the authors' manuscript text reproduced by [PaperPeel](https://www.paperpeel.com/paper/2610.19060) were inspected, including its model and bounded-alphabet section. Its direct versioned arXiv HTML was unavailable during that check. These are explicit limits on the literature comparison; the proofs in this repository do not depend on an exhaustive priority claim.
