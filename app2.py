from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/rpgfront", methods=["GET", "POST"])
def rpg():
    output = ""
    
    if request.method == "POST":
        name = request.form.get("name", "Player")
        choice1 = request.form.get("choice1", "")
        choice2 = request.form.get("choice2", "")

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

            output += "<br><strong>Final battle coming soon!</strong>"

        elif choice1 == "2":
            output += "Skipping tutorial... update coming soon!"
        else:
            output += "Invalid choice for tutorial."

    return render_template("rpgfront.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
