from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hub.html")

# Include any other routes here (like /about, /daily, etc.)
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/learnpython")
def learnpython():
    return render_template("learnpython.html")
@app.route("/daily")
def daily():
    return render_template("daily.html")
@app.route("/rpgfront")
def rpgfront():
    return render_template("rpgfront.html")
if __name__ == "__main__":
    app.run()
