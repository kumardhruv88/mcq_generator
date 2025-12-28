from flask import Flask, render_template, request, send_file
import os

from groq_client import call_groq
from prompts import SUMMARY_PROMPT, MCQ_PROMPT, LEARNING_GUIDE_PROMPT
from utils.pdf_reader import read_pdf
from utils.mcq_parser import parse_mcqs
from utils.pdf_exporter import export_quiz_pdf

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

LAST_QUIZ = []

@app.route("/", methods=["GET", "POST"])
def index():
    global LAST_QUIZ
    summary = guide = quiz = None

    if request.method == "POST":
        num_questions = int(request.form["num_questions"])
        difficulty = request.form["difficulty"]
        text = ""

        if "pdf" in request.files and request.files["pdf"].filename != "":
            pdf = request.files["pdf"]
            path = os.path.join(UPLOAD_FOLDER, pdf.filename)
            pdf.save(path)
            text = read_pdf(path)
        else:
            text = request.form.get("text")

        summary = call_groq(SUMMARY_PROMPT.format(text=text))

        mcq_text = call_groq(
            MCQ_PROMPT.format(
                text=text,
                n=num_questions,
                difficulty=difficulty
            )
        )

        guide = call_groq(LEARNING_GUIDE_PROMPT.format(text=text))

        quiz = parse_mcqs(mcq_text)
        LAST_QUIZ = quiz

    return render_template(
        "index.html",
        summary=summary,
        quiz=quiz,
        guide=guide
    )

@app.route("/export", methods=["POST"])
def export():
    path = export_quiz_pdf(LAST_QUIZ)
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
