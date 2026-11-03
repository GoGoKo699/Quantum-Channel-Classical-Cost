# A finite preparation protocol for amplitude damping

This section proves the one-way upper bound. The protocol uses a finite menu of pure states and requires no shared randomness. Its message alphabet works for every known input state and every requested joint measurement with Bob's unknown quantum side input.

## Statement and error convention

Let $`\mathcal A_\eta`$ be the qubit amplitude-damping channel with fixed survival parameter $`0\lt \eta\lt 1`$,

```math
K_0=|0\rangle\langle0|+\sqrt\eta\,|1\rangle\langle1|,
\qquad
K_1=\sqrt{1-\eta}\,|0\rangle\langle1|.
```

Alice receives a classical description of a qubit state $`\rho`$. Bob holds an arbitrary unknown state $`\sigma_{BR}`$, where $`R`$ is an untouched reference, and must reproduce a requested measurement on $`A B`$ when the target state is

```math
\mathcal A_\eta(\rho)_A\otimes\sigma_{BR}.
```

The error is the total variation distance between measurement-outcome distributions. The construction below satisfies the stronger requirement that the joint output record and reference have trace distance at most $`\varepsilon`$.

**Theorem.** There is a universal constant $`C`$ such that, for every $`0\lt \eta\lt 1`$ and $`0\lt \varepsilon\le1/4`$, a one-way protocol with a finite global message alphabet of size

```math
M\le \frac{C}{1-\eta}\,\varepsilon^{-1/2}
```

achieves the stated error uniformly over Alice's known mixed or pure input, Bob's side-input dimension and state, and the requested joint measurement. In particular, for each fixed $`\eta\in(0,1)`$,

```math
M_\eta(\varepsilon)=O_\eta(\varepsilon^{-1/2}),
\qquad
\lceil\log_2 M\rceil
\le \tfrac12\log_2(1/\varepsilon)+O_\eta(1).
```

The displayed dependence on $`\eta`$ is a convenient upper bound and is not claimed to be optimal. The theorem charges the message alphabet. It does not assert computational efficiency of finding a decomposition, or bound arithmetic precision, local state-preparation cost, or the description length of the fixed protocol.

## 1. The output ellipsoid and its sphere contact

Use the Bloch convention $`\rho=(I+\boldsymbol r\cdot\boldsymbol\sigma)/2`$, with $`|0\rangle`$ at the north pole. The complete set of channel outputs, including mixed inputs, has Bloch vectors in

```math
\mathcal E_\eta
=\left\{
\begin{pmatrix}0\\0\\1-\eta\end{pmatrix}
+\mathrm{diag}(\sqrt\eta,\sqrt\eta,\eta)\boldsymbol r:
\|\boldsymbol r\|_2\le1
\right\}.
```

For a unit normal $`\boldsymbol n`$, let $`\theta\in[0,\pi]`$ be its polar angle. The support function of the ellipsoid is

**Equation (1).**

```math
h_\eta(\theta)
=(1-\eta)\cos\theta
+\sqrt{\eta\sin^2\theta+\eta^2\cos^2\theta}.
```

Write $`a=1-\eta`$. Rationalization gives the exact identity

**Equation (2).**

```math
1-h_\eta(\theta)
=\frac{a(1-\cos\theta)^2}
{1-a\cos\theta+
\sqrt{\eta\sin^2\theta+\eta^2\cos^2\theta}}.
```

The denominator is strictly positive: its first term is at least $`\eta>0`$. It is at most $`3`$, since $`1-a\cos\theta\le2`$ and the square root is at most $`1`$. For $`0\le\theta\le1`$, the elementary bound $`1-\cos\theta\ge\theta^2/4`$ yields

```math
1-h_\eta(\theta)\ge \frac{a\theta^4}{48}.
```

For $`1\le\theta\le\pi`$, monotonicity of $`1-\cos\theta`$ and the same bound at $`\theta=1`$ give $`1-h_\eta(\theta)\ge a/48`$. Therefore

**Equation (3).**

```math
1-h_\eta(\theta)
\ge \frac{a}{48}\min\{\theta^4,1\}.
```

In particular, the output ellipsoid touches the Bloch sphere only at the north pole. Its contact is quartic in the polar normal:

**Equation (4).**

```math
1-h_\eta(\theta)
=\frac{1-\eta}{8\eta}\theta^4+O_\eta(\theta^6)
\quad(\theta\to0).
```

The construction uses the global inequality (3), so its validity does not depend on truncating this expansion.

## 2. Regularization buys a uniform support margin

Put $`\delta=2\varepsilon\le1/2`$ and define the regularized output

**Equation (5).**

```math
\widetilde\rho
=(1-\delta)\mathcal A_\eta(\rho)+\delta I/2.
```

Its Bloch-vector set is the contracted ellipsoid
$`\mathcal K=(1-\delta)\mathcal E_\eta`$. Thus

**Equation (6).**

```math
\begin{aligned}
1-h_{\mathcal K}(\theta)
&=1-(1-\delta)h_\eta(\theta)\\
&=\delta+(1-\delta)(1-h_\eta(\theta))\\
&\ge \delta+\frac{a}{96}\min\{\theta^4,1\}.
\end{aligned}
```

We will construct unit Bloch vectors $`V`$ whose convex hull contains $`\mathcal K`$. The relevant mesh scale is $`\sqrt\delta`$ near the pole and $`\theta^2`$ farther away.

## 3. A finite spherical net with the required mesh

Distances in this section are geodesic angles on the unit sphere. Set

**Equation (7).**

```math
R_0=\delta^{1/4},
\qquad
s=\frac{\sqrt a}{16}.
```

In particular, $`R_0\lt 1`$ and $`0\lt s\lt 1/16`$. Build finite nets on the following closed regions:

1. On the polar cap $`0\le\theta\le R_0`$, use covering radius $`r_0=sR_0^2=s\sqrt\delta`$.
2. For each $`R_j=2^jR_0\lt 1`$, cover the annulus $`R_j\le\theta\le\min\{2R_j,1\}`$ with radius $`r_j=sR_j^2`$.
3. Cover $`1\le\theta\le\pi`$ with radius $`r_\infty=s`$.

The union of all these net points is $`V`$. The regions cover the whole sphere; overlapping boundaries cause no problem.

### Existence and cardinality

For a closed spherical region and a positive radius $`r`$, take a maximal set of points whose pairwise distances exceed $`r`$. Compactness ensures a finite such set, and maximality ensures that its radius-$`r`$ balls cover the region. Its radius-$`r/2`$ balls have disjoint interiors.

For completeness, the required area estimate is uniform in the annulus radius. A radius-$`x`$ spherical cap has area $`2\pi(1-\cos x)`$. For $`0\le x\le\pi`$,

**Equation (8).**

```math
2\pi(1-\cos x)\le \pi x^2,
\qquad
2\pi(1-\cos x)\ge \frac{4x^2}{\pi}.
```

A radius-$`r_j/2`$ ball centered in the $`j`$-th annulus lies inside the polar cap of radius $`2R_j+r_j/2`$. Since $`r_j=sR_j^2\le R_j/16`$, that containing cap has area at most a universal constant times $`R_j^2`$. Each disjoint small ball has area at least $`r_j^2/\pi`$. Hence, with a universal constant $`C_0`$, the annular net requires at most

**Equation (9).**

```math
\frac{C_0R_j^2}{r_j^2}
=\frac{C_0}{s^2R_j^2}
```

points. The same argument for the inner cap gives at most $`C_0/(s^2R_0^2)`$ points. A packing in the entire sphere bounds the outer net by $`C_0/s^2`$ points, after increasing $`C_0`$ if necessary.

There are finitely many dyadic annuli, and

```math
\sum_{j:\,R_j\lt 1}\frac{1}{R_j^2}
\le \frac{1}{R_0^2}\sum_{j=0}^{\infty}4^{-j}
=\frac{4}{3R_0^2}.
```

Because $`R_0\le1`$, the total number of vertices satisfies

**Equation (10).**

```math
|V|
\le \frac{C_1}{s^2R_0^2}
\le \frac{C_2}{1-\eta}\,\delta^{-1/2},
```

for universal constants $`C_1,C_2`$. This establishes a finite global alphabet; it is not a separate alphabet chosen after seeing the input.

## 4. The net's convex hull contains every regularized output

Fix any unit normal $`\boldsymbol n`$, at polar angle $`\theta`$, and choose a net vertex $`\boldsymbol v`$ supplied by the region containing $`\boldsymbol n`$. If their angular distance is $`d`$, then

**Equation (11).**

```math
1-\boldsymbol n\cdot\boldsymbol v
=1-\cos d\le d^2/2.
```

In the inner cap, $`d\le s\sqrt\delta`$, so the right side is at most $`a\delta/512\le\delta`$. In an annulus with inner radius $`R_j`$, it is at most

```math
\frac{s^2R_j^4}{2}
=\frac{aR_j^4}{512}
\le\frac{a\theta^4}{96}.
```

In the outer region it is at most $`s^2/2=a/512\le a/96`$. Comparing each case with (6) gives

```math
\boldsymbol n\cdot\boldsymbol v
\ge h_{\mathcal K}(\boldsymbol n).
```

Therefore the polytope $`P=\mathrm{conv}(V)`$ obeys

**Equation (12).**

```math
h_P(\boldsymbol n)
\ge h_{\mathcal K}(\boldsymbol n)
\qquad\text{for every unit }\boldsymbol n.
```

The support-function characterization of compact convex sets implies
$`\mathcal K\subseteq P`$. Equivalently, if a point of $`\mathcal K`$ lay outside $`P`$, a separating hyperplane would contradict (12). Every vertex of $`P`$ lies on the Bloch sphere, and $`P`$ lies inside the Bloch ball. It is therefore a polytope of physical qubit states containing the entire regularized output family.

## 5. The communication protocol

Associate to each $`\boldsymbol v_k\in V`$ the fixed pure state
$`\tau_k=(I+\boldsymbol v_k\cdot\boldsymbol\sigma)/2`$. Alice computes her regularized output (5). Containment gives a convex decomposition

**Equation (13).**

```math
\widetilde\rho=\sum_{k=1}^{M}p_k(\rho)\tau_k,
\qquad p_k(\rho)\ge0,
\quad\sum_kp_k(\rho)=1.
```

A measurable choice of the probabilities can be fixed once for the protocol. For example, triangulate the finite polytope using its vertices, order the resulting simplices, and assign each point to the first simplex containing it. Barycentric coordinates on that simplex give the probabilities; a fixed tie rule handles shared faces. The output ellipsoid has nonempty interior for $`\eta>0`$, so the containing polytope is three-dimensional. Degenerate boundary faces are handled by their lower-dimensional simplices.

Alice samples $`k`$ from (13) using private randomness and sends that label. Bob prepares $`\tau_k`$, then performs the requested joint measurement using his actual side input. Averaging over the label produces exactly $`\widetilde\rho`$. Neither the menu nor Alice's message rule needs the requested measurement or knowledge of Bob's state.

An individual output can be decomposed using at most four vertices, by the three-dimensional Carathéodory theorem. This does not reduce the charged alphabet to four: different inputs can require different vertices, and the global set of possible labels has size $`M=|V|`$, bounded in (10).

## 6. Uniform error, mixed inputs, and side references

For any input $`\rho`$, let $`\omega=\mathcal A_\eta(\rho)`$. Equation (5) gives

**Equation (14).**

```math
\frac12\|\widetilde\rho-\omega\|_1
=\delta\,\frac12\|I/2-\omega\|_1
\le\frac\delta2=\varepsilon.
```

The inequality holds for every qubit state; no purity assumption is used. For an arbitrary unknown side-reference state $`\sigma_{BR}`$,

**Equation (15).**

```math
\frac12\| (\widetilde\rho-\omega)_A\otimes\sigma_{BR}\|_1
=\frac12\|\widetilde\rho-\omega\|_1
\le\varepsilon.
```

Trace distance contracts under every quantum channel. Applying Bob's requested measurement or instrument on $`A B`$, while leaving $`R`$ untouched, therefore preserves the bound. This controls both total variation distance of the outcome record and trace distance of that record jointly with $`R`$. It also covers an ensemble in which Alice's classical input label is correlated with the side-reference state, by applying the uniform conditional bound and convexity.

The reference statement concerns the unknown side input and its reference. Alice's channel input is supplied as a classical description; this theorem does not simulate the action of $`\mathcal A_\eta`$ on an unknown input entangled with an inaccessible reference.

Substituting $`\delta=2\varepsilon`$ into (10) proves the theorem.

## 7. Endpoints and parameter dependence

At $`\eta=0`$, the channel always outputs $`|0\rangle\langle0|`$. Bob prepares that state with no message, so the alphabet has one element and the communication cost is zero.

At $`\eta=1`$, the channel is the identity and its output set is the entire Bloch ball. The quartic-contact estimate is unavailable because $`1-h_1`$ vanishes in every direction. A uniform spherical net of angular covering radius $`\sqrt\delta`$ has $`O(\delta^{-1})`$ vertices and support at least $`1-\delta/2`$, so it contains the ball of radius $`1-\delta`$. The same preparation protocol consequently gives $`M=O(\varepsilon^{-1})`$. The whole-sphere argument in the [lower-bound endpoint analysis](amplitude_lower.md) gives the matching lower bound.

For every fixed $`0\lt \eta\lt 1`$, the upper exponent is $`1/2`$. The displayed construction is not uniform near $`\eta=1`$; its prefactor diverges as the damped ellipsoid approaches the entire sphere. The endpoint $`\eta=0`$ likewise has a simpler exact protocol than the general construction. No optimal joint asymptotic law in $`(\eta,\varepsilon)`$ is asserted.

The communication cost counts a finite worst-case one-way alphabet. Shared randomness is unnecessary for this upper bound, and the proof makes no claim about expected communication or the optimal cost of interactive protocols.

## Reading route

The [matching lower bound](amplitude_lower.md) permits all physical decoders and unlimited shared randomness. The [geometry and examples](geometry_and_examples.md) explain the resulting cost law and its limiting regimes.
