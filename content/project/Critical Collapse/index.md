---
title: Critical collapse
summary: Dynamical systems can have solutions which a shape that mimics itself on different scales.
tags:
- Numerical Simulations
- Einstein's Equations
- General Relativity
date: "2014-09-23"
math: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: An ingoing Gaussian wave approaches the critical solution and becomes self-similar. The wave is shown in logarithmic time (tau) and negative logarithmic space (x) coordinates, moving towards $x = -\infty$.
  focal_point: smart
  preview_only: false

<!-- links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/ -->
url_code: "https://github.com/mpuerrer/EYM-char-MOL"
url_pdf: "https://arxiv.org/pdf/0708.1914.pdf"
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

Partial differential equations such as Einstein's equations can have solutions with features that repeat themselves on different scales. We call this a **self-similar** solution. This phenomenon is well know from looking at a snowflake in the microscope where its structure looks similar at different magnifications.

# Critical collapse in spherical symmetry

A relatively simple, non-linear dynamical system with these properties are **Einstein's equations** in *spherical symmetry* (the spatial dimensions are symmetric shells and can be characterized just but a radius) coupled to a *massless scalar field* [Choptuik, PRL 70, 9, (1993)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.70.9). This system has two end states: if a wave is strong (or dense) enough it can collapse and form a Schwarzschild black hole, or if it is weaker, it can disperse to flat space time.

In my [PhD thesis](https://arxiv.org/pdf/0708.1914.pdf) and a technical paper [PRD 71, 104005, (2005)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.71.104005) I studied this system in a special coordinate system that allows to evolve the waves until infinity (I used compactified Bondi coordinates).
The figure at the top of this page shows a *Gaussian wave* pulse evolving in logarithmic time $\tau$ (you can clearly see it at $\tau = 0$) as it starts to approach the origin ($r=0$ which corresponds to $x = - \infty$). As it does so it comes close to a self-similar **attractor** which makes it loose its starting shape and turn into a series of discretely self-similar pulses that come ever closer to the origin as it evolves in time.

The self-similarity can only be seen if the initial Gaussian pulse is chosen very carefully so that its eventual endstate is either a very light black hole or slightly below that -- it requires *fine-tuning*. One can think of the attractor as a **limit cycle** with one *unstable direction* perpendicular to the cycle which drives away the solution to collapse or dispersion. In the picture below we need to fine tune an initial data parameter $p$ so that it almost lies in the plane where $p=p^*$ and it can get close to the critical solution before being driven away.

 {{< figure src="critical-solution.png" id="critical-solution" >}}

# Power law tails

A related effect which occurs in the solutions of nonlinear wave equations are radiation **tails**.
They are related to the fall-off properties of the field at late times ($\propto t^{p}$ with $0 < p \in \mathbb{N}$) and they emerge from primary outgoing radiation that is backscattered. This is a far-field effect which can either be due to a background or from an effective potential. I studied tails for the coupled Einstein - Yang Mills system with a special numerical code. It casts the hyperbolic evolution system as a characteristic initial value problem which is then solved with the method of lines with 6th order discretization in space and 4th order Runge Kutta in time.
We find $p = −2$ at future null infinity and $p = −4$ at spatial infinity.

 {{< figure src="EYM_tails.png" id="EYM_tails" >}}
