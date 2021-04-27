---
title: Numerical relativity simulations of binary black hole mergers
summary: Numerical solutions of Einstein's equations are the only way to describe the merger accurately.
tags:
- Numerical Relativity
- Numerical Simulations
- Einstein's Equations
- General Relativity
date: "2015-10-11"
math: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Real part of GW strain for numerical relativity simulations performed with BAM.
  focal_point: smart
  preview_only: false

<!-- links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/ -->
url_code: ""
url_pdf: "https://journals.aps.org/prd/pdf/10.1103/PhysRevD.93.044006"
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

To elucidate the properties of merging black hole binaries from their emitted gravitational waves as recorded by GW detectors such as LIGO, Virgo and KAGRA, it is crucial to have at our disposal a set of very accurate waveforms. The gold standard for accurate waveforms are numerical relativity (NR) simulations of **Einstein's equations**

$$
G\_{ab} = 8\pi T\_{ab},
$$

where $G\_{ab}$ is the Einstein tensor formed from the **metric** (which measures distances in space time) and its first and second derivatives, and $T\_{ab}$ is stress energy tensor of matter. For binary black holes we can set $T\_{ab} = 0$ and consider vacuum solutions.

[NR simulations](https://www.cambridge.org/core/books/numerical-relativity/72D4F6D791BC6F8F9CF87A60FC354D6A) are the only way of accurately describing the highly non-linear merger part of the waves where the orbital velocity $v$ reaches a sizable fraction of the speed of light $c$. In contrast, the waves from the low frequency inspiral, where $v \ll c$,  can be well approximated by post-Newtonian theory.

However, NR simulations are not perfectly accurate, they just approximate Einstein on a numerical grid of finite size. To estimate the error in numerical simulations it is customary to perform simulations with grids of different fineness. The numerical solution typically depends on a power of the gridsize $\Delta$, so that the error goes like $\Delta^p$, and the error decreases when $\Delta$ is made smaller [^1]. One typically checks convergence of the numerical code, i.e. that for a numerical algorithm which is, say 4th order accurate ($p=4$) the error really decreases as $\Delta^4$.

I have used simulation codes for binary black holes using finite difference ([BAM](https://arxiv.org/pdf/gr-qc/0610128.pdf)) or pseudo-spectral ([SpEC](https://www.black-holes.org)) grids.



Below I show the **orbital motion** of the three highest resolutions for a binary black hole merger with mass-ratio 1:18 [Husa et al, PRD 93, 044006 (2016)](https://journals.aps.org/prd/pdf/10.1103/PhysRevD.93.044006).

 {{< figure src="orbit.png" id="orbit" >}}


Even though NR simulations have some error, this error is much smaller than in **waveform models**. We can see this in the figure below where different waveform models are compared against NR
[Ossokine et al, PRD 102, 044055 (2020)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.044055)

 {{< figure src="NR-vs-models.png" id="NR-vs-models" >}}


Binary black holes may have some initial eccentricity in their orbit, but by the time they enter the LIGO band they typically follow a non-eccentric quasi-circular inspiral. NR simulations can only be done for short waveform lengths and therefore it is important to set the black holes' momenta so that they follow a non-eccentric inspiral and merger. To find good initial parameters for quasi-circular evolution I designed an iterative method [Pürrer, et al, PRD 85, 124051 (2012)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.85.124051). The figure below shows the residual eccentricity in the phase of the gravitational wave for a set of simulations with different starting parameters.

 {{< figure src="eccentricity-reduction-phase.png" id="eccentricity-reduction-phase" >}}


[^1]: This is an oversimplification. Accurate binary black hole NR simulations require more than a single uniform grid size and there are other types of errors beyond this truncation error that come into play in extracting the waves.
