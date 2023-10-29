from flask import Flask, url_for,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/id/<name>")
def hello_world(name=None):
    return render_template('hello.html', name=name)
