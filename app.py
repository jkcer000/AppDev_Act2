from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]

        if "news" in user_input.lower():
            response = "Here are today's top headlines (sample)"
        elif "person" in user_input.lower():
            response = "Here is what's happening with that person (sample)"
        else:
            response = "I don't understand yet."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
