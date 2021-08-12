from flask import Flask
# application object made of Flask object with name of the module used here.
app = Flask(__name__)

# Directly links this index function output to the homepage i.e. the index page as notad by the /
# This essentially is rendering "Views" from django

@app.route('/')
def index():
    return "<h1>Hellow lil man!</h1>"
# This is a basic example of routing other than the index. Note the different function name.
@app.route('/testing')
def testing():
    return "<h1>Hellow lil man! You made it to the test page. </h1>"
# return a simple html string at the index page.

# Dynamic routing
# Will be unique for every unique name passed into the function.
# Requires passed in variable, and a parameter passed into the function
@app.route('/testing/<name>')
def other_page(name):
    return 'user: {}'.format(name)

# Variables can be altered after being passed into the function.
# def other_page(name):
#     return 'user: {}'.format(name.upper())


# For testing Debug
# def other_page(name):
#     return '100th letter in name: {}'.format(name[100]

if __name__ == '__main__':
    app.run()
    # Debug mode
    # Flask runs in NON-DEBUG mode as default
    # Console options are available with the PIN provided at the beginning of the error output. 
    # app.run(debug=True)
