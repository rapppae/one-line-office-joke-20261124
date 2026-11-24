"""Write the office joke to /output/entry.txt.

One line, 120 characters (limit 200) -- no trailing newline.
The kind of line you send a colleague after a meeting that should
have been an email.
"""

from pathlib import Path

ENTRY = "Our daily standup is fifteen minutes because that is exactly how long it takes to explain why nothing shipped yesterday."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
