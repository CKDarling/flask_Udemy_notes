from flask import Blueprint, render_template, redirect, url_for
from myproject import database
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies',__name__,template_folder='templates/puppies')
@puppies_blueprint.route('/')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@puppies_blueprint.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        database.session.add(Puppy(form.name.data))
        database.session.commit()

        return redirect(url_for("list"))
    return render_template('add.html',form=form)

@puppies_blueprint.route('/delete',methods=['GET','POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        pup = Puppy.query.get(form.id.data)
        database.session.delete(pup)
        database.session.commit()

        return redirect(url_for('list'))
    return render_template('delete.html',form=form)
