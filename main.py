import os

# One emoji, one smile: heart hands (U+1FAF6) — a small gesture of care.
# Warm at first glance, readable by any stranger, and chosen rather than
# the default smiley: two hands shaping a heart says "I wish you well"
# without a word, a face, or any intimacy a stranger would misread.
EMOJI = "\U0001FAF6"


def main():
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 8 characters,
    # not only white space. Fail loudly here rather than ship an invalid file.
    assert 1 <= len(EMOJI) <= 8 and not EMOJI.isspace(), "emoji fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
