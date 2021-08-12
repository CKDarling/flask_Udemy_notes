from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    # grabs name of the input
    username = request.args.get('username')

    uppers = [True for i in username if i.isupper()]
    downers = [True for i in username if i.islower()]
    last_letter = username[-1].isdigit()

    if (sum(uppers) > 0 and sum(downers) > 0 and last_letter):
        check = True
    else:
        check = False

    return render_template('success.html',username_check=check,username=username)


@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
