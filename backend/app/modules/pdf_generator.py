from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(text, filename="analysis_report.pdf"):

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 10))

    pdf = SimpleDocTemplate(filename)

    pdf.build(story)

    return filename