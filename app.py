from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    name = ""
    return render_template("about.html",name = name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
