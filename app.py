from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/header")
def hedaer():
    return render_template("hedaer.html")


@app.route("/footer")
def footer():
    return render_template("footer.html")


app.run(debug=True)
