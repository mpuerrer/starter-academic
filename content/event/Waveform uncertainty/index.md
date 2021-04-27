---
title: "Incorporating waveform uncertainty into modeling and inference of GWs"
event: "Statistical Methods for the Detection, Classification, and Inference of Relativistic Objects."
location: ICERM, Brown University
event_url: https://icerm.brown.edu/programs/sp-f20/w4/#workshopschedule
#address:
#  street: 450 Serra Mall
#  city: Stanford
#  region: CA
#  postcode: '94305'
#  country: United States

summary: "I discuss how systematic errors in waveform models can affect parameter inference and how these errors can be incorporated into the waveform model construction."
abstract: "I discuss how systematic errors in waveform models can affect parameter inference and how these errors can be incorporated into the waveform model construction. For models that include these errors one can marginalize the posterior distribution over these additional degrees of freedom. I demonstrate this for an aligned- spin effective-one-body model where the uncertainties are captured by an efficient Fourier domain GPR model."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "18 Nov 2020"
date_end: "18 Nov 2020"
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "18 Nov 2020"

authors: [Michael Pürrer and Stephen Green]
tags: [Data Analysis, Gaussian Process Regression, Deep Learning, LIGO]

# Is this a featured talk? (true/false)
featured: true

image:
  caption: 'Comparison of marginal posterior distributions for a GW150914-like NR-surrogate signal.'
  focal_point: Right

links:
#- icon: twitter
#  icon_pack: fab
#  name: Follow
#  url: https://twitter.com/
url_code: ""
url_pdf: ""
url_slides: "https://icerm.brown.edu/materials/Slides/sp-f20-w4/Incorporating_waveform_uncertainty_into_modeling_and_inference_of_gravitational_waves_]_Michael_Pürrer,_Max_Planck_Institute_for_Gravitational_Physics.pdf"
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
- example
---

## Parameter inference marginalizing over model calibration errors

We built a effective-one-body (EOB) based waveform model that also incorporates calibration errors of the base effective-one-body model against numerical relativity. 
We want to incorporate the uncertainty in the waveform model $h(\boldsymbol\lambda) \to p(h | \boldsymbol\lambda)$.

To achieve this we modeled the additional degrees of freedom as amplitude and phase deviations in the Fourier domain w.r.t. a neutral EOB calibration using **Gaussian process regression** (GPR). The error model has $2 \times 10$ additional parameters $\epsilon$ and is applied as a correction on top of SEOBNRv4_ROM. It has the following form

$$
\delta \tilde h_{CE}(\boldsymbol\lambda, \boldsymbol\epsilon; f) = (1 + \delta A(\boldsymbol\lambda, \boldsymbol\epsilon; f)) \, \exp(i \, \delta\phi(\boldsymbol\lambda, \boldsymbol\epsilon; f))
$$

For parameter inference (using a NRSur3dq8 signal in zero noise) we sample SEOBNRv4CE over $\lambda$ and $\epsilon$, and marginalize over $\epsilon$. This leads to posterior distributions which are less precise, but reduce biases compared to SEOBNRv4_ROM or SEOBNRv4CE with $\epsilon=0$.


## A mixture density network for calibration posteriors


The SEOBNRv4 effective-one body waveform model used a polynomial fit to the means of the calibration posteriors $p(\boldsymbol\theta | \boldsymbol\lambda)$￼at the numerical relativity points $\{ \boldsymbol\lambda_i \}$ to tune free parameters.

We propose to improve on this by a using mixture of Gaussians, i.e. a **mixture density network** (MDN)

$$
p(\boldsymbol\theta | \boldsymbol\lambda) \approx \sum_{k=1}^K \pi_k(\boldsymbol\lambda) \mathcal{N}(\boldsymbol\theta | \mu_k(\boldsymbol\lambda), \sigma_k^2(\boldsymbol\lambda)))
$$

Here, $\boldsymbol\lambda$ are the physical parameters of the binary (the mass-ratio and the spins projected onto the orbital angular momentum vector), while $\boldsymbol\theta$ are the calibration parameters in the EOB waveform model.

{{< figure src="MDN.png" id="MDN" >}}

<!-- {{% callout note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /callout %}}

Slides can be added in a few ways:

- **Create** slides using Wowchemy's [*Slides*](https://wowchemy.com/docs/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://wowchemy.com/docs/writing-markdown-latex/).

Further event details, including [page elements](https://wowchemy.com/docs/writing-markdown-latex/) such as image galleries, can be added to the body of this page. -->
