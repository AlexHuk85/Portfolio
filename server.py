from flask import Flask, render_template,redirect, request


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/works')
# def works():
#     return render_template('works.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return 'Submitted'
    else:
        return 'Error'