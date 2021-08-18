from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/project.html')
def project():
    return render_template("project.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


app.run()