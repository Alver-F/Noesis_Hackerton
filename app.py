from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/rights')
def rightspage():
    return render_template('rights.html')

@app.route('/councelling')
def councellingpage():
    return render_template('councelling.html')

@app.route('/courses')
def coursespage():
    return render_template('courses.html')

#test



if '__main__' == __name__:
    app.run(debug=True, port=5000)


