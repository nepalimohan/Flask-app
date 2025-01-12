from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return "Hello, Flask!"
    return render_template('index.html')

@app.route('/about')
def about():
    return "About Page"

@app.route('/contact')
def contact():
    return "contact Page"



if __name__ == '__main__':
    app.run(debug=True)