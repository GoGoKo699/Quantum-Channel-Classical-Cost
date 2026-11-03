# From Watrous to finite-message qubit simulation

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the 2018 manuscript and individual chapters. The section numbers below refer to that manuscript. The project uses one anchor, supported by the primary research citations in [related work](../references/RELATED_WORK.md).

The central question is concrete: if Alice knows a qubit state's complete description, how much classical information must she send so that Bob can use the channel output in a joint measurement with an unknown quantum system? Learning the state-and-measurement language makes the question precise. Convex geometry and positivity then explain why some noisy channels admit finite exact communication, while amplitude damping requires an alphabet that grows as the error decreases.

Use the [30-milestone map](MILESTONES.md) to follow the whole story. Its first 12 milestones assemble the background; its remaining 18 connect the exact obstruction, finite constructions, and matching accuracy law. This bridge identifies the needed textbook tools and supplies the conceptual steps into the project's proofs. Reading the entire book is unnecessary.

## Focused source route

| Watrous sections | What to take from the source | Where it enters this project |
|---|---|---|
| [1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf): operators, decompositions, and norms | Positive operators, eigenvalues, and trace and operator norms | States, physical response effects, and error bounds in the [model](../science/model.md) |
| [1.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf): analysis and convexity | Compactness, convex combinations, separation, and Carathéodory's theorem | Finite preparation menus in the [exact proof](../science/exact_classification.md#sufficiency-two-finite-constructions) |
| [2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): states, reductions, and purifications | Mixtures, tensor products, partial traces, and reference systems | The joint input and retained outcome–reference state |
| [2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): channels and representations | Complete positivity, Kraus operators, and Choi operators | The [pure-output normal form](../science/exact_classification.md#structure-at-a-pure-output) |
| [2.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): measurements | A measurement is a family of positive effects summing to the identity | The reduction of arbitrary physical decoding to effects on Bob's system |
| [3.1.1 and 3.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf): discrimination and trace norms | Operational distinguishability; contractivity, including Corollary 3.40 | Uniform statistical error and the stronger reference guarantee |
| [6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf): separability | Positive combinations of product operators | The entanglement-breaking branch and its Choi-state test |

Begin with the first, third, and fifth rows to understand the experiment. Return to convexity for the constructions and to channel representations and separability for the classification. The cap-area converse and adaptive spherical construction are developed in the repository; they are not textbook theorems being assigned under different names.

## Notation and normalization

Watrous writes a vector as $`u`$ and its rank-one operator as $`uu^*`$. Here these are often $`|u\rangle`$ and $`|u\rangle\langle u|`$. His adjoint symbol $`*`$ corresponds to $`\dagger`$; his identity operator $`1_{\mathcal X}`$ corresponds to $`I_X`$. The operator space and density-operator set appear here as $`\mathcal L(X)`$ and $`\mathcal D(X)`$. A physical effect is positive and bounded above by the identity; unlike a state, its trace need not be one.

The project defines distance between states using the explicit half-trace-norm convention

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

For diagonal classical states this is total variation distance. The factor one half also appears in the outcome–reference error. The Bell-test lower bound instead uses the operator norm of a difference of effects. These norms measure different operational comparisons and should not be interchanged.

Choi normalization and tensor order require a second translation. Watrous's equation (2.65) uses the unnormalized operator in output–input order:

```math
J(\mathcal N)
=\sum_{i,j=0}^1\mathcal N(|i\rangle\langle j|)
\otimes|i\rangle\langle j|.
```

For a qubit channel it has trace two. Dividing by two gives a normalized Choi state in that order. In input–output order, the corresponding state is

```math
\chi_{\mathcal N}
=\frac12\sum_{i,j=0}^1|i\rangle\langle j|
\otimes\mathcal N(|i\rangle\langle j|)
=\frac12 S J(\mathcal N)S^\dagger,
```

where $`S`$ swaps the two factors. This is the order underlying the displayed principal minor in the [pure-output lemma](../science/exact_classification.md#structure-at-a-pure-output). Swapping factors preserves separability and the relevant positivity condition, but changes where matrix entries sit. Fix both the order and the normalization before comparing entries.

The transpose in the Bell identity below is an ordinary matrix transpose in the chosen computational basis. It is neither an adjoint nor a physical transposition operation performed by Bob.

## What the classical description changes

Alice can compute probabilities from the known matrix $`\rho`$. Her encoding rule may be nonlinear in that description. It therefore need not be a quantum measurement that could be applied to an unknown copy of the state. Bob, however, receives his side system physically. His response probabilities must arise from positive measurement effects on that system, even when the requested joint measurement is known to him.

This asymmetry is the heart of the model. It explains how a channel that is not entanglement breaking can nevertheless have a finite classical simulation in this experiment. The positive protocol uses knowledge of the input description. It does not give a classical replacement for an unknown quantum input entangled with an external system.

The reference $`R`$ belongs to Bob's supplied state $`\omega_{BR}`$. The experiment starts from $`\rho_A\otimes\omega_{BR}`$, and ends with the outcome $`Y`$ and untouched $`R`$. Matching their joint state controls both outcome probabilities and conditional reference states. The measured systems are discarded; no target post-measurement state on those systems is prescribed.

## A complete two-label example

Consider complete dephasing in the computational basis:

```math
\Delta\!\begin{pmatrix}1-p&c\\\overline c&p\end{pmatrix}
=\begin{pmatrix}1-p&0\\0&p\end{pmatrix}.
```

Alice knows $`p`$ and $`c`$. She samples a bit $`m`$, choosing $`m=1`$ with probability $`p`$, and sends it. Bob prepares $`|m\rangle\langle m|`$ and performs the requested joint measurement with his actual side input. Averaging over the bit prepares exactly $`\Delta(\rho)`$. The global message alphabet is $`\{0,1\}`$, so one bit suffices, with no shared randomness.

This remains exact when Bob's side input is entangled with a reference: the averaged state before the measurement is exactly $`\Delta(\rho)\otimes\omega_{BR}`$. Applying the same physical measurement therefore gives the same outcome–reference state.

For a numerical instance, take $`p=1/4`$. If Bob's unknown side qubit has population $`a`$ on $`|0\rangle`$, a Bell-projector outcome has probability

```math
\Pr(\Phi^+)
=\frac12\left(\frac34a+\frac14(1-a)\right)
=\frac{1+2a}{8}.
```

Conditioned on Alice's two messages, Bob's effective Bell-outcome effects are $`|0\rangle\langle0|/2`$ and $`|1\rangle\langle1|/2`$. Their probability-weighted average reproduces the displayed answer for every unknown side state. The state-preparation protocol works for every requested POVM; the Bell calculation simply makes one observable consequence explicit.

Complete dephasing is an entanglement-breaking channel. Residual coherence changes the exact conclusion: if dephasing retains any nonzero multiple of the off-diagonal entry, its pure basis outputs have a surviving coherence tangent, and finite exact simulation becomes impossible. The [classification proof](../science/exact_classification.md) establishes that discontinuity.

## From a Bell outcome to the exact obstruction

Write $`\Phi=|\Phi^+\rangle\langle\Phi^+|`$ for the Bell projector. For any qubit output $`\sigma`$ and unknown side state $`\tau`$,

```math
\mathrm{Tr}[\Phi(\sigma\otimes\tau)]
=\frac12\mathrm{Tr}(\sigma^{\mathsf T}\tau).
```

The transpose matters for complex states. For example, two copies of $`(|0\rangle+i|1\rangle)/\sqrt2`$ have zero overlap with the Bell vector, consistent with this formula.

Every physical decoder for this binary outcome supplies an effect $`F_{\lambda,m}`$ on Bob's qubit. At each shared seed there are at most $`M`$ such effects. Alice changes their mixing probabilities as her input changes. Uniform exact agreement for every side state fixes the entire averaged effect, forcing it to equal $`\mathcal N(\rho)^{\mathsf T}/2`$.

Near a pure output, write the small diagonal entry of this effect as $`q_t`$ and its off-diagonal entry as $`c_t`$. Positivity bounds each response's coherence. The repository's finite-random-effect lemma strengthens that bound for a fixed finite menu, even with continuous shared randomness:

```math
q_t\longrightarrow0
\quad\Longrightarrow\quad
\frac{|c_t|^2}{q_t}\longrightarrow0.
```

If $`q_t=0`$, positivity also forces $`c_t=0`$; the ratio is defined as zero in that case.

A non-entanglement-breaking qubit channel with a pure output instead gives a positive limiting ratio. This incompatibility proves the converse. The argument requires a measure-theoretic step to control the shared seeds; a picture of a finite deterministic polygon alone would not prove it.

The positive cases use different geometry. If every output is mixed, compactness places the whole output set strictly inside the Bloch sphere. A finite polytope of pure states can contain it, letting Alice sample a vertex label. Entanglement-breaking channels have a finite measure-and-prepare representation. These two constructions and the converse give the complete exact criterion.

## Why amplitude damping has a half-logarithmic bit cost

Amplitude damping with fixed survival parameter $`0\lt\eta\lt1`$ keeps the north-pole state pure but contracts and shifts other Bloch vectors. Exact finite simulation fails. Allowing a small error opens a geometric margin and makes finite preparation possible.

The lower proof follows nearly pure outputs. Inputs with excited-state population $`p`$ generate a cap of principal output directions with area proportional to $`p`$, while the small output eigenvalue is proportional to $`p^2`$. Choosing $`p`$ of order $`\sqrt\varepsilon`$ therefore leaves a cap of area of order $`\sqrt\varepsilon`$ whose directions are all almost pure. Each useful response effect covers only order $`\varepsilon`$ area at the required accuracy. Averaging positive response weights over the cap and shared seed forces order $`\varepsilon^{-1/2}`$ messages. See the [cap-area proof](../science/amplitude_lower.md).

The upper proof uses the support function of the output ellipsoid. Its deficit from the sphere is quartic near the contact direction. Adding output depolarization of order $`\varepsilon`$ permits a nonuniform spherical mesh, dense near that direction and coarser farther away. Its convex hull contains every regularized output and uses order $`\varepsilon^{-1/2}`$ vertices. The [construction](../science/amplitude_upper.md) proves containment and counting with global inequalities.

An individual convex decomposition may use only four vertices. The communication resource counts all labels that can occur across all inputs, so its alphabet is the full menu, not four. Shared randomness is unnecessary for this upper bound and remains unrestricted in the lower bound.

Together the arguments give, for fixed interior $`\eta`$,

```math
M_\eta(\varepsilon)=\Theta_\eta(\varepsilon^{-1/2}),
\qquad
C_\eta(\varepsilon)=\tfrac12\log_2(1/\varepsilon)+O_\eta(1).
```

The construction first bounds the trace distance of the averaged prepared state. Tensoring with $`\omega_{BR}`$ preserves that bound; applying the measurement-and-discard channel cannot increase it. This supplies the reference-stable guarantee. At complete reset one label suffices exactly; at the identity endpoint the optimal alphabet is of order $`\varepsilon^{-1}`$. The fixed-channel constants cannot be treated as uniform at either endpoint.

## Where the textbook ends and the research begins

Watrous supplies the operator, channel, measurement, distance, and convexity language. The operational setting, exact identity obstruction, depolarizing constructions, and finite-interaction feasibility reduction are credited to [Naik and coauthors](../references/RELATED_WORK.md#naik2026). The standard entanglement-breaking characterization is credited to [Horodecki, Shor, and Ruskai](../references/RELATED_WORK.md#horodecki2003). These are research dependencies, not additional educational anchors.

The repository supplies the finite-effect tangent lemma, its complete qubit-channel classification, and the matching amplitude-damping cap and net arguments. Its [verification guide](../verification/README.md) checks matrix conventions and representative identities; the universal results use the analytical proofs. The exact finite-versus-infinite classification also covers uniformly finite public interaction trees. The quantitative accuracy law is one-way, counts the worst-case alphabet, and makes no claim about expected communication, optimal interaction, local computation time, or state-synthesis precision.

Continue with the [milestone map](MILESTONES.md), or use the [science route](../science/README.md) to enter the canonical statements and proofs directly.
