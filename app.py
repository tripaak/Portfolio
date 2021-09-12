from flask import Flask, render_template


app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html"), 200


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/project.html')
def project():
    return render_template("project.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=False)