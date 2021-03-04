from flask import (
    Flask, redirect, url_for, render_template, send_from_directory)
import os

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', 
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def notfound(error):
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
