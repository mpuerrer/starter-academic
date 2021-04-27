---
title: Deep learning surrogate model of gravitational waves
summary: Deep learning algorithms have the potential to dramatically improve predictive models of chirp like gravitational waves.
tags:
- Deep Learning
- Surrogate model
- Data Analysis
- gravitational waves
date: "2021-04-26T00:00:00Z"
math: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Waveform data pieces
  focal_point: smart
  preview_only: false

<!-- links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/ -->
url_code: ""
url_pdf: ""
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

Recently, I looked at how machine learning techniques can be used to model gravitational waves emitted from merging binary black holes. I pose the problem
as follows: the labels or input parameters $\vec\lambda$ are parameters describing the merging binary (the ratio of component masses and the components of the black holes' spin vectors), while the targets are the two polarization states $h\_+(t), h\_\times(t)$ of the gravitational wave in general relativity as a function of time. So, we want to find a mapping from $f: \mathbb{R}^n \mapsto (\mathbb{R}^m, \mathbb{R}^m)$, with $n=7$ (precessing binaries) and $m$ the number of time nodes in the output grid. This is a vector valued regression problem.

It is known that neural networks are universal function approximators (under certain technical conditions), but the available theorems do not provide any advice on a preferred network architecture and training procedure.

In a first [study](https://iopscience.iop.org/article/10.1088/1361-6382/ab693b) led by Yoshinta Setyawati and her advisor Frank Ohme along with myself we compared classical regression methods with methods from machine learning, including Gaussian process regression, and neural networks. I won't go over the detailed results here, but, in summary, we found that classical methods such as polynomial fits performed best. Likely this was due to the limited about of training data and the relatively shallow networks.


# A deep learning model of GWs


In the meantime I have built deeper neural networks that perform much better given sufficient data. I have used multi-layer perceptrons with a depth of 24 layers and two million waveforms in the data set.

In principle, one could try to model $h\_+(t), h\_\times(t)$ directly. But one quickly realizes that this is a very hard task due to the sinusoidal and chirp  behavior which is modulated by precession of the binary's orbital plane and results in a very complex morphology and sensitive dependence on the 7 input parameters. 

The fact that the input parameters are 7-dimensional also brings a further problem: the so-called *curse of dimensionality*. It is infeasible to produce and work with waveform data with a fixed number of grid points in each dimension. Even a crude resolution of a mere 10 points per dimension would result in target data sizes of $10^7 \times m$, where $m$ is at least on the order of one hundred for short waveforms, and the number of waveforms depends exponentially on the number of points per dimension.

Therefore, it is quite beneficial to decompose the polarizations $h\_+(t), h\_\times(t)$ into a number of simpler functions which I will call waveform *data pieces*. I won't go into the details here which are somewhat complicated and are motivated by several physical insights. In simple terms one can split the polarizations into quantities that describe the dynamics (a phase and a description of a time-dependent rotation) and modes of the waveform (in a basis of special spherical harmonics appropriate for waveforms).

This is what I show in the main figure on the top of the page. In the leftmost column I collect the data pieces for each of which I train a separate network.
In the second column, I compute the quaternion time series that describes the frame rotation from constituent parts. In the third column I plot waveform modes in a precession adapted reference frame (a frame where the orbital plane is stationary), and, finally, in the fourth column I show the polarizations $h\_+(t), h\_\times(t)$.


# Model accuracy

So, how well can the data piece networks be trained and how accurate are the waveform polarizations after putting everything together?

The plot below shows the configuration with the largest error in the test set for the orbital frequency $\omega_\mathrm{orb}$. Both the data and the DL model evaluated at the data parameters are plotted and match quite closely with a small disagreement appearing in the non-linear merger region before the function reaches a plateau. This results in a sub-radian phase accuracy.

<!-- plot instead as a function of time; use latex in y-label -->
{{< figure src="omega.png" id="omega" >}}


The "mismatch" between the DL model and the original waveform model (I chose a numerical relativity surrogate model) is shown below. This is a normalized waveform overlap, maximized over relative time and phase shifts which ranges between 0 and 1, where 0 would be perfect agreement. The mismatch has a median of about $10^{-3}$ and is better than $0.1$. Except for a few cases in the tail of the distribution this is pretty good accuracy.

{{< figure src="FD_mismatch.png" id="mismatch" >}}


