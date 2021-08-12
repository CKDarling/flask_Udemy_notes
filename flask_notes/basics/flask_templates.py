from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    # Function name
    some_var = 'Kinkade'
    some_second_var = 47


    a_list = [1,2,3,4,5]
    # return render_template('basic_template.html')
    # kwargs value can be anything, flask knows youre passing variables.
    return render_template('built_in_functions.html',variables = [some_var,some_second_var],
                                                     dict_variables={'var_1':some_var,'var_2':some_second_var},
                                                     loop_list=a_list,
                                                     user_logged_in = False)


if __name__ == '__main__':
    app.run(debug=True)
