from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.errorhandler(404)
def notfound():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
