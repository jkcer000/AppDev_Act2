from flask import Flask, render_template, request

app = Flask(__name__)

# Sample news data
news_data = [
    {"title": "AI is changing the world", "category": "Tech"},
    {"title": "New iPhone released", "category": "Tech"},
    {"title": "NBA Finals highlights", "category": "Sports"},
    {"title": "Olympics 2026 updates", "category": "Sports"},
]

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

    return render_template("home.html", news=news_data, response=response)


@app.route("/category/<name>")
def category(name):
    filtered_news = [n for n in news_data if n["category"].lower() == name.lower()]
    return render_template("category.html", news=filtered_news, category=name)


if __name__ == "__main__":
    app.run(debug=True)
