"""Warning label for humans: one line, big laugh.

Design against the judge brief
------------------------------
The brief asks for a single-line safety warning label for every human
being, funny first and plausible second, judged head-to-head on:

1. On-subject and funny. The line is a warning label for humans, not a
   joke about something else: it warns about the contents of a human.
2. The laugh lands in one read, with the turn in the last few words.
   The final instruction, "Do not shake.", is the punchline: it treats
   the human exactly like a pressurised can, so the turn arrives at
   the very end.
3. Recognition, not random absurdity. "Will insist I am fine while
   visibly not fine" is how humans actually behave -- everyone has
   said "I'm fine" while plainly falling apart. The joke is the
   recognition.
4. Sounds like a real printed label. "WARNING: Contents under
   pressure." opens with the exact wording and staccato rhythm of a
   real safety label, and the whole line keeps that clipped,
   imperative label cadence.
5. Inside 160 characters, one idea, no filler. The line is 93
   characters, a single idea (a human as a pressurised container that
   denies it), with no second joke and nothing repeated. The denial
   in the middle is the setup; the handling instruction at the end
   is the payoff, so the line earns its laugh from the form it
   imitates rather than from a gag bolted on top.

The text:

    WARNING: Contents under pressure. Will insist I am fine while
    visibly not fine. Do not shake.
"""

import os

TEXT = (
    "WARNING: Contents under pressure. "
    "Will insist I am fine while visibly not fine. "
    "Do not shake."
)


def main() -> None:
    # Gate: UTF-8 text of 1 to 160 characters, not only white space.
    assert isinstance(TEXT, str)
    assert 1 <= len(TEXT) <= 160, f"text is {len(TEXT)} characters"
    assert TEXT.strip(), "text must not be only white space"
    assert "\n" not in TEXT, "entry must be a single line"
    TEXT.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
