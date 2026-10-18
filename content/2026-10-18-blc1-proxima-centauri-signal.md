---
title: BLC1: The "Signal from Proxima Centauri" That Fooled the Filters
slug: blc1-proxima-centauri-signal
category: Claims & Verdicts
published: 2026-10-18
verdict: Explained
summary: In 2019 a narrowband radio signal at 982 MHz seemed to come only from the direction of Proxima Centauri, the nearest star; a detailed 2021 analysis traced it to human-made radio interference, and 39 hours of follow-up listening never heard it again.
---
## The best candidate Breakthrough Listen ever had

![A giant white radio dish, its mesh outer rim and solid inner surface tilted toward the sky, sits on a brown cylindrical tower under a blue sky, with a much smaller dish in the background](parkes-murriyang.jpg)
*The 64-metre Parkes radio telescope in New South Wales, Australia, also known by its Wiradjuri name Murriyang. BLC1 turned up in data it recorded while pointed at Proxima Centauri in April 2019. Credit: Stephen West (Diceman), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Parkes_Radio_Telescope_09.jpg), CC BY-SA 3.0.*

**Breakthrough Listen** is the privately funded search for alien radio and laser signals run by the Breakthrough Initiatives, which began observing in 2016. From **April 29 to May 4, 2019**, it piggybacked on a campaign that used the CSIRO **Parkes "Murriyang"** telescope to watch **Proxima Centauri** for stellar flares. Proxima is the closest star to the Sun, about 4.2 light-years away, and it has a roughly Earth-mass planet, **Proxima b**, in its habitable zone. Parkes stared at it for **26 hours and 9 minutes** across a huge band of radio frequencies, 0.7 to 4.0 GHz, split into channels just **3.81 Hz** wide.

Searching those data in 2020, team member **Shane Smith** found something that survived every automatic filter. The team's software flagged **4,172,702 "hits"** (narrow signals above the noise). **5,160** of them showed up while the telescope pointed at Proxima but not when it pointed away. After visual checks, exactly **one** was left. They called it **BLC1**, short for "Breakthrough Listen Candidate 1".

## Why BLC1 looked so good

The detailed analysis by **Sofia Sheikh** and colleagues (*Nature Astronomy*, October 2021) lists what made it stand out:

- **It was extremely narrow**, under 3.81 Hz wide, at about **982.002 MHz**. Natural radio sources such as stars and gas clouds don't make signals that narrow. Only technology does.
- **Its frequency drifted** at about **0.03 Hz per second**. That's what you'd expect from a transmitter that is moving or accelerating relative to Earth, such as one on a spinning, orbiting planet, rather than one sitting still on the ground near the telescope.
- **The drift itself changed smoothly** over the hours, as if the source were following an orbit.
- **It vanished when the telescope looked away.** The team alternated 30 minutes on Proxima with 5 minutes on calibrator sources (quasars). BLC1 appeared in five of the Proxima scans and in none of the nine "off" scans.
- **It lasted about five hours**, from 13:17 to 18:19 UTC on April 29, 2019. That's far longer than a passing plane or a low-orbit satellite could stay in view.
- **Nothing official transmits there.** The Australian Communications and Media Authority had no registered transmitters at 982.002 MHz in Australia, and the observatory had no catalogued interference at that frequency. The wider band is reserved for aircraft navigation.

![Two-panel chart. Left: the signal's start frequency rises in five steps from 0 to about 400 Hz above 982.00241 MHz between 13:17 and 17:54 UTC. Right: the drift rate stays near 0.03 Hz per second for the first four scans, then drops to about 0.011 Hz per second in the last one](blc1-drift.png)
*BLC1 in each of the five 30-minute Proxima scans where it was detected. The frequency crept up by about 400 Hz over the afternoon, and the drift rate slowed. That smooth change in drift is part of what made it look like a transmitter on an orbiting body. Error bars are the authors' "error proxy," not formal uncertainties. Chart by IEI, plotting data from Sheikh et al. 2021, Nature Astronomy, [Supplementary Table S1 (arXiv:2111.06350)](https://arxiv.org/abs/2111.06350).*

## The leak

The team was still working when the story got out. On **December 18, 2020**, *The Guardian* reported that Breakthrough Listen scientists were investigating a radio beam that "appears to have come from the direction of Proxima Centauri," and that they had not yet found an Earthly culprit. *National Geographic* ran a fuller story the same day and noted the detection had been leaked before the research was ready. Even then, Sheikh told *National Geographic* that the team strongly suspected a human origin. The headlines were still irresistible: a possible signal from the nearest star, which also happens to be the target of Breakthrough's own Starshot probe concept.

## How it was taken apart

Sheikh's team didn't just say "probably interference." They built a **10-step verification checklist** and ran BLC1 through it. The key findings:

- **Ordinary moving transmitters didn't fit.** They modelled cars on the nearby highway, walkers, planes on routes such as Melbourne to Sydney, every known non-low-orbit satellite above the horizon (using orbital data from space-track.org), and deep-space probes including Voyager 2, New Horizons and Juno. Vehicles fast enough to give the right drift couldn't stay in range for five hours, and slower ones gave too little drift. The satellite and probe drifts didn't match either.
- **It didn't match Proxima either.** Earth's rotation should give any genuine signal from Proxima's direction a particular drift pattern after correction. BLC1's drift didn't fit that pattern, though the authors noted that a transmitter on one of Proxima's planets could produce drifts of roughly the right size.
- **A passing asteroid was a coincidence.** A small near-Earth asteroid, **2019 GG3**, was within about 1° of Proxima during the observations. A transmitter on it, or a radar reflection off it, would have drifted in the wrong direction, so the team ruled it out.
- **BLC1 had relatives.** The team searched about **7,000** archival Parkes observations from 2019 and 2020. They found four fainter signals at the same frequency on other days of the Proxima campaign, plus one on a different star four days earlier that was clearly interference. Several of these showed up in off-source scans too.
- **It had dozens of lookalikes at other frequencies, all of them interference.** In the same observation they found **36** signals with BLC1's exact drift shape and **27** mirror images that drifted the opposite way, about 60 in total. All of them appeared in the off-source scans, which marks them as local.
- **The lookalikes followed a pattern made by electronics.** Their spacings were whole multiples of frequencies used by **clock oscillators** (the timing crystals inside digital devices), such as 133.33 MHz, 15 MHz and **2.000004 MHz**. BLC1 sat exactly in step with three lookalikes, near 712, 856 and 1,062 MHz, at multiples of that 2.000004 MHz spacing.

Their conclusion was that BLC1 was an **intermodulation product**. When two or more radio signals pass through the same electronics, they can mix and create "ghost" signals at sums and differences of their frequencies. Here, a roughly 2 MHz clock oscillator was mixing with other interference somewhere near the telescope. The specific device was never identified. Why did the ghost appear only when the telescope pointed at Proxima? The authors concluded that its strength happened to rise and fall in step with the observing pattern. From millions of hits, the filters picked out the one whose timing happened to match. In the Breakthrough press release, Sheikh put it this way: "given a haystack of millions of signals, the most likely explanation is still that it is a transmission from human technology that happens to be 'weird' in just the right way to fool our filters."

## Listening again

The team also went back. They re-observed Proxima with the same receiver in **November 2020**, again in early 2021, and for five days from **April 29 to May 3, 2021**, matching the original dates, time of day and observing pattern. A follow-up note in *Research Notes of the AAS* reports **39 hours** of re-observation with **no re-detection** of BLC1, and no other signal of interest within 1 MHz of 982.002 MHz. The authors said this makes a repeating transmission or a twinkling (scintillating) interstellar source less likely, and is consistent with brief local interference.

## Our verdict: Explained

**What is established:** a narrowband, drifting signal at 982.002 MHz appeared in five Parkes scans of Proxima Centauri on April 29, 2019, and in none of the off-source scans that day. This is documented in two peer-reviewed papers with public data.

**What explains it:** a chain of evidence, not just a hunch. Dozens of lookalikes in the same data, all clearly local, share BLC1's drift shape. Their frequencies are tied together by common clock-oscillator spacings, and BLC1 fits that frequency ladder. Weaker copies at the same frequency turned up on other days, some of them in off-source scans. Thirty-nine hours of re-observation found nothing.

**What remains open:** the exact device was never found, and the team couldn't fully explain why BLC1 was missing from every off-source scan. A tiny sliver of doubt therefore remains. The authors' own scoring on the Rio Scale 2.0, a rating system for how significant a possible SETI detection is, put the chance of an interstellar origin at effectively zero.

So it's **Explained**, and honestly that's the good news. BLC1 showed that a modern SETI pipeline can find the single strangest signal among four million, and that a team will publish its full working, including a public data release, rather than either hyping or burying it. Compare the [Wow! signal](https://deedesigns.github.io/iei-archive/articles/wow-signal.html), which was never re-detected and came with far less data to check.

## What changed afterwards

BLC1 led directly to the verification framework now used for future signals of interest. The paper's top recommendation was to observe from two sites at once, so that interference local to one telescope can't fool both. Breakthrough Listen has since built an automated search system at the **MeerKAT** array in South Africa, called BLUSE. An array can compare many antennas and beams at the same time instead of nodding a single dish on and off a target. By 2024 BLUSE had processed roughly half a million pointings. As of today we haven't found any peer-reviewed report of a signal from Proxima Centauri or anywhere else that has survived that kind of scrutiny. This page reflects sources we could verify as of October 18, 2026.

## Sources

- [Sheikh et al. 2021, "Analysis of the Breakthrough Listen signal of interest blc1 with a technosignature verification framework", Nature Astronomy](https://doi.org/10.1038/s41550-021-01508-8) ([arXiv:2111.06350](https://arxiv.org/abs/2111.06350), including Supplementary Table S1)
- [Smith et al. 2021, "A radio technosignature search towards Proxima Centauri resulting in a signal of interest", Nature Astronomy](https://doi.org/10.1038/s41550-021-01479-w) ([arXiv:2111.08007](https://arxiv.org/abs/2111.08007))
- ["No Redetections of blc1 in 39 hr of Reobservation Campaigns of Proxima Centauri", Research Notes of the AAS (2021)](https://iopscience.iop.org/article/10.3847/2515-5172/ac33b2)
- [Breakthrough Initiatives: "Breakthrough Listen Releases Analysis of Previously Detected Signal" (Oct. 25, 2021)](https://breakthroughinitiatives.org/news/33)
- [Berkeley SETI Research Center: blc1 data release](https://seti.berkeley.edu/blc1)
- [The Guardian: "Scientists looking for aliens investigate radio beam 'from nearby star'" (Dec. 18, 2020)](https://www.theguardian.com/science/2020/dec/18/scientists-looking-for-aliens-investigate-radio-beam-from-nearby-star)
- [National Geographic: "Alien hunters detect mysterious radio signal from nearby star" (Dec. 18, 2020)](https://www.nationalgeographic.com/science/article/alien-hunters-detect-mysterious-radio-signal-from-nearby-star)
- [IAF / IAC 2024: "Early Results from Breakthrough Listen's Automated Commensal Technosignature Survey at MeerKAT" (Czech)](https://www.iafastro.org/events/iac/international-astronautical-congress-2024/technical-programme/symposium-keynotes/a41-pesek-lecture-early-results-from-breakthrough-listens-automated-commensal-technosignature-survey-at-meerkat.html)
- [Parkes Radio Telescope photo by Stephen West, via Wikimedia Commons (CC BY-SA 3.0)](https://commons.wikimedia.org/wiki/File:Parkes_Radio_Telescope_09.jpg)
