from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    breed = StringField('What breed is the puppy?',validators=[DataRequired()])
    neutered = BooleanField('Has the puppy been neutered?')

    moods = [('mood_one','Happy'),('mood_two','Excited')]
    mood = RadioField('Please choose dog mood:',choices=moods)

    foods = [('chi','Chicken'),('bf','Beef'),('hm','Ham')]
    #  lowercase U (u) in the below line is to notate 'unicode' format some browsers require.
    food = SelectField(u"Pick dog's favorite food:",choices=foods)

    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])

def index():
    form = InfoForm()

    if form.validate_on_submit():
        # Flashes a user the following message.
        flash('Thanks you for submitting data.')

        # Session data is server stored.
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data

        # How to pass in a form data point and send it into a flash.
        flash(f"Your entered breed was: {session['breed']}")
        # For the method of returning a following page after successful POST
        return redirect(url_for('thank_you'))

    return render_template('index.html',form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
