from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'


class InfoForm(FlaskForm):

    breed = StringField("What Breed is the Dog?")
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    breed = False
    form = InfoForm()

    if form.validate_on_submit():

        #form.attribute_of_form.data
        breed = form.breed.data
        form.breed.data = ''

    return render_template('form_home.html',form=form,breed=breed)


if __name__ == '__main__':
    app.run(debug=True)
