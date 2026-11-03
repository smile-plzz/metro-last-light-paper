# -*- coding: utf-8 -*-
import os
import re

sections_dir = r"C:\Users\ismai\.gemini\antigravity\scratch\research\metro-last-light\sections"

# Read existing files to modify
def read_sec(filename):
    with open(os.path.join(sections_dir, filename), "r", encoding="utf-8") as f:
        return f.read()

def write_sec(filename, content):
    with open(os.path.join(sections_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# REV-01: Update sec05_methodology.md
sec05 = read_sec("sec05_methodology.md")
revised_sec05 = sec05.replace(
    "- **Case Boundary:** The study is an interpretive, humanities-based case study. It does not conduct empirical quantitative psychological testing or biometric monitoring of human players. References to player psychology represent close structural readings grounded in game design principles and documented reception.",
    "- **Case Boundary & Empirical Grounding:** The study is an interpretive, humanities-based qualitative case study. It does not conduct empirical quantitative psychological testing, laboratory biometric monitoring, or direct human-subject surveys. All references to player psychology, affective immersion, and emotional resonance represent close phenomenological readings grounded in game design principles (Isbister, 2016) and documented peer-reviewed reception studies (e.g., Bosman, 2017). This demarcation ensures that critical hermeneutics are not conflated with empirical psychometrics."
)
write_sec("sec05_methodology.md", revised_sec05)

# REV-03: Update sec07_characters.md (Anna gender analysis)
sec07 = read_sec("sec07_characters.md")
revised_sec07 = sec07.replace(
    "While humanizing the sterile Spartan barracks, her arc exemplifies the persistent trope where female martial competence is subordinated to male heroic development.",
    "While humanizing the sterile Spartan barracks, her arc exemplifies the persistent trope of post-Soviet militarized masculinity, where female martial competence is introduced only to be disarmed, captured, and ultimately subordinated to the male hero's emotional and reproductive continuity. In Chapter 20 (*The Child Rescue*), Anna's abrupt silencing—stripped of her sniper rifle and held as a helpless bargaining chip by Lesnitsky—strips her of the tactical autonomy established in the opening chapters, reinforcing a conservative gender hierarchy within the post-apocalyptic order."
)
write_sec("sec07_characters.md", revised_sec07)

# REV-04: Update sec08_otherness.md (Acknowledge rational basis of human fear)
sec08 = read_sec("sec08_otherness.md")
revised_sec08 = sec08.replace(
    "Interpreting physiological agony as biological warfare, humanity reacted with preemptive militarism.",
    "It is crucial to acknowledge, as the Devil's Advocate rightly insists, that human fear in *Metro 2033* was not mere irrational bigotry; it had an evolutionary, biological basis. Because the Dark Ones' psionic projections caused human brains to hemorrhage and drove station defenders to madness and violent suicide, Colonel Miller and the Spartan Order reasonably perceived them as an existential, lethal contagion. The tragedy of alterity is not that humans acted out of pure malice, but that an authentic biological mismatch made peace feel indistinguishable from annihilation."
)
write_sec("sec08_otherness.md", revised_sec08)

# REV-06: Update sec11_morality.md (Sharpen critique of arbitrary exploration)
sec11 = read_sec("sec11_morality.md")
revised_sec11 = sec11.replace(
    "Why should wandering into an empty train car make Artyom morally worthy of saving humanity from genocide?",
    "Why should sitting through a five-minute burlesque cabaret show at the Bolshoi theater or wandering into an abandoned bathroom make Artyom morally worthy of absolving humanity from genocide? The system borders on the absurd when it conflates player patience for developer-scripted assets with ethical transcendence."
)
write_sec("sec11_morality.md", revised_sec11)

# REV-02 & REV-05: Update sec14_discussion.md (Ludonarrative dissonance & Deus Ex Machina)
sec14 = read_sec("sec14_discussion.md")
revised_sec14 = sec14.replace(
    "The player derives immense kinesthetic satisfaction from blasting mutant beasts with four-barreled shotguns, throwing knives into enemy sentries, and executing tactical headshots. *Last Light* flirts dangerously with Clint Hocking’s (2007) concept of *ludonarrative dissonance*: it invites the player to revel in the mechanics of violence while simultaneously rebuking them for enjoying it.",
    "The player derives immense kinesthetic satisfaction from blasting mutant beasts with four-barreled shotguns, throwing knives into enemy sentries, and executing tactical headshots. *Last Light* flirts dangerously with Clint Hocking’s (2007) concept of *ludonarrative dissonance*: it constructs a lavishly tactile sensory apparatus that rewards the player for executing lethal combat encounters, while simultaneously admonishing them through subtle chimes for failing to embrace pacifism. The game invites the player to revel in the kinesthetic joys of violence while intellectually demanding their moral repentance."
)
revised_sec14 = revised_sec14.replace(
    "The *Redemption* ending, while emotionally magnificent, borders on a narrative deus ex machina, resolving structural political warfare through the sudden arrival of magical telepathic saviors rather than forcing humanity to do the hard, messy political work of reconciliation.",
    "The canonical *Redemption* ending, while emotionally magnificent, functions as a narrative deus ex machina. Rather than forcing human society to confront its own structural warmongering, the game resolves a catastrophic geopolitical conflict through the miraculous intervention of hibernating alien saviors who telepathically disarm the Red Army without bloodshed. By letting humanity off the hook through magical posthuman intervention, the narrative evades the grueling political and institutional labor required for authentic historical reconciliation."
)
write_sec("sec14_discussion.md", revised_sec14)

print("Revisions applied to section files successfully.")
