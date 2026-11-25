"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one 100-word monologue to /output/entry.txt.
The Dark Lord is not defeated. He is just... putting things off.

Verified: exactly 100 words, under 600 characters, deterministic output.
"""

import os

MONOLOGUE = (
    "The hero's sword is still stuck in my floor. "
    "Fourteen years now. "
    "I keep meaning to pull it out, tomorrow, maybe, when the rain stops. "
    "My generals want a war. "
    "My war room wants a map. "
    "My map wants a coastline that no longer exists, because I moved it. "
    "I moved it twice, actually. "
    "The second time was spite. "
    "The kettle has boiled dry again. "
    "I can hear it ticking. "
    "Outside, the banners flap for a battle I scheduled last spring and keep "
    "rescheduling, like a dentist appointment. "
    "Let them come. "
    "The door is open. "
    "The sword is still there."
)


def main() -> None:
    words = MONOLOGUE.split()
    assert len(words) == 100, f"expected 100 words, got {len(words)}"
    assert 1 <= len(MONOLOGUE) <= 600, f"expected 1-600 chars, got {len(MONOLOGUE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
