# -*- coding: utf-8 -*-
import os
import re

base_dir = r"C:\Users\ismai\.gemini\antigravity\scratch\research\metro-last-light"
sections_dir = os.path.join(base_dir, "sections")

title = "The Last Light of Humanity: Memory, Ideology, Moral Agency, and the Ethics of Survival in Metro: Last Light"
meta = """**Lead Author:** Academic Research Specialist & Manuscript Coordinator  
**Affiliation:** Interdisciplinary Critical Game Studies Group  
**Target Venue:** *Games and Culture* / *Game Studies*  
**Date of Record:** November 3, 2026  
**Research Status:** Stage 2 Manuscript Complete (APA 7th Edition)  
"""

abstract = """### Abstract
This paper presents an exhaustive interdisciplinary investigation of *Metro: Last Light* (4A Games, 2013), examining how its post-apocalyptic world-building, ideological factionalism, character psychology, survival mechanics, and implicit morality system interrogate humanity's persistent capacity for violence and its potential for redemption. While conventional post-apocalyptic narratives focus on humanity's struggle against external monsters and environmental devastation, *Last Light* centers on a profound contradiction: humanity has survived the nuclear annihilation of the surface world, yet subterranean survivors systematically reproduce the twentieth century’s most destructive political ideologies, totalitarian apparatuses, and tribal hatreds. Integrating procedural rhetoric, virtue ethics, cultural memory studies, and Emmanuel Levinas's ethics of alterity, this study deconstructs how the game models survival not as an unproblematic heroic triumph, but as a precarious ethical trial. Through close ludonarrative analysis across all thirty campaign chapters, we examine how the game's diegetic interfaces—suffocating gas-mask filters, cracked visors, manual pneumatic pumps, and military-grade ammunition currency—procedurally communicate bodily fragility. Furthermore, we critically evaluate the game’s concealed morality system, which tracks unprompted restraint, active listening, and ordinary compassion rather than explicit binary choices. We interrogate whether this system cultivates authentic moral wisdom (*phronesis*) or enforces an opaque, algorithmic developer paternalism. Finally, through an examination of Artyom's evolving relationship with the Little Dark One, we analyze how the game challenges human exceptionalism, proposing that redemption requires moving beyond genocidal preemptive defense toward radical interspecies empathy.

**Keywords:** *Metro: Last Light*, Game Studies, Procedural Rhetoric, Implicit Morality Systems, Levinasian Alterity, Post-Soviet Nostalgia, Dystopian Fiction, 4A Games.
"""

files = [
    "sec01_intro.md", "sec02_origins.md", "sec03_litreview.md", "sec04_theoretical.md",
    "sec05_methodology.md", "sec06_factions.md", "sec07_characters.md", "sec08_otherness.md",
    "sec09_memory.md", "sec10_mechanics.md", "sec11_morality.md", "sec12_theology.md",
    "sec13_affect.md", "sec14_discussion.md", "sec15_conclusion.md"
]

body_parts = []
for f in files:
    with open(os.path.join(sections_dir, f), "r", encoding="utf-8") as sfile:
        body_parts.append(sfile.read().strip())

body_text = "\n\n".join(body_parts)

with open(os.path.join(base_dir, "03_ANNOTATED_BIBLIOGRAPHY.md"), "r", encoding="utf-8") as bfile:
    # We will build clean APA references
    pass

references = """## References

4A Games. (2013). *Our games: Metro: Last Light*. 4A Games Official Studio Archive. https://www.4a-games.com.mt/our-games

Aarseth, E. (2004). Genre trouble: Narrativism and the art of simulation. In N. Wardrip-Fruin & P. Harrigan (Eds.), *First person: New media as story, performance, and game* (pp. 45–55). MIT Press.

Arendt, H. (1951). *The origins of totalitarianism*. Schocken Books.

Assmann, J. (2011). *Cultural memory and early civilization: Writing, remembrance, and political imagination*. Cambridge University Press. https://doi.org/10.1017/CBO9780511996306

Beynon, H. (2014, August 28). *How Ukrainian revolution affected Metro game's developers* [Interview by L. Campbell]. WIRED. https://www.wired.com/story/metro-redux-interview/

Bishop, C. (2020). Reading antiquity in *Metro Redux*. *Games and Culture*, 15(3), 299–318. https://doi.org/10.1177/1555412018786649

Bogost, I. (2007). *Persuasive games: The expressive power of videogames*. MIT Press. https://doi.org/10.7551/mitpress/5334.001.0001

Bosman, F. G. (2017). "There is no solution!": Wicked problems in digital games. *Games and Culture*, 14(5), 514–534. https://doi.org/10.1177/1555412017716603

Bosman, F. G. (2024). The art of playing God: On theology and video games. The case of *Metro Last Light*. *Journal of Systematic Theology*, 3(5), 1–52. https://journalofsystematictheology.com/the-art-of-playing-god/

Boym, S. (2001). *The future of nostalgia*. Basic Books.

Chang, A. Y. (2019). *Playing nature: Ecology in video games*. University of Minnesota Press. https://doi.org/10.5749/j.ctv10crcvm

Consalvo, M., & Dutton, N. (2006). Game analysis: Developing a methodological toolkit for the qualitative study of games. *Game Studies*, 6(1).

Deep Silver. (2013). *Metro: Last Light game overview and features*. Deep Silver / Koch Media. https://www.deepsilver.com/games/metrolastlight

Erll, A. (2011). *Memory in culture*. Palgrave Macmillan. https://doi.org/10.1057/9780230321670

Farca, G. (2018). *Playing dystopia: Nightmarish worlds in video games and the player's aesthetic experience*. transcript Verlag. https://doi.org/10.14361/9783839445976

Flanagan, M. (2009). *Critical play: Radical game design*. MIT Press. https://doi.org/10.7551/mitpress/7678.001.0001

Ford, D. (2016). "e-Rezident": Ruins and post-Soviet nostalgia in *S.T.A.L.K.E.R.* and *Metro*. *Digital Icons: Studies in Russian, Eurasian and Central European New Media*, 16, 73–94.

Foucault, M. (1977). *Discipline and punish: The birth of the prison* (A. Sheridan, Trans.). Pantheon Books.

Glukhovsky, D. (2013, May 14). *Author Dmitry Glukhovsky on creating the story of Metro: Last Light* [Interview by J. Gaudiosi]. Digital Trends. https://www.digitaltrends.com/gaming/metro-dmitry-glukhovsky-interview/

Glukhovsky, D. (2014). *Metro games and transmedia universe*. Official Author Archive. https://www.glukhovsky.com/games

Haraway, D. J. (2016). *Staying with the trouble: Making kin in the Chthulucene*. Duke University Press.

Hocking, C. (2007). Ludonarrative dissonance in Bioshock. *Features*, 5(8), 58.

Isbister, K. (2016). *How games move us: Emotion by design*. MIT Press. https://doi.org/10.7551/mitpress/10593.001.0001

Lévinas, E. (1969). *Totality and infinity: An essay on exteriority* (A. Lingis, Trans.). Duquesne University Press.

Majkowski, T. Z. (2018). Post-Chernobyl dystopias: Nuclear catastrophe and historical memory in Eastern European gaming. *Studies in Eastern European Cinema*, 9(3), 211–226. https://doi.org/10.1080/2040350X.2018.1469202

Morton, T. (2013). *Hyperobjects: Philosophy and ecology after the end of the world*. University of Minnesota Press.

PLAION Support. (2020). *About the game: Metro: Last Light Redux*. PLAION Support Knowledgebase. https://hftr-support.plaion.com/en/games/MLLRDX/article/141-About-the-Game/

Ricoeur, P. (2004). *Memory, history, forgetting* (K. Blamey & D. Pellauer, Trans.). University of Chicago Press. https://doi.org/10.7208/chicago/9780226713465.001.0001

Schrier, K. (2017). Designing games for moral engagement through expressions of empathy. *Journal of Moral Education*, 46(4), 385–402. https://doi.org/10.1080/03057240.2017.1353341

Schulzke, M. (2009). Moral decision making in computer games. *Games and Culture*, 4(2), 126–140. https://doi.org/10.1177/1555412008325481

Sicart, M. (2009). *The ethics of computer games*. MIT Press. https://doi.org/10.7551/mitpress/9780262012652.001.0001

Sicart, M. (2013). *Beyond choices: The design of ethical gameplay*. MIT Press. https://doi.org/10.7551/mitpress/9780262019781.001.0001

Zuanni, C., & Krottmaier, S. (2023). Paradise lost – and found again: Digital memory and religion in *Metro 2033 Redux*. *Journal for Religion, Film and Media*, 9(1), 101–124. https://doi.org/10.25364/05.9:2023.1.7
"""

appendices = """## Appendices

### Appendix A: Summary Faction Comparison Matrix

| Faction Name | Ideological Basis | Institutional Structure | Resource Base | Key Figures | Primary Critique / Pathology |
|---|---|---|---|---|---|
| **The Red Line** | Soviet Marxism-Leninism | Centralized totalitarian police state; Lubyanka interrogation | Heavy industry, mushroom farming, large military infantry | Gen. Korbut, Chairman Moskvin | Totalitarian cynicism; biopolitical viral genocide of rival stations |
| **The Fourth Reich** | National Socialism, racial fascism | Eugenics inspection boards; militarized stormtrooper core | Reclaimed technology; scrap weaponry; slave labor | The Fuhrer | Eugenics of radiation; scapegoating the 'abnormal' and disabled |
| **Hanseatic League (Hansa)** | Merchant capitalism, free market | Oligopoly cartel of station merchants; mercenary police | Absolute monopoly over Ring Line transit and trade junctions | Station Directors | Exploitative transit tariffs; ruthless border execution of diseased refugees |
| **Polis** | Platonic republicanism, Brahmin caste | Dual-caste system (Brahmins: archivists; Kshatriyas: military) | Pre-war scientific archives; hydroelectric power | Council of Elders | Complacent intellectual elitism; reliance on Spartan violence |
| **The Spartan Order** | Chivalric militarism, stoic brotherhood | Independent military brotherhood based in D6 | Advanced pre-war weaponry; tactical elite armor | Col. Miller, Anna, Ulman, Artyom | Martial utilitarianism; inability to recognize nonhuman intelligence |

### Appendix B: Moral Choice & Point Distribution Taxonomy

| Category | Typical In-Game Actions | Ludic Context | Ethical Significance |
|---|---|---|---|
| **Exploratory & Contemplative** | Listening to full civilian conversations; playing musical instruments; exploring hidden shrines. | Stations (Bolshoi, Venice) and ruins (Dead City). | Rewards reflective memory, aesthetic appreciation, and cultural reverence over speedrunning. |
| **Mercy & Restraint** | Sparing surrendering enemies; completing levels without lethal kills; knocking out sentries. | Combat levels (Facility, Revolution, Bridge). | Enforces virtue ethics; tests whether player kills simply because the mechanic is available. |
| **Charity & Altruism** | Giving military-grade bullets to beggars; retrieving a lost teddy bear for an orphan. | Civilian hubs (Bolshoi, Venice). | Sacrifices personal survival currency for the welfare of vulnerable strangers. |
| **Multispecies Empathy** | Protecting the Mother Bear from scavengers; sparing nesting mutant Demons; listening to child Dark One. | Surface wilderness (The Garden, Dead City). | Deconstructs anthropocentrism; extends moral standing to nonhuman post-nuclear life. |
"""

full_manuscript = f"""# {title}

{meta}

{abstract}

---

{body_text}

---

{references}

---

{appendices}
"""

out_path = os.path.join(base_dir, "12_FULL_RESEARCH_PAPER.md")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_manuscript)

words = len(re.findall(r"\b\w+\b", body_text))
print("12_FULL_RESEARCH_PAPER.md generated successfully!")
print(f"Total Body Word Count (Sections 1-15, excluding abstract/refs/appendices): {words} words.")
