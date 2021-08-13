from myproject import database

class Puppy(database.Model):

    __tablename__ = 'puppies'

    id = database.Column(database.Integer,primary_key=True)
    name = database.Column(database.Text)
    owner = database.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy name is {self.name} and owner is {self.owner.name}.'

        else:
            return f'Puppy name is {self.name} and has no owner.'

class Owner(database.Model):

    __tablename__ = 'owners'

    id = database.Column(database.Integer,primary_key=True)
    name = database.Column(database.Text)
    puppy_id = database.Column(database.Integer,database.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner name is: {self.name} and owns puppy id {self.puppy_id}'
