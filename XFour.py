from flask import Flask, render_template, request
from markupsafe import Markup

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
                    output += f"Terry now has 10 HP. He used Focus + Ball Throw and dealt 60 damage. {name} had 40 HP and collapsed.<br>"
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
            output += '<a href="/rpgwone"><button>Go to next area</button></a>'
        elif choice1 == "2":
            output += 'Skipping tutorial.. <a href="/rpgwone"><button>Go to next area</button></a>'
        else:
            output += "Invalid choice for tutorial."
    return render_template("rpgfront.html", output=output, player_hp=30, enemy_hp=75)

@app.route("/rpgwone", methods=["GET", "POST"])
def rpgwone():
    output = ""
    if request.method == "POST":
        choice1 = request.form.get("choice1", "")
        choice2 = request.form.get("choice2", "")
        output += "This is a serious fight. Your attacks have to be good.<br>"
        output += "Player stats: 150 HP, 70 Stamina. Phrase: I am unstoppable.<br>"
        output += "Enemy stats: 150 HP, 70 Stamina. Phrase: You won't get to my king.<br><br>"
        if choice1 == "1":
            output += "Player used Slash and dealt 75 damage.<br>"
            output += "Enemy used Focus + Slash (Stone Sword) and dealt 120 damage.<br>"
            output += "Player stats: 30 HP, 70 Stamina<br>Enemy stats: 75 HP, 55 Stamina<br>"
        elif choice1 == "2":
            output += "Player used Focus + Slash and dealt 90 damage.<br>"
            output += "Enemy used Focus + Slash (Stone Sword) and dealt 120 damage.<br>"
            output += "Player stats: 30 HP, 55 Stamina<br>Enemy stats: 60 HP, 55 Stamina<br>"
        elif choice1 == "3":
            output += "Player used Ball Throw and dealt 45 damage.<br>"
            output += "Enemy used Focus + Slash (Stone Sword) and dealt 120 damage.<br>"
            output += "Player stats: 30 HP, 70 Stamina<br>Enemy stats: 105 HP, 55 Stamina<br>"
        elif choice1 == "4":
            output += "Player used Focus + Ball Throw and dealt 60 damage.<br>"
            output += "Enemy used Focus + Slash (Stone Sword) and dealt 120 damage.<br>"
            output += "Player stats: 30 HP, 70 Stamina<br>Enemy stats: 90 HP, 55 Stamina<br>"
        else:
            output += "Invalid first move.<br>"
            return render_template("rpgwone.html", output=output)
        if choice2 == "1":
            output += "Player used Slash and dealt 75 damage.<br>"
            output += "Enemy had low HP and died.<br>"
            output += "🏆 Earned: Weapon - Stone Sword | Ability - Parry<br>"
        elif choice2 == "2":
            output += "Player used Focus + Slash and dealt 90 damage.<br>"
            output += "Enemy had low HP and died.<br>"
            output += "🏆 Earned: Weapon - Stone Sword | Ability - Parry<br>"
        elif choice2 == "3":
            output += "Player used Ball Throw and dealt 45 damage.<br>"
            output += "Enemy used Focus + Slash and dealt 120 damage.<br>"
            output += "Player had 30 HP and collapsed. Game Over. x_x<br>"
        elif choice2 == "4":
            output += "Player used Focus + Ball Throw and dealt 60 damage.<br>"
            output += "Enemy used Focus + Slash and dealt 120 damage.<br>"
            output += "Player had 30 HP and collapsed. Game Over. x_x<br>"
        else:
            output += "Invalid second move.<br>"
    return render_template("rpgwone.html", output=output, player_hp=30, enemy_hp=75)

@app.route("/daily", methods=["GET", "POST"])
def daily():
    questions = [
        {
            "question": "How to print the type of a variable?",
            "options": ["print(type(x))", "print(x(type))", "print(x=type)", "print(xtype)"],
            "answer": "print(type(x))"
        },
        {
            "question": "How to make an else if?",
            "options": ["else if:code", "elif rule:code", "elseif rule:code", "else:code"],
            "answer": "elif rule:code"
        },
        {
            "question": "What is the string variable type?",
            "options": [
                "it is a type that represents words and typed like this x = 'anything here'",
                "it is a type that represents numbers and typed like x = any number here",
                "it is a type that is used to represent numbers entirely and typed like x = any number.any number from 0 to 9",
                ""
            ],
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

@app.route("/xchat", methods=["GET", "POST"])
def xchat():
    chat_log = []
    if request.method == "POST":
        user_message = request.form.get("message", "")
        if user_message:
            chat_log.append(f"You: {user_message}")
            response = generate_terry_response(user_message)
            chat_log.append(f"Master Terry: {response}")
    return render_template("xchat.html", chat_log=chat_log)

def generate_terry_response(message):
    message = message.lower()
    if "help" in message or "what can i do" in message:
        return "Stay focused. Your next move decides your fate."
    elif "Mate who is trick" in message:
        return "You shouldn't talk about him... he's no one. Definitely."
    elif "Tell me who is trick" in message:
        return "He is one... You will meet him in World 7. No more info!"
    elif "Terry what happened to jerry?" in message:
        return "He died fighting TRICK, lord of the unknown team."
    elif "I would like to talk with XLegend" in message:
        if "you are weak" in message:
            return "I shall banish you"
        return "Hello it's me. What do you want? One answer only."
    elif "xlegend" in message:
        return "You found an easter egg. Only my friends know XLegend!"
    elif "hello" in message:
        return "Greetings, warrior. Ready to train again?"
    elif "who are you" in message:
        return "I am Master Terry. Keeper of stones and secrets."
    elif "who is xlegend?" in message:
        return "He is the ALL powerful warrior. He fought aliens, demons, and more to keep your adventure alive."
    elif "tired" in message:
        return "Rest if you must. But victory waits for no one."
    else:
        return "Interesting... but I have no clue what you're talking about."
@app.route("/XLegend", methods=["POST", "GET"])
def XLegend():
    chat_log = []
    if request.method == "POST":
        user_message = request.form.get("message", "")
        if user_message:
            chat_log.append(f"You: {user_message}")
            response = generate(user_message)
            chat_log.append(f"XLegend: {response}")
    return render_template("xchatt.html", chat_log=chat_log)
def  generate(message):
    if "can i recommend adding something" in message:
        return "NO"
    elif "Hello" in message:
        return "Yo there is a chest in the castle grab it you will get smth OP"
    elif "can i fight you" in message:
        return "we will team up in world 9 for something cant tell you find out yourself"
    elif "why did you make this website" in message:
        return "to test my full potential in development"
    elif "can i friend you in roblox" in message:
        return "sure username:Adam1gamingzain displayname:XLegend"
    elif "monkey" in message:
        return "EASTER EGG B.A.D INCOMING"
    elif "BAD incoming" in message:
        return "I CAN FEEL MY TRUE PHASE AWAKENING NOW I SHALL KILL YOU (sends DTDS) HELLO WOULD YOU LIKE TO DIE"
    elif "how do i defend bads and dtds" in message:
        return "SKILL ISSUE DETECTED. DTDS INCOMING BAD INCOMING"
    elif "can you leak something" in message:
        return "next tool in update 2.0 imagine saying that to an AI version of the dev"
    elif "." in message:
        return "? u good? should i dial 911 XD"
    elif "who is trick" in message:
        return "he is the leader of the so called 'unknown gang' but i have enough power to stop the whole rpg universe i'll deal with em later i guess" 
    elif "who are you" in message:
        return "I am Adam the dev himself dont expose me if i find out ur banned from my website"  
    elif "what are you" in message:
        return "a monke gamer"
    elif "show it" in message.lower():
        return Markup('<a href="/book"><button>Xlegends book</button></a>')
    else:
        return "i forgot to program myself to answer to this (sorry)"
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    result = None
    if request.method == 'POST':
        answers = {
            'q1': 'c',
            'q2': 'a',
            'q3': 'b',
            'q4': 'c'
        }

        score = 0
        for key in answers:
            if request.form.get(key) == answers[key]:
                score += 1

        result = f"You got {score}/4 correct! {'🐵 MONKEY LEGEND' if score == 4 else 'Keep grinding!'}"

    return render_template("monke.html", result=result)
     
     
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
@app.route("/book")
def book():
    return render_template("book.html")


if __name__ == "__main__":
    app.run()
