from flask import Flask, request, redirect, render_template
import jinja2
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


@app.route("/")
def index():
    template = jinja_env.get_template('register.html')
    return render_template('register.html')

@app.route("/register.html", methods=['POST'])
def greeting():
    first_name = request.form['first_name']
    
    return render_template('home.html', name=first_name)

if __name__ == '__main__':
    app.run()