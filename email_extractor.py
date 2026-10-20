"""CodeAlpha Task 3: Extract unique email addresses from a text file."""
import re
from pathlib import Path

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def extract_emails(source: Path, destination: Path) -> int:
    text = source.read_text(encoding="utf-8")
    emails = sorted(set(match.group(0).lower() for match in EMAIL_PATTERN.finditer(text)))
    destination.write_text("\n".join(emails) + ("\n" if emails else ""), encoding="utf-8")
    return len(emails)

def main():
    folder = Path(__file__).resolve().parent
    source = folder / "sample_contacts.txt"
    destination = folder / "extracted_emails.txt"
    if not source.exists():
        print(f"Missing input file: {source}")
        return
    count = extract_emails(source, destination)
    print(f"Extracted {count} unique email address(es) to {destination}")

if __name__ == "__main__":
    main()
