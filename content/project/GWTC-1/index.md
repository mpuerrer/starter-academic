---
title: GTWC-1, LIGO and Virgo's first catalog of gravitational-wave events
summary: Results from the LIGO Scientific Collaboration and Virgo Collaboration (LVC) for coalescing binary black holes and binary neutron stars from the GTWC-1 catalog.
tags:
- LIGO
- Data Analysis
date: "2018-12-03"
math: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  #caption: Masses of observed black holes and neutron stars
  focal_point: Smart


# links:
# - icon: twitter
#   icon_pack: fab
#   name: Follow
#   url: https://twitter.com/


# url_code:
url_code: ""
url_pdf: "https://journals.aps.org/prx/abstract/10.1103/PhysRevX.9.031040"
url_slides: "https://umd.box.com/s/z5ds89i4hpdxqndksi754qy9jjmjsj0h"
url_video: "https://youtu.be/G7l7U_OP_8g?t=11860"


# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

# Introduction 

LIGO and Virgo can observe gravitational waves from the inspiral and merger of compact binaries,
which are among the most extreme and bright events in the Universe. The emitted waves are of gravitational rather than electromagnetic nature and are radiated from the orbiting and accelerating black holes or neutron stars until they merge and form a stable remnant.

These wave signals are buried in noisy data streams recorded by the interferometric gravitational wave detectors LIGO and Virgo. A crucial tool to find the signals in the data and to identify the astrophysical properties of their sources are accurate models of the gravitational waves emitted in the merger. I have made important contributions to building accurate and fast source models of compact binaries and to the Bayesian analysis of the astrophysical signal parameters.


# How to measure the masses and spins

Given a *waveform model* $h(\vec\lambda)$ and time series data $d(t)$ recorded by the detector we can define a *likelihood function* (assuming stationary Gaussian noise)

$$
\mathcal{L}(d|\vec\lambda) \propto \left[  -\frac{1}{2} \langle d - h(\vec\lambda), d - h(\vec\lambda) \rangle \right],
$$

and numerically sample the *posterior probability density* of the model parameters $\vec\lambda$ given the data $d$ (Bayes' theorem):

$$
p(\vec\lambda | d, M) = \frac{p(\vec\lambda | M) p(d|\vec\lambda, M) }{p(d|M)}.
$$

Here, $\langle h_1, h_2 \rangle$ is an *inner product* between waveforms, weighted by the detector noise.


# Presentations

I presented the results of the "GWTC-1" catalog of compact binaries at the Joint Space-Science Institute Gravitational Wave Physics and Astronomy Workshop ([GWPAW](https://jsi.astro.umd.edu/2018-jsi-workshop/program)) in Maryland on December 1, 2018 on behalf of the LIGO Scientific Collaboration and Virgo Collaboration. 

We performed a thorough analysis of all 11 gravitational-wave detections found in the first two observing runs of LIGO and Virgo (O1 and O2). We relied on state-of-the art models of the gravitational waveform emitted from these cataclysmic events to infer the binaries’ masses, spins and tidal deformabilities. I am very proud to have been part of this outstanding effort by the LIGO Scientific Collaboration and Virgo Collaboration.

I gave a another presentation of the GWTC-1 results on May 20, 2019, at the Harvard "Black hole initiative" conference. You can watch my talk on [youtube](https://youtu.be/G7l7U_OP_8g?t=11860).


# Masses in the stellar graveyard

The graphic above shows the masses of black holes (blue) and neutron stars (orange) observed by LIGO and Virgo in the GWTC-1 catalog (2018); electromagnetic observations of black holes and neutron stars  are shown in violet and yellow, respectively. You can see at a glance that LIGO/Virgo black holes tend to be more massive than black holes observed through electromagnetic 
means.


# Links

To learn more about these observations you take a look at the following links:
  * [Science summary](https://www.ligo.org/science/Publication-O2Catalog/flyer.pdf) released by the LIGO Scientific and Virgo Collaborations.
  * LIGO's [O1/O2 Catalog webpage](https://www.ligo.org/detections/O1O2catalog.php).
  * The [technical publication](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.9.031040).
  * The [press release](https://www.aei.mpg.de/78997/ligo-and-virgo-announce-four-new-gravitational-wave-detections) put out by the Albert Einstein Institute.



