from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/daily", methods=["GET", "POST"])
def daily():
    questions = [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["5", "6", "8", "9"],
            "answer": "8"
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["func", "def", "function", "lambda"],
            "answer": "def"
        },
        {
            "question": "What type does input() return by default?",
            "options": ["int", "str", "bool", "float"],
            "answer": "str"
        }
    ]

    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            user_answer = request.form.get(f"q{i}")
            if user_answer == q["answer"]:
                score += 1
        return render_template("daily.html", questions=questions, score=score)

    return render_template("daily.html", questions=questions)
