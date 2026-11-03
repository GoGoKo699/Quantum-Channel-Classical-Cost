# Thirty milestones for understanding classical channel cost

This map follows the scientific question from a physical measurement to the exact classification and the sharp amplitude-damping accuracy law. Its single educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/). The [source bridge](ANCHOR.md) explains how that foundation connects to the project.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background joins operators, side information, error and communication into one experiment. The narrative then develops two connected arguments: a boundary obstruction for exact simulation and matching geometric bounds for approximate simulation. Each phase ends by assembling its components. The map supplies global understanding; the canonical science pages retain the full technical proofs.

Watrous section numbers refer to the author's [2018 manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). These references supply prerequisites. The finite-effect lemma, classification and amplitude-damping cost proofs are developed in the linked project sources. Research attribution remains in [related work](../references/RELATED_WORK.md).

## Phase I: background and preliminaries, M01–M12

### M01 · States as operational objects

- **Central question:** What information does a qubit density operator specify?
- **Understanding target:** Connect positivity and unit trace to valid measurement probabilities, and distinguish a pure state from a statistical mixture.
- **Dependencies and story role:** No earlier milestone; establishes the object whose channel output must be simulated.
- **Conceptual connection:** A state description predicts outcomes, while a physical copy can participate in a joint measurement.
- **Sources:** Watrous §2.1.2; [the experiment being simulated](../science/model.md#the-experiment-being-simulated).

### M02 · Effects describe physical responses

- **Central question:** What restricts the probability rule of a physical decoder?
- **Understanding target:** Explain an effect as a positive operator bounded by the identity, and a POVM as effects summing to the identity.
- **Dependencies and story role:** M01; converts an operational output probability into an operator constraint.
- **Conceptual connection:** Positivity will limit Bob even when his processor includes ancillas, private randomness and dependence on the whole requested measurement.
- **Sources:** Watrous §2.3.1; [allowed one-way protocols](../science/model.md#allowed-one-way-protocols).

### M03 · Channels preserve physical consistency

- **Central question:** Why require complete positivity and trace preservation?
- **Understanding target:** Explain how these conditions make a channel valid on states and on extensions with untouched systems.
- **Dependencies and story role:** M01–M02; introduces the fixed transformation whose outputs define the simulation task.
- **Conceptual connection:** Reference systems clarify physical validity without changing Alice's input into an unknown quantum register.
- **Sources:** Watrous §2.2.1; [the channel and input specification](../science/model.md#the-experiment-being-simulated).

### M04 · Kraus and Choi descriptions

- **Central question:** How can one channel be studied through operators or a bipartite matrix?
- **Understanding target:** Relate a Kraus representation to the channel action and distinguish the normalized Choi state from the unnormalized Choi operator.
- **Dependencies and story role:** M03; prepares the algebra used at a pure output.
- **Conceptual connection:** Kraus operators expose restrictions on individual output vectors; the Choi state exposes entanglement-breaking constraints. Normalization accounts for factors of two.
- **Sources:** Watrous §2.2.2; [structure at a pure output](../science/exact_classification.md#structure-at-a-pure-output).

### M05 · A classical description changes the encoder

- **Central question:** What can Alice do because she knows the state description?
- **Understanding target:** Distinguish arbitrary probabilities computed from a description from probabilities obtained by measuring an unknown input state.
- **Dependencies and story role:** M01–M03; fixes the sender's information before resource bounds are discussed.
- **Conceptual connection:** Nonlinear dependence on a known description allows finite exact simulation of some channels that are not entanglement breaking.
- **Sources:** Watrous §§2.1.2, 2.3.1 for state and measurement foundations; [encoder definition](../science/model.md#allowed-one-way-protocols).

### M06 · Unknown side inputs and untouched references

- **Central question:** What must survive when Bob's system is correlated with something inaccessible?
- **Understanding target:** Identify Alice's described state, Bob's physical side input, the untouched reference and the classical outcome as distinct objects.
- **Dependencies and story role:** M02–M05; assembles the systems in the experiment.
- **Conceptual connection:** The outcome together with its conditional reference state records more information than the outcome distribution alone.
- **Sources:** Watrous §2.1.3; [ideal classical–quantum output](../science/model.md#the-experiment-being-simulated).

### M07 · Error has an operational meaning

- **Central question:** What does a uniform accuracy promise control?
- **Understanding target:** Interpret total variation and half the trace norm as distinguishability errors; distinguish statistical accuracy from reference-stable accuracy.
- **Dependencies and story role:** M02, M06; makes the approximation target precise.
- **Conceptual connection:** Discarding a reference weakens the requirement. Preparation within trace distance gives a guarantee after any requested measurement through contractivity.
- **Sources:** Watrous §§1.1.3, 3.1.1, 3.3.2; [accuracy and cost](../science/model.md#accuracy-and-cost) and [preparation sufficiency](../science/model.md#why-state-preparation-is-sufficient-for-the-upper-bounds).

### M08 · Convex mixtures become Bloch geometry

- **Central question:** How does a finite collection of states generate a family of possible outputs?
- **Understanding target:** Connect probabilistic preparation to convex combinations, pure qubit states to the sphere and mixed states to its interior.
- **Dependencies and story role:** M01, M03; supplies the geometric language for constructive protocols.
- **Conceptual connection:** A polytope of physical states can contain an entire channel image, allowing one fixed preparation menu to serve many inputs.
- **Sources:** Watrous §§1.2.1, 2.1.2; [interior-image construction](../science/exact_classification.md#a-channel-image-strictly-inside-the-bloch-ball).

### M09 · The charged resource is a global alphabet

- **Central question:** What does a finite worst-case message bound actually restrict?
- **Understanding target:** Distinguish the number of possible labels from average message length, shared-randomness entropy and local computational work.
- **Dependencies and story role:** M05, M08; identifies the resource before comparing protocols.
- **Conceptual connection:** Each shared seed permits at most $`M`$ labels, although the decoder's effects may vary over infinitely many seeds. One label means zero transmitted bits.
- **Sources:** Watrous §1.2.2 for probability foundations; [protocols](../science/model.md#allowed-one-way-protocols) and [cost definition](../science/model.md#accuracy-and-cost).

### M10 · Measure-and-prepare channels supply a positive case

- **Central question:** Why does entanglement breaking suggest a finite classical protocol?
- **Understanding target:** Explain how a finite measure-and-prepare representation becomes sampling a label from Alice's description and preparing its associated state at Bob.
- **Dependencies and story role:** M04–M06, M09; establishes one exact construction.
- **Conceptual connection:** Separability of a Choi state and finite classical preparation meet here; the standard characterization is credited to Horodecki, Shor and Ruskai.
- **Sources:** Watrous §6.1.1; [entanglement-breaking construction](../science/exact_classification.md#an-entanglement-breaking-channel) and [primary attribution](../references/RELATED_WORK.md#horodecki2003).

### M11 · A Bell measurement tests an operator

- **Central question:** How can one binary measurement constrain every possible decoder?
- **Understanding target:** Explain why matching its probability for every unknown side qubit fixes the effective operator to half the transposed channel output.
- **Dependencies and story role:** M02, M04, M06–M07; turns generic simulation into a necessary matrix condition.
- **Conceptual connection:** The Bell identity supplies a lower-bound test without imposing state preparation or measurement noncontextuality on Bob.
- **Sources:** Watrous §§1.1.2, 2.3.1 for operator and measurement foundations; [Bell reduction](../science/model.md#why-one-bell-measurement-is-enough-for-the-lower-bounds).

### M12 · Assemble the complete experiment

- **Central question:** Which guarantees must one protocol satisfy simultaneously?
- **Understanding target:** State the input, output, free resources, uniform quantifiers and two error criteria, including the encoder's independence from the requested measurement and side dimension.
- **Dependencies and story role:** M01–M11; integrates the background into one operational model.
- **Conceptual connection:** Separate one-way quantitative cost from finite-tree exact feasibility; the latter reduction need not preserve the alphabet size.
- **Sources:** Watrous §§2.1–2.3, 3.1.1 as foundations; [operational model](../science/model.md), especially [interaction scope](../science/model.md#finite-interaction-and-the-scope-of-the-results).

## Phase II: narrative and innovation, M13–M30

### M13 · Positivity couples population and coherence

- **Central question:** What happens to an off-diagonal entry when a positive matrix approaches a boundary state?
- **Understanding target:** Explain how the two-by-two principal-minor inequality bounds coherence using diagonal populations.
- **Dependencies and story role:** M02, M04; isolates the local matrix constraint behind the converse.
- **Conceptual connection:** A response effect with a vanishing population in one direction must also lose its corresponding coherence.
- **Sources:** Watrous §1.1.3; [finite-random-effect lemma, positivity step](../science/exact_classification.md#a-finite-collection-of-random-effects-has-no-coherent-boundary-tangent).

### M14 · Finite menus cannot sustain the boundary tangent

- **Central question:** Why does continuous shared randomness fail to remove the finite-menu obstruction?
- **Understanding target:** Follow the split between small and large positive entries, and the order of the two limits yielding $`\lvert c_t\rvert^2/q_t\to0`$.
- **Dependencies and story role:** M09, M13; upgrades a local positivity bound to a constraint on all allowed randomized menus.
- **Conceptual connection:** Finiteness is needed at each seed; a uniform positive lower bound across all seeds is unnecessary.
- **Sources:** Watrous §§1.2.1–1.2.2 for analysis and probability foundations; [Lemma 1 and its proof](../science/exact_classification.md#a-finite-collection-of-random-effects-has-no-coherent-boundary-tangent).

### M15 · A pure output forces a normal form

- **Central question:** What does a channel's pure output imply about its Kraus operators?
- **Understanding target:** Explain the pure-preimage reduction and why each Kraus operator maps that input ray into the same output ray.
- **Dependencies and story role:** M04, M08; identifies the channel structure to compare with M14.
- **Conceptual connection:** After basis changes, upper-triangular Kraus operators isolate the coherence multiplier $`\gamma`$ and population parameter $`b`$.
- **Sources:** Watrous §§1.2.1, 2.2.2; [Lemma 2, normal-form derivation](../science/exact_classification.md#structure-at-a-pure-output).

### M16 · Coherence distinguishes the entanglement-breaking branch

- **Central question:** What does $`\gamma=0`$ mean within the pure-output normal form?
- **Understanding target:** Connect zero coherence multiplier to an explicit two-label measure-and-prepare map, and nonzero multiplier to a negative partial-transpose principal minor.
- **Dependencies and story role:** M10, M15; identifies the exact dividing condition within channels possessing a pure output.
- **Conceptual connection:** The proof uses positive partial transpose as a necessary condition for separability; it does not require a general sufficiency assertion.
- **Sources:** Watrous §6.1.1; [Lemma 2, entanglement-breaking equivalence](../science/exact_classification.md#structure-at-a-pure-output).

### M17 · A surviving tangent contradicts finite simulation

- **Central question:** How does the channel's local behavior violate the finite-effect lemma?
- **Understanding target:** Compare the quadratic small population with the linear coherence along a pure-input path, then apply the Bell transpose and factor one half.
- **Dependencies and story role:** M11, M14–M16; completes the impossibility direction.
- **Conceptual connection:** The target ratio tends to a positive constant, while every finite random menu forces it to zero. Arbitrary physical contextual decoders remain covered.
- **Sources:** Watrous §§2.2.2, 2.3.1 as foundations; [necessity proof](../science/exact_classification.md#necessity-a-surviving-tangent-prevents-finite-simulation).

### M18 · Two constructions establish sufficiency

- **Central question:** How can the entire output family be generated with finitely many labels?
- **Understanding target:** Explain compactness and polytope containment for an image strictly inside the Bloch ball, alongside the entanglement-breaking construction.
- **Dependencies and story role:** M08–M10; supplies the positive direction complementing M17.
- **Conceptual connection:** A measurable convex-decomposition rule defines Alice's probabilities, and exact average preparation preserves all side-reference correlations.
- **Sources:** Watrous §§1.2.1, 6.1.1; [both sufficiency constructions](../science/exact_classification.md#sufficiency-two-finite-constructions).

### M19 · The exact boundary depends on output geometry

- **Central question:** Which noisy qubit channels admit finite exact generic simulation?
- **Understanding target:** Apply the complete criterion to depolarization, incomplete and complete dephasing, amplitude damping and reset.
- **Dependencies and story role:** M12, M16–M18; integrates the exact theorem and its physical meaning.
- **Conceptual connection:** Noise alone does not decide feasibility. Depolarizing channels can be non-entanglement-breaking yet finitely simulable, while nonzero amplitude-damping survival retains the obstruction.
- **Sources:** Watrous §§2.2.3, 6.1.1 as foundations; [classification](../science/exact_classification.md#the-classification-theorem) and [examples](../science/exact_classification.md#examples-and-boundary-cases).

### M20 · Amplitude damping has two local scales

- **Central question:** How does an output become nearly pure close to the surviving ground state?
- **Understanding target:** Interpret the Bloch ellipsoid and the determinant $`\eta(1-\eta)p^2`$, with $`p`$ the input excited-state population and $`\eta`$ the survival probability.
- **Dependencies and story role:** M03, M08, M19; starts the quantitative problem from the channel's local geometry.
- **Conceptual connection:** The output direction changes on a different scale from its impurity, creating the accuracy-dependent family used in the converse.
- **Sources:** Watrous §§2.1.2, 2.2.2; [geometric explanation](../science/geometry_and_examples.md#why-the-exponent-is-one-half).

### M21 · Nearly pure outputs cover a shrinking cap

- **Central question:** Which output directions remain almost pure at error scale $`\varepsilon`$?
- **Understanding target:** Follow the dominant-eigenvector parametrization, monotone polar coordinate and area Jacobian for the explicit input disk.
- **Dependencies and story role:** M07, M11, M20; translates the local channel behavior into a measurable set of hard inputs.
- **Conceptual connection:** For fixed interior $`\eta`$, choosing population of order $`\sqrt\varepsilon`$ gives cap area of that order and orthogonal Bell leakage of order $`\varepsilon`$.
- **Sources:** Watrous §§1.1.3, 2.1.2; [lower-bound proof, Section 4](../science/amplitude_lower.md#4-an-explicit-input-disk-covers-a-cap-of-output-eigenvectors).

### M22 · Accuracy requires positive nearby weight

- **Central question:** Can a decoder distribute its Bell response among mostly unsuitable effects?
- **Understanding target:** Explain why small orthogonal leakage and a lower bound on total trace force a constant amount of response weight near each cap direction.
- **Dependencies and story role:** M02, M07, M21; extracts the quantitative restriction imposed by positivity.
- **Conceptual connection:** Dividing an effect by its trace is a proof device. The trace weights preserve the general physical decoder model.
- **Sources:** Watrous §§1.1.3, 2.3.1; [lower-bound proof, Section 5](../science/amplitude_lower.md#5-accurate-effects-require-a-constant-weight-of-nearby-response-states).

### M23 · Area counting gives the lower exponent

- **Central question:** How many response effects are needed to cover the hard directions?
- **Understanding target:** Combine the area served by one normalized effect with the required positive weight, and explain why averaging over shared seeds preserves the bound.
- **Dependencies and story role:** M09, M21–M22; completes the approximate converse.
- **Conceptual connection:** A cap of area proportional to $`\sqrt\varepsilon`$ requires order $`\varepsilon^{-1/2}`$ labels when each response serves area of order $`\varepsilon`$.
- **Sources:** Watrous §1.2.2 for probability foundations; [lower-bound proof, Section 6](../science/amplitude_lower.md#6-cap-area-counting-is-unchanged-by-arbitrary-shared-randomness).

### M24 · Regularization opens a support margin

- **Central question:** How much geometric space does a small allowed error buy?
- **Understanding target:** Interpret a support function, its quartic deficit in the polar normal angle and the additional margin produced by mixing with the maximally mixed state.
- **Dependencies and story role:** M07–M08, M20; begins a constructive protocol from supporting planes.
- **Conceptual connection:** The global support inequality justifies the construction; the local quartic expansion explains its mesh scales.
- **Sources:** Watrous §1.2.1; [upper-bound proof, Sections 1–2](../science/amplitude_upper.md#1-the-output-ellipsoid-and-its-sphere-contact).

### M25 · Adapt the net to the available margin

- **Central question:** Where must the preparation vertices be dense?
- **Understanding target:** Explain the inner cap, dyadic annuli and outer region, then relate their covering radii to their numbers of vertices.
- **Dependencies and story role:** M24; constructs a finite menu with the desired scaling.
- **Conceptual connection:** A uniform mesh wastes vertices away from the pure output. Summing the annular counts gives order $`\varepsilon^{-1/2}`$ vertices for fixed interior survival.
- **Sources:** Watrous §1.2.1 for compactness foundations; [upper-bound proof, Section 3](../science/amplitude_upper.md#3-a-finite-spherical-net-with-the-required-mesh).

### M26 · Support domination certifies containment

- **Central question:** Why does the net work for every output, including mixed inputs?
- **Understanding target:** Compare the angular support loss of a nearby vertex with the regularized ellipsoid's support deficit in every direction.
- **Dependencies and story role:** M08, M24–M25; turns a collection of nearby directions into a global containment statement.
- **Conceptual connection:** Separating hyperplanes show that domination of every support value places the entire regularized channel image inside the preparation polytope.
- **Sources:** Watrous §1.2.1; [upper-bound proof, Section 4](../science/amplitude_upper.md#4-the-nets-convex-hull-contains-every-regularized-output).

### M27 · Turn containment into a physical protocol

- **Central question:** How do vertices become messages with a reference-stable guarantee?
- **Understanding target:** Describe measurable convex decomposition, label sampling, local preparation and the requested joint measurement, then propagate the trace-distance bound.
- **Dependencies and story role:** M05–M09, M26; completes the constructive direction.
- **Conceptual connection:** Four vertices may suffice in one decomposition, but the charged alphabet contains every possible vertex label. No shared randomness is needed by this construction.
- **Sources:** Watrous §§1.2.1, 2.3.1, 3.3.2; [upper-bound protocol and error analysis, Sections 5–6](../science/amplitude_upper.md#5-the-communication-protocol).

### M28 · Match the law and separate its endpoints

- **Central question:** What do the two bounds establish, and where does their regime end?
- **Understanding target:** Derive the half-logarithmic bit law from the matching alphabet exponent, while keeping survival fixed and treating reset and identity separately.
- **Dependencies and story role:** M12, M23, M27; integrates the approximation theorem.
- **Conceptual connection:** Reset needs one label; identity requires order $`\varepsilon^{-1}`$ labels. Parameter-dependent constants prevent an unsupported interchange of limits.
- **Sources:** Watrous §§1.1.3, 2.2.1 as foundations; [sharp theorem](../science/geometry_and_examples.md#the-sharp-amplitude-damping-theorem) and [endpoints](../science/geometry_and_examples.md#endpoints-and-other-channels).

### M29 · Separate inherited ingredients, new proofs and checks

- **Central question:** What supports each part of the scientific account?
- **Understanding target:** Distinguish textbook foundations, the inherited generic-simulation framework and standard entanglement-breaking theorem, the present proofs, and finite numerical checks.
- **Dependencies and story role:** M19, M28; places the results in their evidential and literature context.
- **Conceptual connection:** Matrix tests expose convention errors; analytical arguments establish universal claims. Neighboring capacity and ordinary sampling tasks charge different resources.
- **Sources:** Watrous §§2.2–2.3, 6.1.1 as foundations; [related work](../references/RELATED_WORK.md) and [verification guide](../verification/README.md).

### M30 · Explain the complete communication story

- **Central question:** Why can some noisy channels be simulated exactly while amplitude damping has a diverging accuracy cost?
- **Understanding target:** Connect the experiment, coherent pure-output boundary, finite constructions and matching approximate bounds into one explanation with its assumptions intact.
- **Dependencies and story role:** M12, M19, M28–M29; synthesizes both phases and the contribution as a whole.
- **Conceptual connection:** Output geometry controls this known-input classical interface. The established conclusions concern exact feasibility and one-way worst-case accuracy cost, with separate boundaries for interaction, expected communication and implementation complexity.
- **Sources:** Watrous Chapters 1–3 and §6.1.1 as the shared foundation; [model](../science/model.md), [classification](../science/exact_classification.md) and [geometric synthesis](../science/geometry_and_examples.md#resource-interpretation).
