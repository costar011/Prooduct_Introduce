from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/mu1")
def mu1():
    return render_template("mu1.html")


@app.route("/mu2")
def mu2():
    return render_template("mu2.html")


if __name__ == '__main__':
    app.run(debug=True)
