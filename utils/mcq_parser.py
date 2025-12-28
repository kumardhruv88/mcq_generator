import re

def parse_mcqs(text):
    questions = []
    blocks = re.split(r"\nQ\d+\.", text)[1:]

    for block in blocks:
        lines = block.strip().split("\n")
        question = lines[0]
        options = {}
        correct = ""

        for line in lines[1:]:
            if line.startswith(("A.", "B.", "C.", "D.")):
                options[line[0]] = line[2:].strip()
            elif line.startswith("Correct Answer"):
                correct = line.split(":")[-1].strip()

        questions.append({
            "question": question,
            "options": options,
            "correct": correct
        })

    return questions
