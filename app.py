# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blogs')
def blog():
    return render_template('blogs.html')

@app.route('/about')
def course():
    return render_template('about.html')

@app.route('/courses')
def about():
    return render_template('course.html')

if __name__ == '__main__':
    app.run(debug=True)
