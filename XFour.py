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
                if choice3 == "1":
                 output += f"{name} used Ball Throw and dealt 45 damage!<br>"
                 output += f"Terry now has 10 HP ,He used Focus+Ball Throw and dealt 60 dmg {name} had 40 HP and ended up with under 0 {name} lost<br>"
                 output += f"Game over {name} x_x<br>"
                elif choice3 == "2":
                 output += f"{name} used Focus + Ball Throw and dealt 60 damage!<br>"
                 output += "Terry had 55 HP and collapsed. 💥<br>"
                 output += f"🎉 {name} is victorious over Terry! 🎉<br>"
            elif choice2 == "2":
                output += f"{name} used Focus + Ball Throw and dealt 60 damage!<br>"
                output += "Terry did the same. Both have HP 40, Stamina 30.<br>"
                if choice3 == "1":
                 output += f"{name} used Ball Throw and dealt 45 damage!<br>"
                 output += "Terry had 40 HP and collapsed. 🎉<br>"
                 output += f"🎊 Congratulations {name}, you beat Terry! 🎊<br>"
            elif choice3 == "2":
                 output += f"{name} used Focus + Ball Throw and dealt 60 damage!<br>"
                 output += "Terry had 40 HP and collapsed. 💥<br>"
                 output += f"🎉 {name} is victorious over Terry! 🎉<br>"
            else:
                output += "Invalid move selection.<br>"


            output += "<a href=""/rpgwone"
            "><button>Go to starter place</button></a>"
            

        elif choice1 == "2":
            output += "Skipping tutorial.. <a href="/"><button>Go to starter place</button></a>"
        else:
            output += "Invalid choice for tutorial."

    return render_template("rpgfront.html", output=output)
@app.route("/rpgwone", methods=["GET", "POST"])
def rpgwone():
    output = ""
    if request.method == "POST":
        Choice1 = request.form.get("choice1", "")
        Choice2 = request.form.get("choice2", "")
        output += "This is a serious fight. Your attacks have to be good."
        output += "Player stats: 150 HP 70 Stamina. phrase: I am unstoppable"
        output += "Enemy stats: 150 HP 70 Stamina. You wont get to my king."
        if Choice1 == 1:
            output += "Player used slash and dealt 75 damge"
            output += "Enemy used Focus+Slash(stone sword) and dealt 120 damge"
            output += "Player stats: 30 HP 70 stamina. you will see Enemy stats: 75 HP 55 Stamina. LOSER You wont get to my king"
            if Choice2 == 1:
                output += "Player used slash and dealt 75 damge"
                output += "Enemy had 75 HP,ended up with 0 and died "
                output += "Well that was Easy Earned:weapons:stone sword abilities: Parry"
                output += "Stay tuned more stuff soon."
            elif Choice2 == 2:
                output += "Player used Focus+slash and dealt 90 damge"
                output += "Enemy had 75 HP,ended up with less than 0 and died "
                output += "Well that was Easy Earned:weapons:stone sword abilities: Parry"
                output += "Stay tuned more stuff soon."
            elif Choice2 == 3:
                output += "Player used Ball Throw and dealt 45 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) "
                output += "Player had 30 HP and ended up with less than 0 Player collapsed"
                output += "Game over x_x"
            elif Choice2 == 4:
                output += "Player used Focus+Ball Throw and dealt 60 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) and dealt 120 damge "
                output += "Player had 30 HP and ended up with less than 0 Player collapsed"
                output += "Game over x_x"            
        elif Choice1 == 2:
            output += "Player used Focus+Slash and dealt 90 damge"
            output += "Enemy used Focus+Slash(stone sword) and dealt 120 damge"
            output += "Player stats: 30 HP 55 stamina. you will see Enemy stats: 60 HP 55 Stamina. LOSER You wont get to my king"
            if Choice2 == 1:
                output += "Player used slash and dealt 75 damge"
                output += "Enemy had 60 HP,ended up with less than 0 and died "
                output += "Well that was Easy Earned:weapons:stone sword abilities: Parry"
                output += "Stay tuned more stuff soon."
            elif Choice2 == 2:
                output += "Player used Focus+Slash and dealt 90 damge"
                output += "Enemy had 60 HP,ended up with less than 0 and died "
                output += "Well that was Easy Earned:weapons:stone sword abilities: Parry"
                output += "Stay tuned more stuff soon."
            elif Choice2 == 3:
                output += "Player used Ball Throw and dealt 45 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) "
                output += "Player had 30 HP and ended up with less than 0 Player collapsed"
                output += "Game over x_x"
            elif Choice2 == 4:
                output += "Player used Focus+Ball Throw and dealt 60 damge"
                output += "Enemy had 60 HP,ended up with 0 and died "
                output += "Well that was easy Earned:weapons:Stone Sword abilities: Parry"
                output += "Stay tuned more stuff soon." 
            elif Choice1 == 3:
             output += "Player used Ball Throw and dealt 45 damge"
             output += "Enemy used Focus+Slash(stone sword) and dealt 120 damge"
             output += "Player stats: 30 HP 70 stamina. you will see Enemy stats: 105 HP 55 Stamina. LOSER You wont get to my king"
            if Choice2 == 1:
                output += "Player used slash and dealt 75 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) abd dealt 120 damge "
                output += "Player had 30 HP , ended up with 0 and died"
                output += "Game over x_x"
            elif Choice2 == 2:
                output += "Player used Focus+Slash and dealt 90 damge"
                output += "Enemy used Focus+Slash(Stone Sword) and dealt 120 damge "
                output += "Player had 30 HP,ended with less than 0 and died"
                output += "Game over x_x"
            elif Choice2 == 3:
                output += "Player used Ball Throw and dealt 45 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) "
                output += "Player had 30 HP and ended up with less than 0 Player collapsed"
                output += "Game over x_x"
            elif Choice2 == 4:
                output += "Player used Focus+Ball Throw and dealt 60 damge"
                output += "Enemy used Focus+Slash(Stone Sword) and dealt 120 damge "
                output += "Player had 30 HP ,ended with less than 0 and died"
                output += "Game over x_x"
            elif Choice1 == 4:
             output += "Player used Ball Throw and dealt 60 damge"
             output += "Enemy used Focus+Slash(stone sword) and dealt 120 damge"
             output += "Player stats: 30 HP 70 stamina. you will see Enemy stats: 90 HP 55 Stamina. LOSER You wont get to my king"
            if Choice2 == 1:
                output += "Player used slash and dealt 75 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) abd dealt 120 damge "
                output += "Player had 30 HP , ended up with 0 and died"
                output += "Game over x_x"
            elif Choice2 == 2:
                output += "Player used Focus+Slash and dealt 90 damge"
                output += "Enemy used Focus+Slash(Stone Sword) and dealt 120 damge "
                output += "Player had 30 HP,ended with less than 0 and died"
                output += "Game over x_x"
            elif Choice2 == 3:
                output += "Player used Ball Throw and dealt 45 damge"
                output += "Enemy Used Focus+Slash(Stone Sword) "
                output += "Player had 30 HP and ended up with less than 0 Player collapsed"
                output += "Game over x_x"
            elif Choice2 == 4:
                output += "Player used Focus+Ball Throw and dealt 60 damge"
                output += "Enemy used Focus+Slash(Stone Sword) and dealt 120 damge "
                output += "Player had 30 HP ,ended with less than 0 and died"
                output += "Game over x_x"
    return render_template("rpgwone.html", output=output)

@app.route("/daily", methods=["GET", "POST"])
def daily():
    questions = [
        {
            "question": "How to print the type of a variable",
            "options": ["print(type(x))", "print(x(type))", "print(x=type)", "print(xtype)"],
            "answer": "print(type(x))"
        },
        {
            "question": " how to make an else if?",
            "options": ["else if:code", "elif rule:code", "elseif rule:code", "else:code"],
            "answer": "elif rule:code"
        },
        {
            "question": "What is the string variable type?",
            "options": ["it is a type that represents words and typed like this x = 'anything here'", "it is a type that represents numbers and typed like x = any number here", "it is a type that is used to represent numbers entirely and typed like x = any number.any number from 0 to 9", ""],
            "answer": "it is a type that represents words and typed like this x = 'anything here'"
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

@app.route("/aboutm")
def aboutm():
    return render_template("mainabout.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/patch.notes")
def patch_notes():
    return render_template("patch.html")
@app.route("/mpatch.notes")
def patchnotesm():
    return render_template("mainpatch.html")

if __name__ == "__main__":
    app.run()
