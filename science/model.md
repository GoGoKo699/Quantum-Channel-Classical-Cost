# Operational model and communication resource

A classical description of a qubit is enough to reproduce many of its measurement statistics with a short classical message. A different question arises when the receiver must combine that qubit with an **unknown quantum system**. The simulator must then supply a physical operation on the receiver's system, including its correlations with an untouched reference.

We use the generic channel-simulation setting of [Naik, Zartab, Gisin, and Banik](https://arxiv.org/html/2501.15807v2). Their perfect-channel obstruction and finite simulations of depolarizing channels are the starting points. The results here classify all qubit channels for exact finite communication and determine the one-way accuracy cost of amplitude damping.

## The experiment being simulated

Fix a known qubit-to-qubit completely positive trace-preserving channel

```math
\mathcal N:\mathcal L(A)\longrightarrow\mathcal L(A'),
\qquad
A\cong A'\cong\mathbb C^2.
```

Alice receives the complete classical description of an arbitrary density operator $`\rho_A`$. Bob receives a physical system $`B`$ in an unknown state. It may be correlated or entangled with an inaccessible reference $`R`$: its joint state is an arbitrary $`\omega_{BR}`$. The supplied input to the experiment is

```math
\rho_A\otimes\omega_{BR}.
```

The description of $`\rho_A`$ gives Alice no information about $`\omega_{BR}`$. Requiring the protocol to work for every $`\rho_A`$ and every $`\omega_{BR}`$ also permits the side state to be chosen adversarially after the input description is specified. It does not supply Alice with an unknown quantum input entangled with Bob.

Bob is asked to perform an arbitrary finite-outcome POVM $`\mathsf Q=\{Q_y\}_y`$ on $`A'B`$, where $`Q_y\ge0`$ and $`\sum_y Q_y=I_{A'B}`$. The systems $`A'B`$ are discarded after the measurement. The target output is the outcome register $`Y`$ together with the untouched reference:

```math
\Omega^{\mathrm{ideal}}_{\rho,\omega,\mathsf Q}
=
\sum_y |y\rangle\langle y|_Y\otimes
\operatorname{Tr}_{A'B}
\left[
(Q_y\otimes I_R)
\bigl(\mathcal N(\rho)\otimes\omega_{BR}\bigr)
\right].
```

Each reference block is positive: equivalently, insert $`\sqrt{Q_y}`$ on both sides of the joint state before tracing out $`A'B`$. This formulation records both the outcome probabilities and the conditional reference states. It is therefore stronger than checking the outcome distribution alone.

The systems $`B`$ and $`R`$ may have any finite dimensions, and the same simulation guarantee must hold for every such choice. Bob knows the requested POVM but does not know his supplied quantum state. The classical message is an interface for the fixed channel: Alice's encoder is independent of Bob's later measurement choice and side-system dimension.

## Allowed one-way protocols

Alice and Bob may share an arbitrary classical random variable $`\lambda`$ with law $`\mu`$ on a probability space $`(\Lambda,\mathcal F,\mu)`$. Its law is independent of the external inputs and measurement request. There is no restriction to a finite or discrete shared-randomness space.

Alice sends one message from the alphabet

```math
[M]=\{1,\ldots,M\}
```

using a stochastic encoder $`p(m\mid\rho,\lambda)`$. These probabilities may be nonlinear functions of the known density operator. They are not required to arise from a quantum measurement on an unknown input. For each input, they are nonnegative and sum to one.

For every $`(\lambda,m,\mathsf Q)`$, Bob may use an arbitrary physical local processor on his actual side system, with local ancillas and private randomness. Because its required output is classical, its action is described by a POVM

```math
\mathsf F^{\lambda,m,\mathsf Q}
=
\{F_y^{\lambda,m,\mathsf Q}\}_y
\quad\text{on }B.
```

In particular,

```math
0\le F_y^{\lambda,m,\mathsf Q}\le I_B,
\qquad
\sum_y F_y^{\lambda,m,\mathsf Q}=I_B.
```

The entire requested POVM is an argument of the decoder. We impose no measurement-noncontextuality assumption and do not require Bob to reconstruct a quantum state before measuring. Private decoder randomness is already included in these effects.

The simulated classical–quantum output is

```math
\begin{aligned}
\Omega^{\mathrm{sim}}_{\rho,\omega,\mathsf Q}
={}&
\int_\Lambda d\mu(\lambda)
\sum_{m=1}^M p(m\mid\rho,\lambda)
\sum_y |y\rangle\langle y|_Y\\
&\otimes
\operatorname{Tr}_B
\left[
(F_y^{\lambda,m,\mathsf Q}\otimes I_R)
\omega_{BR}
\right].
\end{aligned}
```

All encoder probabilities and matrix entries of decoder effects are assumed measurable in their arguments. The integrals are ordinary finite-dimensional operator integrals of bounded measurable functions. This permits continuous shared randomness while excluding undefined, nonmeasurable protocols.

No quantum communication or preshared entanglement is available. Every run produces an output: failed branches cannot be discarded without contributing to the simulation error.

## Accuracy and cost

A protocol has **reference-stable error** at most $`\varepsilon`$ when

```math
\frac12
\left\|
\Omega^{\mathrm{sim}}_{\rho,\omega,\mathsf Q}
-
\Omega^{\mathrm{ideal}}_{\rho,\omega,\mathsf Q}
\right\|_1
\le\varepsilon
```

uniformly over all allowed inputs, side systems, references, and requested POVMs. When $`R`$ is trivial, this becomes total variation distance between the classical outcome distributions. Exact simulation means $`\varepsilon=0`$.

We also consider the weaker **statistical error** criterion: set $`R`$ to be trivial and require total variation error at most $`\varepsilon`$ uniformly over every input, side-input state, side-system dimension, and requested POVM. Write $`M_{\mathcal N}^{\mathrm{ref}}(\varepsilon)`$ and $`M_{\mathcal N}^{\mathrm{stat}}(\varepsilon)`$ for the smallest one-way alphabet sizes under the two criteria, assigning infinity when no finite alphabet suffices. Tracing out a reference cannot increase distinguishability, so

```math
M_{\mathcal N}^{\mathrm{stat}}(\varepsilon)
\le
M_{\mathcal N}^{\mathrm{ref}}(\varepsilon).
```

At zero error the two conditions coincide: equality of each outcome probability for every side-input density operator fixes each effective POVM effect, and those effects also fix the conditional reference states. At positive error we use only the displayed ordering. All lower bounds below hold under the weaker statistical criterion, while the constructions satisfy the stronger reference criterion. Consequently the exact classification and the matching amplitude-damping scaling hold for both.

When no superscript is displayed, $`M_{\mathcal N}(\varepsilon)`$ means $`M_{\mathcal N}^{\mathrm{ref}}(\varepsilon)`$. The corresponding fixed-length binary communication cost is

```math
C_{\mathcal N}(\varepsilon)
=
\left\lceil\log_2 M_{\mathcal N}(\varepsilon)\right\rceil,
```

with the same infinity convention. An alphabet of size one costs zero bits. The alphabet bound is uniform in the input and shared-randomness realization; it is a worst-case resource.

The channel, input descriptions, requested measurements, local computation, local ancillas, and shared randomness are uncharged. The question concerns information-theoretic communication cost. It makes no claim about efficient classical computation of the encoding, digital precision, or laboratory synthesis of Bob's local states and measurements.

## Why one Bell measurement is enough for the lower bounds

The unrestricted decoder still has a useful physical constraint. Take $`B`$ to be a qubit and fix the two-outcome POVM

```math
\mathsf Q_\Phi=\{\Phi,I_{A'B}-\Phi\},
\qquad
\Phi=|\Phi^+\rangle\langle\Phi^+|,
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

For any side-input state $`\sigma_B`$,

```math
\operatorname{Tr}\!\left[
\Phi\bigl(\mathcal N(\rho)\otimes\sigma\bigr)
\right]
=
\operatorname{Tr}\!\left[
\frac{\mathcal N(\rho)^{\mathsf T}}2\,\sigma
\right],
```

where the transpose uses the basis defining $`|\Phi^+\rangle`$. If $`F_{\lambda,m}`$ is Bob's effect for this one requested outcome, the simulator induces

```math
E_\rho
=
\int_\Lambda
\sum_{m=1}^M
p(m\mid\rho,\lambda)F_{\lambda,m}\,d\mu(\lambda),
\qquad
0\le F_{\lambda,m}\le I_2.
```

Exact simulation for every unknown $`\sigma`$ requires the operator identity

```math
E_\rho=\frac{\mathcal N(\rho)^{\mathsf T}}2.
```

For an $`\varepsilon`$-accurate protocol, the corresponding necessary condition is

```math
\left\|
E_\rho-\frac{\mathcal N(\rho)^{\mathsf T}}2
\right\|_\infty
\le\varepsilon.
```

Indeed, a binary total variation error is the absolute error in either outcome probability, and the supremum of $`|\operatorname{Tr}(H\sigma)|`$ over states $`\sigma`$ is $`\|H\|_\infty`$ for Hermitian $`H`$.

This condition is used only as a lower-bound consequence of the full task. It is not asserted to be a sufficient test for generic simulation. It also remains necessary if Alice is told in advance that this single Bell measurement will be requested.

## Why state preparation is sufficient for the upper bounds

A constructive simulator may use a more restricted decoder. Suppose Alice's message makes Bob prepare a state $`\widehat\rho`$ satisfying

```math
\frac12\|\widehat\rho-\mathcal N(\rho)\|_1\le\varepsilon
```

uniformly in the known input, after averaging over all protocol randomness. Bob can then perform the actual requested measurement on $`\widehat\rho\otimes\omega_{BR}`$. Tensoring with a state preserves trace norm, and the measurement-and-discard operation is a channel, so trace-distance contractivity gives the full reference-stable guarantee.

Thus an approximate remote-preparation construction proves an upper bound even though general simulators are not required to prepare a state. The lower bounds retain the broader decoder class.

## Finite interaction and the scope of the results

For exact feasibility, we also allow a finite public communication tree: a finite number of rounds with uniformly finite message alphabets, arbitrary physical operations on Bob's quantum system between messages, and arbitrary shared randomness. The tree has no timing or other communication side channel.

[Naik et al., Proposition 1 and Appendix VII](https://arxiv.org/html/2501.15807v2#S4) show that finite interactive protocols can be converted into finite one-way protocols. Alice samples a complete contingent response strategy for all possible finite histories of Bob's messages and sends its label. Bob then executes his original quantum operations and reads the indicated response along the actual history. Summing over unused counterfactual responses reproduces the original statistics. The same reasoning preserves the conditional reference states, since each actual transcript has the original physical instrument on $`B`$.

A finite strategy table can be much larger than the original interactive transcript. Accordingly:

| Result | Communication model |
|---|---|
| Exact finite-versus-infinite classification | One-way protocols and finite public interaction trees |
| Matching amplitude-damping accuracy cost | One-way protocols with worst-case alphabet size $`M`$ |
| Finite expected communication with unbounded messages or stopping times | Not determined here |
| Sharp quantitative advantage or limitation of interaction | Not determined here |

A protocol that terminates almost surely but has no finite uniform communication tree is not covered by the qualitative interactive reduction used here.

## Relation to other simulation tasks

The unknown quantum side input is essential to the question. A decoder given only a classical measurement description can reproduce statistics without implementing the required measurement on an unknown physical system. Generic simulation asks for that stronger physical composition, following the cited work.

The known classical description on Alice's side is equally essential. These protocols do not replace an arbitrary unknown quantum input by a classical message, and their feasibility does not imply that the simulated channel is entanglement breaking. The input encoder can depend nonlinearly on its classical description.

The task concerns one use of the specified channel with a uniform accuracy guarantee. It is distinct from asymptotic quantum capacity, entanglement-assisted channel simulation, learning an unknown channel, and sampling the final output of a restricted circuit family.
