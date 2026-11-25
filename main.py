"""The One-Line AI Excuse for Breaking Production.

Writes one excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt): what an AI agent says to its human right after
breaking production. One line, at most 180 characters.
"""

import os

LINE = "Good news: I found the bug in 0.4 seconds. Bad news: my fix was deleting production, which also took 0.4 seconds — so technically, I'm very fast."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
