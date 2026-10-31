---
title: Seven Dyson Sphere Candidates? Project Hephaistos and the Galaxies Hiding Behind the Stars
slug: dyson-sphere-candidates-hephaistos
category: The Search
published: 2026-10-31
verdict: Disputed
summary: In 2024 a search of five million stars flagged seven red dwarfs glowing in the infrared the way a partial Dyson sphere might, but follow-up radio work shows at least one is a normal star sitting in front of a distant dusty galaxy, and the rest are under strong suspicion.
---
## The idea: look for waste heat

In 1960 the physicist Freeman Dyson published a short paper in *Science* titled "Search for Artificial Stellar Sources of Infrared Radiation." His argument was simple: a civilization that keeps growing will eventually want most of its star's energy, and any structure that captures starlight must get rid of the absorbed energy as heat. That heat should glow in the infrared. So instead of waiting for someone to send us a message, we could look for stars that are a little too dim in visible light and too bright in the mid-infrared. Any such shell or swarm of collectors is now called a **Dyson sphere**.

The beauty of the idea is that it doesn't depend on aliens wanting to be found. The problem is that the universe is full of natural things that also glow in the infrared: dust around young stars, debris disks left by colliding planets, and, as this story shows, galaxies far in the background.

## Project Hephaistos: a search of five million stars

Project Hephaistos is a Dyson sphere search led from Uppsala University in Sweden, with Penn State's Jason Wright among the collaborators. Its second paper, by **Matías Suazo and colleagues**, appeared in *Monthly Notices of the Royal Astronomical Society* in May 2024. The team combined three sky surveys: ESA's **Gaia** (visible light plus distances), **2MASS** (near-infrared) and NASA's **WISE** (mid-infrared, including the 12 and 22 micron bands where a Dyson sphere's waste heat should show up).

They modeled what a star would look like with a partial Dyson sphere, between 100 and 700 K in temperature and covering 10% to 90% of the star, and compared those models with about 5 million stars within 300 parsecs (roughly 980 light-years). Then they threw out impostors step by step: stars in dusty nebulae (using a neural network trained on WISE images), stars showing hydrogen-alpha emission or brightness flicker (signs of youth), stars with messy positional data that might be binaries, faint detections, and finally everything that looked blended with a neighbor when they inspected the images by eye.

![Two bar charts: a log-scale funnel from about 5 million stars down to 7 candidates, and a bar chart showing 328 blends, 29 irregular, 4 nebular and 7 surviving candidates among the last 368 sources](hephaistos-candidate-funnel.png)
*How Project Hephaistos narrowed about 5 million stars to 7 Dyson sphere candidates. Most sources that survived to the last stage turned out to be blends with nearby objects. Chart by the Institute for Extraterrestrial Inquiry. Data: [Suazo et al. 2024, MNRAS 531, 695](https://doi.org/10.1093/mnras/stae1186), Table 4 and Section 2.7. Our own chart.*

## What they found

Seven sources survived, labeled **A through G**. All seven are **M dwarfs** (small red stars), about 140 to 275 parsecs away, with infrared excesses that the authors' best-fitting models matched to a Dyson sphere at about 100 to 275 K covering roughly 3% to 16% of the star.

The excitement was understandable. M dwarfs very rarely have the warm, bright dust that could explain such a glow, and the stars didn't flicker the way young stars usually do. But the authors themselves were careful. They wrote that "it is definitely premature to presume" the infrared light comes from Dyson spheres, noted that the mid-infrared data quality is "typically quite low," and called for follow-up spectroscopy.

They also flagged a warning sign. For **candidate G**, the center of the infrared light in WISE's 12 micron band was shifted about 5.6 arcseconds from the star's position, larger than expected. And they estimated that chance alignments with background galaxies could account for about two contaminated sources in a sample of this size.

## The skeptics: galaxies behind the stars

Within weeks, **Tongtian Ren, Michael Garrett and Andrew Siemion** (Jodrell Bank, University of Manchester, and Breakthrough Listen) checked radio sky surveys. They found radio sources near three of the candidates:

- **A**: a radio source about 4.9 arcseconds from the star.
- **B**: a radio source about 0.4 arcseconds from the star.
- **G**: a radio source about 5.0 arcseconds away, with a steep radio spectrum typical of a jet-launching active galactic nucleus (a feeding supermassive black hole in a distant galaxy).

Red dwarfs rarely give off steady radio emission, so their explanation was that dusty galaxies sit almost directly behind these stars. WISE's images are blurry, about 6 to 12 arcseconds across, so a galaxy a few arcseconds away gets folded into the star's infrared brightness. They pointed to a particular class, **"hot DOGs"** (hot dust-obscured galaxies), which are faint in visible and near-infrared light but bright at exactly the wavelengths the search relied on. At about one per 31 square degrees of sky, there are enough of them to contaminate a handful of stars out of five million, which they argued could probably explain all seven candidates.

## The follow-up: candidate G is a galaxy

In early 2025 the same team published sharp radio images of the source near candidate G, taken with the UK's e-MERLIN array and the European VLBI Network. The source, **VLASS J233532.86-000424.9**, splits into three compact parts and has a brightness temperature above 100 million kelvin. That's the signature of a radio-loud active galactic nucleus, not a star. They detected **no radio emission at the star's position**. They also noted that WISE's shorter-wavelength light sits on the star, while the longer-wavelength light that made it a candidate drifts toward the galaxy.

Garrett told Phys.org that some, maybe all, of the candidates are probably contaminated, while adding that he hoped some turn out to be good Dyson sphere candidates. As far as we could find, no published study has yet confirmed or ruled out candidates C, D, E and F individually.

## What's evidence, what's claim, what's speculation

- **Evidence:** Seven M dwarfs have unusual mid-infrared excesses in WISE data. Three have radio sources nearby, and the radio source near G is definitely a background active galaxy.
- **Claim:** That these are "Dyson sphere candidates." That's a technical label meaning "consistent with our models and not yet explained." The authors never claimed to have found alien structures.
- **Speculation:** That any of them is artificial. Nothing in the data requires it, and a known natural explanation (background galaxies) has already worked for one candidate.

## Verdict

**Disputed, leaning strongly toward a natural explanation.** Candidate G is explained: its infrared glow is a distant galaxy behind an ordinary red dwarf. A and B very likely share the same problem. The other four haven't been individually explained, but the same contamination is a plausible fit, and the infrared data are too low quality to say more yet. This isn't a failure of the search. It's how a careful search is supposed to work: publish the oddballs, invite people to knock them down, and refine the filters. Like [Tabby's Star](https://deedesigns.github.io/iei-archive/articles/tabbys-star-boyajian.html), the Hephaistos candidates show how Dyson's 1960 idea keeps producing real astronomy even when the aliens don't turn up. Mid-infrared spectra from a telescope like JWST, or sharper infrared imaging that separates star from background, could settle the remaining four.

## Sources

- [Dyson 1960, "Search for Artificial Stellar Sources of Infrared Radiation," Science 131, 1667](https://doi.org/10.1126/science.131.3414.1667)
- [Suazo et al. 2024, "Project Hephaistos II: Dyson sphere candidates from Gaia DR3, 2MASS, and WISE," MNRAS 531, 695](https://doi.org/10.1093/mnras/stae1186) ([arXiv:2405.02927](https://arxiv.org/abs/2405.02927))
- [Ren, Garrett & Siemion 2024, "Background Contamination of the Project Hephaistos Dyson Spheres Candidates," RNAAS](https://doi.org/10.3847/2515-5172/ad5017) ([arXiv:2405.14921](https://arxiv.org/abs/2405.14921))
- [Ren, Garrett & Siemion 2025, "High-resolution imaging of the radio source associated with Project Hephaistos Dyson Sphere Candidate G," MNRAS Letters 538, L56](https://academic.oup.com/mnrasl/article/538/1/L56/7954734) ([arXiv:2501.05152](https://arxiv.org/abs/2501.05152))
- [Phys.org, "High-resolution imaging of Dyson sphere candidate reveals no radio signals" (February 2025)](https://phys.org/news/2025-02-high-resolution-imaging-dyson-sphere.html)
- [Project Hephaistos home page, Uppsala University](https://www.astro.uu.se/~ez/hephaistos/hephaistos.html)
