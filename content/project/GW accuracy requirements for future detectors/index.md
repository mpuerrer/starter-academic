---
title: Gravitational waveform accuracy requirements for future ground-based detectors
summary: We assess how accurate models of gravitations waves should be to avoid systematic errors in the measurement of the binaries' parameters.
tags:
- LIGO
- Data Analysis
date: "2020-06-01"
math: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
#  caption: Statistical error (blue) will decrease as GW detectors become more and more sensitive, but systematic errors in waveform models (red) and numerical relativity (green) are constant and will dominate for loud signals.
  focal_point: Smart

links:
#- icon: twitter
#  icon_pack: fab
#  name: Follow
#  url: https://twitter.com/georgecushen
url_code: ""
url_pdf: "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.023151"
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---


# Introduction

Gravitational wave detectors record GW signals in detector noise. If we can make the noise floor lower, then the detector can observe fainter sources in the Universe and we will learn more about the properties and the origin of compact binaries. The current LIGO, Virgo and Kagra detectors have already made dozens of intriguing observations of astrophysical mergers and use second-generation technologies. Here we are interested in stellar mass black hole binary mergers, with component masses between $\sim 3$ to $\sim 100$ solar masses.

Future third-generation (3G) ground-based gravitational wave (GW) detectors, such as the planned Einstein Telescope in Europe and Cosmic Explorer in the US, will have unprecedented sensitivities enabling studies of the entire population of stellar mass binary black hole coalescences in the Universe.

To infer binary parameters from a GW signal we require accurate models of the gravitational waveform as a function of black hole masses, spins, etc. Such waveform models are built from numerical relativity (NR) simulations (full numerical simulations, solving Einstein's equations in 3+1 dimensions) and/or semi-analytical expressions in the inspiral. 

We investigate the limits of the current waveform models and study at what detector sensitivity these models will yield unbiased parameter inference for loud “golden” binary black hole systems, what biases we can expect beyond these limits, and what implications such biases will have for GW astrophysics. 

The graphic above shows that the statistical error (shown in blue) which comes from the noise floor in the detectors will decrease as GW detectors become more and more sensitive. However, systematic errors in waveform models (red) and numerical relativity (green) are constant (for a particular model evaluated at particular binary parameters) and will therefore dominate for loud signals.

# What are errors in waveforms?

Even the most accurate waveforms computed from numerical relativity simulations can only approximate the true waveform emitted from a merging compact binary. We need a tool to assess how accurate waveforms are and should be. We can define an *inner product* between a signal $d(t)$ and a waveform $h(t)$ and weight it by the the detector noise (its power spectral density $S_n(f)$). This is conveniently done in the Fourier domain: $\tilde h(f)$ denotes the Fourier transform of $h(t)$ and $^*$ conjugation. We define the inner product as 
<!-- shown in the [figure](#figure-inner_product) below. -->

<!-- $$
\langle d | h \rangle =
4\\, \mathrm{Re} \int_0^{\infty} \frac{ \tilde d(f) \tilde h^*(f)}{S\_n(f)} \mathrm{d}f
$$ -->

{{< figure src="inner_product.png" id="inner_product" >}}


Typically we maximize $\langle d | h \rangle$ over relative time and phase shifts which we do not care about for assessing accuracy and normalize the expression. This gives a quantity called "match", ranging between 0 and 1. If the match is close to 1, it is convenient to use the "mismatch" = 1 - match.


With this in hand we find that for 3G detectors the mismatch error for semi-analytical models needs to be reduced by at least **three orders of magnitude** and for NR waveforms by **one order of magnitude**. 


# How wrong will estimated masses and spins be?

We have just seen that model waveforms are imperfect and have errors. If we use imperfect models to perform a measurement then we expect that we won't be able to correctly infer the true parameters of the source binary. So, instead we'll get the true parameters plus or minus an offset, giving us a *biased* estimate.

In the paper we show that typical biases in units of standard deviations for the mass-ratio (the ratio of component masses of the binary) and effective aligned-spin (a linear combination of the black holes' spin components perpendicular to the orbital plane of the binary) will be of order unity for 2G design sensitivity and will reach several tens for 3G networks. 

The figure below shows how spin measurements can be affected. The contours are for detectors that become more an more accurate which makes the contours shrink, but in this case the center of the contours are strongly offset from the true value (red asterisk).

{{< figure src="effective_spin_posteriors.png" id="effective_spin_posteriors" >}}


So far we have looked at single events. But we are already observing dozens of binaries and will observe a lot more in the future! In that case it is more useful to say something about the population of stellar mass black hole binaries in the Universe.

We show that for a population of one hundred high mass precessing binary black holes, measurement errors sum up to a sizable population bias, about 10–30 times larger than the sum of error bars (to be precise, the sum of the 90% credible intervals) for mass and spin parameters.

# How does this affect residual tests?

We do not know for sure that Einstein's theory of general relativity is correct, and so scientists are looking to see whether we can observe any deviations from the GR waveforms. One way of doing this is to subtract the best fit waveform (from Bayesian parameter inference) from the data stream and analyze what's left. That's the residual.

We have seen above that waveforms are imperfect and so this will leave an imprint in the residual. We demonstrate that the residual signal can be very loud (i.e, have significant signal-to-noise ratio) and can lead to Bayes factors (this is a way of model comparison) as high as $10^{11}$ between a coherent and an incoherent wavelet model for the population events. This coherent power left in the residual could lead to the observation of erroneous deviations from general relativity. 

The figure below shows a residual in time - frequency space along with the evolution of the emitted GW signal (red). The residual is largest near the merger (highest frequency in the signal) -- that is where gravity is most non-linear and hardest to model.

{{< figure src="residual_power.png" id="residual_power" >}}

 
# The take-away message


We have seen that imperfect waveform models cause a series of problems in the measurement of the properties of merging binary black holes, both for single events and when considering the population. Tests of GR are affected as well and we will have to be very careful with their interpretation.

To address these issues and be ready to reap the scientific benefits of 3rd generation GW detectors in the 2030s, waveform models that are significantly more physically complete and accurate need to be developed in the next decade along with major advances in efficiency and accuracy of NR codes. So, there is a lot of work that is left to be done!

