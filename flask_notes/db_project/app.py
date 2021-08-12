import os
from forms import AddForm, DelForm, AddOwner, DelOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'test'
# Setup DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    # 1:1
    # one puppy to one owner
    # Uselist is set to false due to single relationship
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy name is {self.name} and owner is {self.owner.name}.'

        else:
            return f'Puppy name is {self.name} and has no owner.'

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner name is: {self.name} and owns puppy id {self.puppy_id}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_owner',methods=['GET','POST'])
def add_owner():
    form = AddOwner()
    if form.validate_on_submit():
        db.session.add(Owner(form.name.data,form.puppy_id.data))
        db.session.commit()

        return redirect(url_for('list_owner'))
    return render_template('add_owner.html',form=form)

@app.route('/owners')
def list_owner():
    owners = Owner.query.all()
    return render_template('list_owner.html',owners=owners)

@app.route('/delete_owner',methods=['GET','POST'])
def del_owner():
    pass
    form = DelOwnerForm()
    if form.validate_on_submit():
        owner = Owner.query.get(form.id.data)
        db.session.delete(owner)
        db.session.commit()

        return redirect(url_for('list_owner'))

    return render_template('delete_owner.html',form=form)

@app.route('/puppies')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)


@app.route('/add_pup',methods=['GET','POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        db.session.add(Puppy(form.name.data))
        db.session.commit()

        return redirect(url_for("list_pup"))

    return render_template('add.html',form=form)

@app.route('/delete_pup',methods=['GET','POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        pup = Puppy.query.get(form.id.data)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
