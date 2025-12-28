SUMMARY_PROMPT = """
Summarize the document clearly for students.

Rules:
- No equations
- No model parameters
- No research methodology
- Simple language

Limit: 150–180 words

Text:
{text}
"""


MCQ_PROMPT = """
You are an expert exam question setter.

Generate exactly {n} multiple-choice questions.

Difficulty level: {difficulty}

Difficulty rules:
- Easy: basic definitions and direct facts
- Medium: conceptual understanding and applications
- Hard: reasoning-based, deeper understanding

STRICT OUTPUT FORMAT (ONLY THIS):

Q1. Question
A. Option
B. Option
C. Option
D. Option
Correct Answer: A

Content:
{text}
"""


LEARNING_GUIDE_PROMPT = """
Create a clean learning guide.

Format strictly as:
1. Key Concepts
2. Recommended Research Papers
3. Books
4. YouTube Channels
5. Suggested Learning Roadmap

Text:
{text}
"""
