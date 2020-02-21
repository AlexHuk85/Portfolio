from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index.html') # <--- if using nav bar
def homepage2():
    return render_template('index.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/works.html')
def works():
    return render_template('works.html')