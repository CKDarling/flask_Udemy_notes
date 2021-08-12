from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():

    return render_template('base.html')
@app.route('/test')
def other_page():
    return render_template('test_inheritance.html')

if __name__ == '__main__':
    app.run(debug=True)
