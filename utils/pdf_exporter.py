from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_quiz_pdf(quiz, path="quiz.pdf"):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    y = height - 50

    for i, q in enumerate(quiz, start=1):
        c.drawString(40, y, f"{i}. {q['question']}")
        y -= 20

        for key, opt in q["options"].items():
            c.drawString(60, y, f"{key}. {opt}")
            y -= 15

        y -= 20
        if y < 100:
            c.showPage()
            y = height - 50

    c.save()
    return path
