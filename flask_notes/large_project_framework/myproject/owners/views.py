from flask import Blueprint, render_template, redirect, url_for
from myproject import database
from myproject.models import Owner
from myproject.owners.forms import AddForm, DelForm

owners_blueprint = Blueprint('owners',__name__,template_folder='templates/owners')
@owners_blueprint.route('/')
def list():
    owners = Owner.query.all()
    return render_template('list_owner.html',owners=owners)

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        database.session.add(Owner(form.name.data,form.puppy_id.data))
        database.session.commit()

        return redirect(url_for('owners.list'))
    return render_template('add_owner.html',form=form)

@owners_blueprint.route('/delete',methods=['GET','POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        owner = Owner.query.get(form.id.data)
        database.session.delete(owner)
        database.session.commit()

        return redirect(url_for('owners.list'))
    return render_template('delete_owner.html',form=form)
