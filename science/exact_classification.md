# Exact classification of qubit channels

**A qubit channel has a finite exact generic classical simulation precisely when it has no pure output or is entanglement breaking.** A nonzero coherence tangent at a pure output is the obstruction. The result permits arbitrary input-independent shared randomness and arbitrary physical decoding on the receiver's unknown side system.

The [operational model](model.md) distinguishes ordinary outcome statistics from the stronger requirement to preserve conditional states of an untouched reference. The classification holds under both criteria. Its converse already follows from one fixed binary Bell measurement with one unknown side qubit.

The perfect-channel impossibility and finite simulation of every nontrivially depolarizing channel were established by [Naik, Zartab, Gisin, and Banik](https://arxiv.org/html/2501.15807v2). The argument below extends these endpoints to all qubit-to-qubit channels. The standard measure-and-prepare characterization of entanglement-breaking channels is due to [Horodecki, Shor, and Ruskai](https://arxiv.org/abs/quant-ph/0302031).

## The classification theorem

Let $`\mathcal N:\mathcal L(\mathbb C^2)\to\mathcal L(\mathbb C^2)`$ be a completely positive trace-preserving channel. The following conditions are equivalent:

1. $`\mathcal N`$ admits exact generic simulation with a finite one-way classical alphabet.
2. $`\mathcal N`$ admits exact generic simulation with a finite public communication tree.
3. Either every state in $`\mathcal N(\mathcal D(\mathbb C^2))`$ is strictly mixed, or $`\mathcal N`$ is entanglement breaking.

The two simulation statements allow arbitrary shared randomness with a law independent of the input, finite local ancillas, and unrestricted physical processors on Bob's side input. They hold for statistical simulation and for reference-stable simulation. In particular,

```math
M_{\mathcal N}^{\mathrm{stat}}(0)
=
M_{\mathcal N}^{\mathrm{ref}}(0)
\lt \infty
```

if and only if condition 3 holds. A finite public tree means a uniformly finite number of rounds and finite message alphabets, as specified in the model.

For a qubit, a state that is not pure is positive definite. Thus the first alternative in condition 3 is a statement that the entire compact channel image lies inside the Bloch ball, away from its boundary. It does not require that the image have nonzero volume.

## A finite collection of random effects has no coherent boundary tangent

The main obstruction is a property of positive operators.

**Lemma 1.** Let $`(\Lambda,\mathcal F,\mu)`$ be a probability space, let $`M\lt \infty`$, and let $`F_{\lambda,m}`$ be measurable $`2\times2`$ effects satisfying

```math
0\le F_{\lambda,m}\le I_2,
\qquad 1\le m\le M.
```

For every $`t>0`$, let $`p_t(m\mid\lambda)`$ be measurable probabilities with $`\sum_m p_t(m\mid\lambda)=1`$. Define

```math
E_t=\int_\Lambda\sum_{m=1}^M
p_t(m\mid\lambda)F_{\lambda,m}\,d\mu(\lambda),
```

and, in one fixed basis, write

```math
q_t=\langle1|E_t|1\rangle,
\qquad
c_t=\langle0|E_t|1\rangle.
```

If $`q_t\to0`$ as $`t\to0`$, then

```math
\frac{|c_t|^2}{q_t}\longrightarrow0,
```

where the ratio is defined to be zero when $`q_t=0`$.

**Proof.** Set

```math
f_{\lambda,m}=\langle1|F_{\lambda,m}|1\rangle,
\qquad
g_{\lambda,m}=\langle0|F_{\lambda,m}|1\rangle.
```

Positivity and the effect bound give

```math
|g_{\lambda,m}|^2
\le
\langle0|F_{\lambda,m}|0\rangle f_{\lambda,m}
\le f_{\lambda,m}.
```

In particular $`g_{\lambda,m}=0`$ whenever $`f_{\lambda,m}=0`$.

Fix $`\delta>0`$. For terms with $`f_{\lambda,m}\ge\delta`$, we have $`|g_{\lambda,m}|\le f_{\lambda,m}/\sqrt\delta`$. Their total absolute contribution to $`c_t`$ is at most $`q_t/\sqrt\delta`$.

For the remaining nonzero terms, define

```math
A_\delta
=
\left\{
\lambda:\text{some }m\in[M]\text{ has }
0\lt f_{\lambda,m}\lt \delta
\right\},
\qquad
H_\delta=\mu(A_\delta).
```

Cauchy–Schwarz, applied to the measure
$`p_t(m\mid\lambda)\,d\mu(\lambda)`$ on $`\Lambda\times[M]`$, yields

```math
\begin{aligned}
&\int_\Lambda\sum_m
p_t(m\mid\lambda)|g_{\lambda,m}|
\mathbf{1}_{\{0\lt f_{\lambda,m}\lt \delta\}}\,d\mu(\lambda)
\\
&\quad\le
\left(
\int_\Lambda\sum_m
p_t(m\mid\lambda)f_{\lambda,m}\,d\mu(\lambda)
\right)^{1/2}
\\
&\qquad\quad\times
\left(
\int_\Lambda\sum_m
p_t(m\mid\lambda)
\frac{|g_{\lambda,m}|^2}{f_{\lambda,m}}
\mathbf{1}_{\{0\lt f_{\lambda,m}\lt \delta\}}
\,d\mu(\lambda)
\right)^{1/2}
\\
&\quad\le \sqrt{q_t H_\delta}.
\end{aligned}
```

The quotient in the integral is used only where $`f_{\lambda,m}>0`$. In the last step it is at most one; moreover, the sum of the selected probabilities is at most $`\mathbf{1}_{A_\delta}(\lambda)`$.

For each fixed $`\lambda`$, there are only finitely many values $`f_{\lambda,m}`$. As $`\delta`$ decreases to zero, none of its positive values can remain in $`(0,\delta)`$. Hence $`\mathbf{1}_{A_\delta}(\lambda)\to0`$ pointwise. The indicators are bounded by one, so dominated convergence gives $`H_\delta\to0`$.

Combining the two parts, whenever $`q_t>0`$,

```math
\frac{|c_t|}{\sqrt{q_t}}
\le
\sqrt{\frac{q_t}{\delta}}+\sqrt{H_\delta}.
```

First take the limit superior as $`t\to0`$ for fixed $`\delta`$, then let $`\delta\downarrow0`$. This proves the claim. If $`q_t=0`$, positivity of $`E_t`$ also gives $`c_t=0`$, consistent with the stated convention. $`\square`$

The order of limits is important. There need not be a positive lower bound on the nonzero entries of all response effects across the shared-randomness space. The proof needs only a finite collection at each realization and an input-independent probability law.

## Structure at a pure output

**Lemma 2.** Suppose a qubit channel has a pure output. After input and output unitary basis changes, it has a pure preimage satisfying

```math
\mathcal N(|0\rangle\langle0|)=|0\rangle\langle0|.
```

In these bases there are a density matrix $`\sigma`$ and a complex number $`\gamma`$ such that

```math
\begin{aligned}
\mathcal N(|0\rangle\langle1|)
&=\gamma |0\rangle\langle1|,\\
\mathcal N(|1\rangle\langle0|)
&=\overline\gamma |1\rangle\langle0|,\\
\mathcal N(|1\rangle\langle1|)
&=\sigma,
\end{aligned}
```

with

```math
|\gamma|^2\le b,
\qquad
b=\langle1|\sigma|1\rangle.
```

Within this pure-output class, $`\mathcal N`$ is entanglement breaking if and only if $`\gamma=0`$.

**Proof.** A pure output always has a pure preimage. To see this, diagonalize any input that produces a pure state $`P`$:

```math
\rho=\sum_j r_j|\psi_j\rangle\langle\psi_j|,
\qquad
P=\sum_j r_j\mathcal N(|\psi_j\rangle\langle\psi_j|).
```

For each $`r_j>0`$, the expectation of $`I-P`$ in the corresponding output must vanish. Every such output is therefore supported on the one-dimensional range of $`P`$ and equals $`P`$. Choose one $`|\psi_j\rangle`$ and change bases. Input and output unitaries preserve the simulation task because Alice can transform her known description and Bob can transform the requested measurement.

Choose a finite Kraus representation. Since

```math
\sum_j K_j|0\rangle\langle0|K_j^\dagger
=
|0\rangle\langle0|,
```

each vector $`K_j|0\rangle`$ is parallel to $`|0\rangle`$. Write

```math
K_j=
\begin{pmatrix}
a_j & d_j\\
0 & e_j
\end{pmatrix}.
```

Trace preservation implies

```math
\sum_j|a_j|^2=1,
\qquad
\sum_j\overline a_jd_j=0.
```

Consequently,

```math
\begin{aligned}
\mathcal N(|0\rangle\langle1|)
&=
\left(\sum_j a_j\overline d_j\right)|0\rangle\langle0|
+
\left(\sum_j a_j\overline e_j\right)|0\rangle\langle1|\\
&=\gamma|0\rangle\langle1|.
\end{aligned}
```

Also $`b=\sum_j|e_j|^2`$, so Cauchy–Schwarz gives $`|\gamma|^2\le b`$.

When $`\gamma=0`$, linearity gives the explicit measure-and-prepare channel

```math
\mathcal N(\rho)
=
\langle0|\rho|0\rangle\,|0\rangle\langle0|
+
\langle1|\rho|1\rangle\,\sigma.
```

It is entanglement breaking.

Conversely, the normalized Choi state of an entanglement-breaking channel is separable, and its partial transpose must be positive. For the displayed normal form, the principal submatrix of that partial transpose on the span of $`|01\rangle`$ and $`|10\rangle`$ is

```math
\frac12
\begin{pmatrix}
0 & \overline\gamma\\
\gamma & \langle0|\sigma|0\rangle
\end{pmatrix}.
```

Its determinant is $`-|\gamma|^2/4`$. Positivity therefore requires $`\gamma=0`$. Only the elementary necessity of positive partial transpose for separability is used here, not a sufficiency criterion. $`\square`$

The lemma applies whether the initially supplied preimage is pure or mixed. A channel mapping a full-rank qubit input to a pure state is, in fact, a constant pure-state channel; the classification includes it in the entanglement-breaking branch.

## Necessity: a surviving tangent prevents finite simulation

Suppose the channel has a pure output and is not entanglement breaking. By Lemma 2, we may use the stated normal form with $`\gamma\ne0`$ and $`b>0`$.

For $`0\lt t\lt 1`$, let

```math
|\psi_t\rangle=\sqrt{1-t^2}|0\rangle+t|1\rangle.
```

The output has matrix entries

```math
\begin{aligned}
\langle1|\mathcal N(\psi_t)|1\rangle
&=bt^2,\\
\langle0|\mathcal N(\psi_t)|1\rangle
&=\gamma t\sqrt{1-t^2}
+t^2\langle0|\sigma|1\rangle.
\end{aligned}
```

Here $`\psi_t`$ abbreviates $`|\psi_t\rangle\langle\psi_t|`$. Thus

```math
\frac{
|\langle0|\mathcal N(\psi_t)|1\rangle|^2
}{
\langle1|\mathcal N(\psi_t)|1\rangle
}
\longrightarrow
\frac{|\gamma|^2}{b}>0.
```

Assume an exact one-way generic simulator with $`M\lt \infty`$ exists. Fix the binary Bell measurement from the model. Its effects satisfy

```math
E_t
=
\int_\Lambda\sum_{m=1}^M
p(m\mid\psi_t,\lambda)F_{\lambda,m}\,d\mu(\lambda)
=
\frac{\mathcal N(\psi_t)^{\mathsf T}}2.
```

The transpose preserves the lower diagonal entry and the absolute off-diagonal entry. Accordingly,

```math
q_t=\frac{bt^2}{2}\to0,
\qquad
\frac{|c_t|^2}{q_t}
\longrightarrow\frac{|\gamma|^2}{2b}>0.
```

This contradicts Lemma 1. No finite one-way alphabet can simulate the channel exactly, even under the weaker statistical criterion. The finite-interaction reduction described in the model then rules out every finite public communication tree.

This converse assumes no restriction on the decoder other than physical positivity of its effects. Shared randomness, local ancillas, contextual decoding, and a classical description of the requested Bell measurement do not remove the obstruction.

## Sufficiency: two finite constructions

### A channel image strictly inside the Bloch ball

Write the output states as

```math
\mathcal N(\rho)
=
\frac12\left(I+\boldsymbol r(\rho)\cdot\boldsymbol\sigma\right).
```

The state space is compact and $`\boldsymbol r(\rho)`$ depends continuously on $`\rho`$. If no output is pure, there is a number $`r_*\lt 1`$ such that

```math
\|\boldsymbol r(\rho)\|_2\le r_*
```

for every input.

Choose an angular radius $`\alpha>0`$ with $`\cos\alpha>r_*`$. Compactness of the unit sphere supplies finitely many unit vectors $`\boldsymbol v_1,\ldots,\boldsymbol v_M`$ such that every unit direction lies within angle $`\alpha`$ of one of them. Their convex hull $`P`$ has support function

```math
h_P(\boldsymbol n)
=
\max_j \boldsymbol n\cdot\boldsymbol v_j
\ge\cos\alpha>r_*
```

for every unit $`\boldsymbol n`$. By the separating-hyperplane characterization of convex containment, $`P`$ contains the ball of radius $`r_*`$ and therefore the full channel image.

Each $`\boldsymbol v_j`$ is the Bloch vector of a physical pure state $`\tau_j`$. For every known input, Alice chooses probabilities satisfying

```math
\mathcal N(\rho)=\sum_{j=1}^M w_j(\rho)\tau_j.
```

A measurable choice is available. Enumerate the finitely many affinely independent subsets of at most four vertices. By Carathéodory's theorem their simplices cover $`P`$. Choose the first simplex containing the target point, and use its unique barycentric coordinates. Membership sets are Borel and the coordinates are continuous on each simplex, giving Borel probabilities after this finite selection.

Alice samples $`j`$ with probability $`w_j(\rho)`$ and sends it. Bob prepares $`\tau_j`$ and performs the requested joint measurement on his actual side system. Averaging prepares exactly $`\mathcal N(\rho)`$, so the protocol preserves every conditional reference state. It requires no shared randomness.

### An entanglement-breaking channel

In finite dimensions an entanglement-breaking channel has a finite measure-and-prepare representation

```math
\mathcal N(\rho)
=
\sum_j \operatorname{Tr}(H_j\rho)\tau_j,
\qquad
H_j\ge0,
\qquad
\sum_jH_j=I.
```

This standard representation is established in [Horodecki, Shor, and Ruskai](https://arxiv.org/abs/quant-ph/0302031). Alice samples the finite label $`j`$ using her known input, sends it, and Bob prepares $`\tau_j`$. This is again exact for arbitrary side inputs and references.

For an entanglement-breaking channel with a pure output, Lemma 2 gives the more specific two-label construction directly. If both prepared states coincide, one label suffices.

Both constructions are one-way protocols and hence finite interactive protocols as well. Together with the converse, they complete the theorem. $`\square`$

## Examples and boundary cases

| Channel | Output geometry or normal form | Exact finite communication |
|---|---|---|
| Identity or any unitary qubit channel | Pure outputs with nonzero coherence tangent | Impossible |
| Depolarizing channel $`\rho\mapsto v\rho+(1-v)I/2`$, $`0\le v\lt 1`$ | Entire image lies strictly inside the sphere | Possible |
| Amplitude damping with survival $`0\lt \eta\lt 1`$ | Pure fixed point and $`\gamma=\sqrt\eta`$ | Impossible |
| Complete reset, $`\eta=0`$ | Constant output | Zero bits |
| Dephasing with residual coherence $`0\lt \kappa\le1`$ | Pure basis outputs and $`\gamma=\kappa`$ | Impossible |
| Complete dephasing, $`\kappa=0`$ | Basis measurement and preparation | One bit suffices |

For the dephasing rows, the channel sends the off-diagonal entry $`\rho_{01}`$ to $`\kappa\rho_{01}`$ and leaves the diagonal entries unchanged. The table concerns exact worst-case communication; it makes no quantitative approximate-cost claim for dephasing.

A full-rank output admixture always makes finite exact simulation possible. If $`\tau`$ is a full-rank state and $`0\lt \delta\le1`$, then

```math
\mathcal N_\delta(\rho)
=
(1-\delta)\mathcal N(\rho)+\delta\tau
\ge\delta\tau
```

has only strictly mixed outputs. The required finite alphabet can diverge as $`\delta`$ decreases to zero. The amplitude-damping accuracy law quantifies one such singular limit without equating exact feasibility with a practical constant-cost implementation.

## Scope of the conclusion

The theorem identifies the boundary for exact classical communication in the specified known-input experiment. It does not classify quantum capacity or classical computation time. Its positive branch includes channels that are not entanglement breaking because the encoder is allowed to use a complete classical description of the input.

The impossibility is a worst-case finite-alphabet statement and extends qualitatively to finite public interaction trees. It does not settle finite expected communication with unbounded message sets or unbounded stopping times. The matching amplitude-damping approximation result uses the separate one-way resource definition in the model.
