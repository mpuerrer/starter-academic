---
title: Surrogate models of gravitational waves
summary: Accelerating semi-analytic models of gravitational waves.
tags:
- Surrogate model
- Gravitational waves
- Data Analysis
date: "2018-10-30"
math: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Surrogate model of effective-one-body model for gravitational waves from black hole binaries.
  focal_point: smart
  preview_only: false

<!-- links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/ -->
url_code: "https://github.com/mpuerrer/TPI"
url_pdf: "https://iopscience.iop.org/article/10.1088/0264-9381/31/19/195010"
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---


# Motivation

Models of gravitational waves (GW) $h(\vec\lambda)$ are crucial for measuring the properties of merging black hole binaries from LIGO data. These properties can be described by the posterior distribution $p(\vec\lambda| d)$ which is computed in **Bayesian inference** using methods such as Markov-chain Monte Carlo or nested sampling. Models are also needed to build template banks of GWs for detection pipelines. These applications require tens of millions or more model evaluations and therefore it is critical that models be **computationally efficient** and also accurate. This motivates building surrogate models which greatly accelerate the original model while preserving accuracy.

# Impact

My surrogate models have been a cornerstone to provide timely analyses for detection and Bayesian inference of LIGO-Virgo data and have been used in **dozens of LVC Collaboration papers**.

{{< cite page="/publication/2014-cq-gra-31-s-5010-p" view="4" >}}
{{< cite page="/publication/2016-ph-rv-d-93-f-4041-p" view="4" >}}
{{< cite page="/publication/2017-ph-rv-d-95-d-4028-b" view="4" >}}
{{< cite page="/publication/2017-ph-rv-d-96-l-3011-d" view="4" >}}
{{< cite page="/publication/2016-ph-rv-d-94-d-4031-s" view="4" >}}
{{< cite page="/publication/2019-ph-rv-d-100-b-4002-l" view="4" >}}
{{< cite page="/publication/2020-ph-rv-d-101-l-4040-c" view="4" >}}

# Techniques

I have used the following techniques to build several surrogate models:
  * **Decomposition of the complex waveform $h$ into simpler data pieces**, such as amplitude $|h|$ and unwrapped phase $\arg [h]$.
  * Representing waveform data pieces on **sparse grids** (to achieve a set spline interpolation error)
  * Expansion of data pieces in **orthonormal bases** $V$ with **singular value decomposition** (SVD) $\mathcal{T} = V \Sigma U^T$, where the matrix $\mathcal{T} = \left[\tau_1 | \dots |\tau_n\right] \in \mathbb{R}^{m \times n}$ contains training set waveforms in its columns.
  * **Tensor product spline interpolation** of expansion coefficients $\mathcal{M} = V^T \mathcal{T}$. See github for my Cython [TPI](https://github.com/mpuerrer/TPI) package.
  * To better deal with high dimensional spaces, support scattered data, and provide uncertainty estimates I have used **Gaussian process regression**.

# Surrogate model

A surrogate model for GWs from aligned spin black hole binaries can then be expressed in the Fourier domain as

$$
\tilde h\_m(\vec\lambda; f) := A\_0(\vec\lambda) 
I\_f[V_A \cdot I\_\otimes [\mathcal{M}\_A] (\vec\lambda) ] (f) 
\exp \left[ i I\_f[V_A \cdot I\_\otimes [\mathcal{M}\_A] (\vec\lambda) ] (f) \right],
$$
where $I_f [\cdot]$ denotes cubic spline interpolation in frequency and $A_0$ is an amplitude prefactor.

# Implementation

You can find my implementation for the latest aligned spin dominant mode model in LIGO's LALSuite analysis package at [github](https://github.com/mpuerrer/lalsuite/blob/master/lalsimulation/src/LALSimIMRSEOBNRv4ROM.c).


# Speedup

The plot below shows the ratio of evaluation time for the original model and the surrogate model which reaches several thousands.

{{< figure src="Speedup.png" id="Speedup" >}}


# Accuracy

To assess model accuracy I compute mismatches between waveforms from the original model and the surrogate. The **mismatch** is related to the normalized noise-weighted inner product between two waveforms maximized over time and phase.

{{< figure src="mismatches.png" id="mismatch" >}}


# Sparse grids

A sparse frequency grid can be constructed with the greedy algorithm shown below. It helps compress the waveform data before computing the SVD which has complexity $\mathcal{O}(m n^2)$ and can otherwise become rather expensive.

{{< figure src="greedy_frequency_points.png" id="greedy_frequency_points" >}}


<!-- # A GPR surrogate model

[Code](https://github.com/benjaminlackey/gpsurrogate) 
[LALSuite](https://github.com/mpuerrer/lalsuite/blob/master/lalsimulation/src/LALSimIMRSEOBNRv4TSurrogate.c)

-->

