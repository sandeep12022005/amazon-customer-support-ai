from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

BASE_DIR = Path(__file__).resolve().parent.parent
KB = BASE_DIR / "knowledge_base"

styles = getSampleStyleSheet()

for folder in KB.iterdir():

    if not folder.is_dir():
        continue

    for md_file in folder.glob("*.md"):

        pdf_path = md_file.with_suffix(".pdf")

        doc = SimpleDocTemplate(str(pdf_path))

        story = []

        text = md_file.read_text(encoding="utf-8")

        for line in text.split("\n"):

            line = line.strip()

            if line == "":
                continue

            story.append(Paragraph(line, styles["BodyText"]))

        doc.build(story)

        print(f"Created {pdf_path.name}")

print("\nAll PDFs Created Successfully.")