# A sharp one-way lower bound for generic simulation of amplitude damping

The lower bound permits arbitrary continuous shared randomness and arbitrary physical decoders. Its proof needs one fixed Bell measurement and an unknown side qubit. The complete task and the two accuracy criteria are defined in the [operational model](model.md).

## 1. Task and error convention

For a survival probability $`0\leq\eta\leq1`$, the amplitude-damping channel is

```math
\mathcal A_\eta
\begin{pmatrix}a&c\\c^*&b\end{pmatrix}
=
\begin{pmatrix}a+(1-\eta)b&\sqrt\eta\,c\\
\sqrt\eta\,c^*&\eta b\end{pmatrix}.
```

Alice receives a classical description of an arbitrary qubit state $`\rho`$. Bob receives an unknown quantum state $`\tau_B`$ and a description of a joint POVM on the intended channel output and $`B`$. Alice and Bob have arbitrary input-independent shared randomness, but no shared entanglement or quantum communication. Alice sends one message from an alphabet of at most $`M`$ labels. Bob may apply any physical quantum instrument to his input, with arbitrary local ancillas and private randomness. Its dependence on the message, shared randomness, and requested POVM is unrestricted.

For every input $`\rho`$, every allowed Bob state, and every requested POVM, the simulator must approximate the ideal outcome distribution within total variation distance $`\varepsilon`$, with

```math
\mathrm{TV}(P,Q)=\frac12\sum_k|P(k)-Q(k)|.
```

The theorem below needs only the restricted subtask in which $`B`$ is one uncorrelated unknown qubit and the requested measurement is the fixed binary Bell-projector POVM

```math
\bigl\{\Phi^+, I-\Phi^+\bigr\},\qquad
\Phi^+=|\Phi^+\rangle\langle\Phi^+|,\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

Consequently the bound also applies when Bob may hold an arbitrarily large or externally reference-correlated input. It does not require the simulator to prepare a channel-output state, impose measurement noncontextuality, or approximate a full quantum instrument. It is a lower bound on a single-round, worst-case message alphabet; finite expected communication and the bit cost of interactive protocols are different resources.

## 2. Statement with explicit constants

**Theorem.** Let $`0\lt \eta\lt 1`$ and $`0\lt \varepsilon\leq1/64`$. Any simulator for the restricted subtask above uses an alphabet satisfying

**Equation (1).**

```math
M\ \geq\ \frac{\eta}{256\varepsilon}
\min\left\{\frac14,
\sqrt{\frac{\varepsilon}{\eta(1-\eta)}}\right\}.
```

In particular, for each fixed $`0\lt \eta\lt 1`$, whenever

```math
0\lt \varepsilon\leq
\min\left\{\frac1{64},\frac{\eta(1-\eta)}{16}\right\},
```

we have

**Equation (2).**

```math
M\ \geq\ \frac1{256}
\sqrt{\frac{\eta}{1-\eta}}\,\varepsilon^{-1/2}.
```

Thus $`M_\eta(\varepsilon)=\Omega_\eta(\varepsilon^{-1/2})`$, and the worst-case one-way bit cost obeys

**Equation (3).**

```math
C_\eta(\varepsilon)\geq
\frac12\log_2\frac1\varepsilon-O_\eta(1).
```

The constants in (1)–(2) are deliberately conservative. Equation (1) is a valid uniform lower estimate, not a claim of a matched two-parameter crossover law. The endpoints are treated separately in Section 7.

## 3. Every physical decoder induces a finite random menu of effects

Let $`(\Omega,\mathcal F,\mu)`$ be any probability space for the shared random variable $`\lambda`$. No finite-support, entropy, or density assumption is made about $`\mu`$. For the fixed binary measurement, Bob's probability of declaring the Bell outcome, conditional on $`(m,\lambda)`$, is

```math
\mathrm{Tr}[F_m(\lambda)\tau],
\qquad 0\leq F_m(\lambda)\leq I_2.
```

This follows from the Born rule for a physical binary instrument, after absorbing any local ancillas and private randomness into its effect. For Alice's input $`\rho`$, let $`p(m\mid\rho,\lambda)`$ be the message distribution. The resulting effect on Bob's qubit is

**Equation (4).**

```math
E_\rho=
\int_\Omega\sum_{m=1}^{M}
p(m\mid\rho,\lambda)F_m(\lambda)\,d\mu(\lambda).
```

The ideal effect is

**Equation (5).**

```math
T_\rho=\frac12\mathcal A_\eta(\rho)^T,
```

because

```math
\mathrm{Tr}\bigl[\Phi^+(\mathcal A_\eta(\rho)\otimes\tau)\bigr]
=\frac12\mathrm{Tr}[\mathcal A_\eta(\rho)^T\tau].
```

For binary distributions, total variation equals the absolute difference in one outcome probability. Uniform accuracy for every unknown $`\tau`$ therefore gives

**Equation (6).**

```math
\|E_\rho-T_\rho\|_\infty\leq\varepsilon.
```

In particular,

**Equation (7).**

```math
\mathrm{Tr}\,E_\rho\geq\frac12-2\varepsilon.
```

The factor two in (7) is the dimension of Bob's qubit. Alice may know the requested Bell measurement: the proof gives her that knowledge and still obtains the lower bound.

## 4. An explicit input disk covers a cap of output eigenvectors

Use pure inputs

**Equation (8).**

```math
|\psi_{p,\phi}\rangle
=\sqrt{1-p}\,|0\rangle+e^{i\phi}\sqrt p\,|1\rangle,
\qquad 0\leq p\leq p_*,\quad 0\leq\phi\lt 2\pi,
```

where

**Equation (9).**

```math
p_*:=\min\left\{\frac14,
\sqrt{\frac{\varepsilon}{\eta(1-\eta)}}\right\}.
```

This is a disk in the natural complex amplitude $`z=\sqrt{p/(1-p)}e^{i\phi}`$, with radius $`\sqrt{p_*/(1-p_*)}`$. The parameter $`p`$ is the excited-state population, not that stereographic radius squared.

The output is

**Equation (10).**

```math
\rho_{p,\phi}:=\mathcal A_\eta(\psi_{p,\phi})
=
\begin{pmatrix}
1-\eta p&\sqrt{\eta p(1-p)}e^{-i\phi}\\
\sqrt{\eta p(1-p)}e^{i\phi}&\eta p
\end{pmatrix}.
```

Its Bloch-vector length and eigenvalues are

**Equation (11).**

```math
R(p)=\sqrt{1-4\eta(1-\eta)p^2},\qquad
\lambda_\pm(p)=\frac{1\pm R(p)}2.
```

For $`0\leq p\leq1/4`$, $`R(p)\geq\sqrt{15/16}>0`$, so the dominant eigenvector is unique. Let $`u_{p,\phi}`$ denote the dominant eigenvector of $`\rho_{p,\phi}^T`$. Its Bloch polar angle $`\beta(p)`$ is determined by

**Equation (12).**

```math
\cos\beta(p)=\frac{1-2\eta p}{R(p)}.
```

Transposition changes the azimuth from $`\phi`$ to $`-\phi`$, which preserves spherical area. Define $`q(p)=1-\cos\beta(p)`$. Direct differentiation gives

**Equation (13).**

```math
q'(p)=
\frac{2\eta[1-2(1-\eta)p]}{R(p)^3}
\geq\eta>0
\qquad (0\leq p\leq1/4).
```

The inequality uses $`1-2(1-\eta)p\geq1/2`$ and $`R(p)\leq1`$. Thus the output dominant eigenvectors cover exactly the full cap

```math
\mathcal C_*:=\{u:0\leq\beta(u)\leq\beta(p_*)\}.
```

Their spherical-area Jacobian is explicit:

**Equation (14).**

```math
dA=\sin\beta\,d\beta\,d\phi=q'(p)\,dp\,d\phi.
```

In particular, this cap has area

**Equation (15).**

```math
A_*:=\mathrm{area}(\mathcal C_*)
=2\pi q(p_*)\geq2\pi\eta p_*.
```

Except for the north pole, the cap parametrization is one-to-one after fixing the usual azimuth convention; the pole has zero spherical area. Uniform area integration over $`\mathcal C_*`$ is consequently a legitimate average over the input family (8), with density proportional to $`q'(p)`$.

The ideal Bell effect $`T_{p,\phi}=\rho_{p,\phi}^T/2`$ has leakage in the orthogonal eigenvector bounded by

**Equation (16).**

```math
\begin{aligned}
\langle u_{p,\phi}^\perp|T_{p,\phi}|u_{p,\phi}^\perp\rangle
&=\frac{1-R(p)}4\\
&=\frac{\eta(1-\eta)p^2}{1+R(p)}\\
&\leq\eta(1-\eta)p_*^2\leq\varepsilon.
\end{aligned}
```

Together with (6), this yields, for every cap direction $`u`$ and its associated input,

**Equation (17).**

```math
L(u):=\langle u^\perp|E_u|u^\perp\rangle\leq2\varepsilon.
```

Here $`E_u`$ abbreviates the simulated effect for that particular input; it need not vary continuously with $`u`$.

## 5. Accurate effects require a constant weight of nearby response states

For every nonzero decoder effect write

```math
F_m(\lambda)=t_m(\lambda)\sigma_m(\lambda),\qquad
t_m=\mathrm{Tr}\,F_m\in(0,2],
```

where $`\sigma_m`$ is a density matrix. Set $`t_m=0`$ for a zero effect and choose its normalized state arbitrarily. Introduce the nonnegative trace weights

```math
w_m(u,\lambda)
=p(m\mid\rho_u,\lambda)t_m(\lambda).
```

Their total integrated mass is $`\mathrm{Tr}\,E_u`$. Set

**Equation (18).**

```math
\delta:=16\varepsilon\leq\frac14.
```

Call a response state good at $`u`$ if

```math
\langle u|\sigma_m(\lambda)|u\rangle\geq1-\delta.
```

For a bad response, its leakage into $`u^\perp`$ is greater than $`\delta`$. Therefore the integrated trace weight of all bad responses is at most $`L(u)/\delta\leq1/8`$. The total good trace weight

**Equation (19).**

```math
G(u):=\int_\Omega\sum_m
w_m(u,\lambda)
\mathbf{1}\{\langle u|\sigma_m(\lambda)|u\rangle\geq1-\delta\}
\,d\mu(\lambda)
```

satisfies

**Equation (20).**

```math
G(u)\geq\frac12-2\varepsilon-\frac18
\geq\frac{11}{32}>\frac14.
```

The weaker bound $`G(u)\geq1/4`$ is sufficient. This step accounts for the fact that decoder effects need not have unit trace and need not themselves be output states.

## 6. Cap-area counting is unchanged by arbitrary shared randomness

**Area lemma.** For any qubit state $`\sigma`$ and $`0\lt \delta\lt 1/2`$, the set

```math
S_{\sigma,\delta}
=\{u:\langle u|\sigma|u\rangle\geq1-\delta\}
```

has Bloch-sphere area at most $`4\pi\delta`$.

To prove it, write $`\sigma=(I+\mathbf s\cdot\boldsymbol\sigma)/2`$, with $`|\mathbf s|\leq1`$. The condition is $`\mathbf s\cdot\mathbf n_u\geq1-2\delta`$. If $`|\mathbf s|\lt 1-2\delta`$, the set is empty. Otherwise it is a cap of area

**Equation (21).**

```math
2\pi\left(1-\frac{1-2\delta}{|\mathbf s|}\right)
\leq4\pi\delta.
```

Now average (19) uniformly over $`\mathcal C_*`$. Since all integrands are nonnegative, Tonelli's theorem permits exchanging cap integration, the finite sum, and the shared-randomness integral. For each fixed $`\lambda`$, use $`p(m\mid\rho_u,\lambda)\leq1`$, $`t_m\leq2`$, and the area lemma to obtain

**Equation (22).**

```math
\begin{aligned}
\frac1{A_*}\int_{\mathcal C_*}G(u)\,dA(u)
&\leq
\int_\Omega\frac1{A_*}\sum_{m=1}^M
t_m(\lambda)
\mathrm{area}(S_{\sigma_m(\lambda),\delta}\cap\mathcal C_*)
\,d\mu(\lambda)\\
&\leq\frac{8\pi M\delta}{A_*}.
\end{aligned}
```

But (20) bounds the left side below by $`1/4`$. Hence

```math
M\geq\frac{A_*}{32\pi\delta}
\geq\frac{2\pi\eta p_*}{32\pi(16\varepsilon)}
=\frac{\eta p_*}{256\varepsilon},
```

which proves (1) and therefore (2)–(3).

The argument imposes no restriction on the probability space of shared randomness. A randomly chosen codebook still has at most $`M`$ response effects for each shared seed; averaging cannot increase the total area those $`M`$ effects cover at the required fidelity.

### Measurability convention

Physical randomized protocols are modeled by measurable stochastic kernels. In particular, Alice's message probabilities are jointly measurable in her classical input and the shared seed, and Bob's effects are measurable in that seed. The functions in (4) and (19) are then jointly measurable, which justifies Tonelli's theorem. No differentiability or continuity of the simulator, finite support of the shared random variable, or density with respect to a preferred measure is required.

## 7. Endpoint audit and scope

### Complete reset: $`\eta=0`$

The channel always produces $`|0\rangle\langle0|`$. Bob can prepare this state locally without receiving input information, so $`M=1`$ and zero bits suffice exactly. The cap Jacobian (13) vanishes and the lower-bound construction correctly yields no positive obstruction. The fixed-channel constant in (2) is not asserted uniformly as $`\eta\downarrow0`$.

### Identity: $`\eta=1`$

The output is pure for every input. Use the whole Bloch sphere, of area $`4\pi`$, instead of a shrinking cap. The ideal Bell effect has zero orthogonal leakage; (6) gives $`L(u)\leq\varepsilon`$. With $`\delta=8\varepsilon`$ and $`\varepsilon\leq1/64`$, the same trace-weight argument has $`G(u)\geq1/4`$. Equation (22) gives

**Equation (23).**

```math
M\geq\frac{4\pi}{32\pi(8\varepsilon)}
=\frac1{64\varepsilon}.
```

Thus the unitary endpoint has the stronger $`\Omega(\varepsilon^{-1})`$ alphabet requirement. Input/output unitary conjugations do not change the communication task or these bounds. The divergence of the coefficient in (2) as $`\eta\uparrow1`$ reflects a nonuniform limit and is controlled by the saturation in (1); it is not an inconsistency.

### What has and has not been proved

The lower bound is rigorous under the stated measurable-protocol model. It is already witnessed by one fixed two-outcome entangled POVM and a single unknown qubit at Bob. It survives continuous shared randomness, arbitrary private randomness, local quantum ancillas, and contextual response to the requested measurement. It does not use a uniform distribution over Alice's unknown state as a promise; the averaging distribution is a proof device because the protocol must work for every input.

This file supplies the lower bound only. The [upper construction](amplitude_upper.md) supplies the matching finite preparation protocol. The quantitative result here must not be transferred to interactive bit complexity through the finite contingent-strategy reduction, whose communication blowup is not controlled by this argument.

## Attribution

The generic simulation task and exact identity obstruction originate in [Naik et al.](../references/RELATED_WORK.md#naik2026). The cap-area argument here gives the finite-error lower bound for amplitude damping. The [related-work account](../references/RELATED_WORK.md) distinguishes this task from ordinary prepare-and-measure simulation, channel programming, and entanglement-assisted asymptotic simulation.
