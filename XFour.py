from flask import Flask, render_template, request

app = Flask(__name__)

history = []

@app.route("/")
def home():
    return render_template("hub.html")

@app.route("/index", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            q = request.form.get("type")
            if q == "two":
                num1 = float(request.form["num1"])
                num2 = float(request.form["num2"])
                op = request.form["op1"]

                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        error = "Cannot divide by zero."
                    else:
                        result = num1 / num2
                else:
                    error = "Invalid operator."
                
                if result is not None and error is None:
                    entry = f"{num1} {op} {num2} = {result}"
                    history.append(entry)

            elif q == "three":
                num1 = float(request.form["num1"])
                num2 = float(request.form["num2"])
                num3 = float(request.form["num3"])
                op1 = request.form["op1"]
                op2 = request.form.get("op2")

                if op2:
                    if op1 == "+":
                        temp = num1 + num2
                    elif op1 == "-":
                        temp = num1 - num2
                    elif op1 == "*":
                        temp = num1 * num2
                    elif op1 == "/":
                        if num2 == 0:
                            error = "Cannot divide by zero."
                        else:
                            temp = num1 / num2

                    if error is None:
                        if op2 == "+":
                            result = temp + num3
                        elif op2 == "-":
                            result = temp - num3
                        elif op2 == "*":
                            result = temp * num3
                        elif op2 == "/":
                            if num3 == 0:
                                error = "Cannot divide by zero."
                            else:
                                result = temp / num3
                        else:
                            error = "Invalid second operator"

                    if result is not None and error is None:
                        entry = f"{num1} {op1} {num2} {op2} {num3} = {result}"
                        history.append(entry)
                else:
                    if op1 == "+":
                        result = num1 + num2 + num3
                    elif op1 == "-":
                        result = num1 - num2 - num3
                    elif op1 == "*":
                        result = num1 * num2 * num3
                    elif op1 == "/":
                        if num2 == 0 or num3 == 0:
                            error = "Cannot divide by zero."
                        else:
                            result = num1 / num2 / num3
                    else:
                        error = "Invalid operator"

                    if result is not None and error is None:
                        entry = f"{num1} {op1} {num2} {num3} = {result}"
                        history.append(entry)

        except Exception as e:
            error = "Error: " + str(e)

    return render_template("index.html", result=result, error=error, history=history)

@app.route("/rpgfront", methods=["GET", "POST"])
def rpgfront():
    output = ""
    
    if request.method == "POST":
        name = request.form.get("name", "Player")
        choice1 = request.form.get("choice1", "")
        choice2 = request.form.get("choice2", "")
        choice3 = request.form.get("choice3", "")

        output += f"Welcome to your adventure, {name}!<br><br>"

        if choice1 == "1":
            output += "--- World: Tutorial Area ---<br>"
            output += f"{name}: HP 100, Stamina 50<br>Master Terry: HP 100, Stamina 50<br><br>"

            if choice2 == "1":
                output += f"{name} threw a ball and dealt 45 damage!<br>"
                output += "Terry used Focus + Ball Throw, dealt 60 damage.<br>"
                output += f"{name}: HP 40, Stamina 45<br>Master Terry: HP 55, Stamina 30<br>"
            elif choice2 == "2":
                output += f"{name} used Focus + Ball Throw and dealt 60 damage!<br>"
                output += "Terry did the same. Both have HP 40, Stamina 30.<br>"
            else:
                output += "Invalid move selection.<br>"

            if choice3 == "1":
                output += f"{name} used Ball Throw and dealt 45 damage!<br>"
                output += "Terry had 40 HP and collapsed. 🎉<br>"
                output += f"🎊 Congratulations {name}, you beat Terry! 🎊<br>"
            elif choice3 == "2":
                output += f"{name} used Focus + Ball Throw and dealt 60 damage!<br>"
                output += "Terry had 40 HP and collapsed. 💥<br>"
                output += f"🎉 {name} is victorious over Terry! 🎉<br>"

            output += "<br><strong>Final battle coming soon!</strong>"

        elif choice1 == "2":
            output += "Skipping tutorial... update coming soon!"
        else:
            output += "Invalid choice for tutorial."

    return render_template("rpgfront.html", output=output)
@app.route("/daily", methods=["GET", "POST"])
def daily():
    questions = [
        {
            "question": "What is the output of print(7 ** 5)?",
            "options": ["45", "46", "81", "49"],
            "answer": "45"
        },
        {
            "question": " how to make an if condition?",
            "options": ["if:code", "if rule:code", "f rule:code", "else rule:code"],
            "answer": "def"
        },
        {
            "question": "What type are variables by default?",
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


@app.route("/learnpython")
def learnpython():
    return render_template("learnpython.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/patch.notes")
def patch_notes():
    return render_template("patch.html")

if __name__ == "__main__":
    app.run()
