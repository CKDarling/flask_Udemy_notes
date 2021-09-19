from flask import Flask
from flask_restful import Resource, Api
from auth import identity, auth
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

api = Api(app)
jwt = JWT(app,auth,identity)


# Models.py
#########################################

class Puppy(db.Model):
    name = db.Column(db.String(80),primary_key = True)

    def __init__(self,name):
        self.name = name

    def json(self):

        # Required with API data
        return {'name':self.name}


#########################################

puppies = []

class PuppyNames(Resource):

    def get(self, name):
        # for pup in puppies:
        #     if pup['name'] ==name:
        #         return pup

        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()

        else:
            return {'none':None},404

    def post(self,name):
        # pup = {'name':name}
        # puppies.append(pup)
        # return pup

        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()

        return pup.json()


    def delete(self,name):
        # for ind, pup in enumerate(puppies):
        #     if pup['name'] == name:
        #         deleted_pup = puppies.pop(ind)
        #
        pup = Puppy.query.filter_by(name=name).first()

        db.session.delete(pup)
        db.session.commit()
        return {'note':'delete success'}

class AllNames(Resource):

    # @jwt_required() # Simply add the decorator to

    def get(self):
        # return {'puppies':puppies}
        puppies = Puppy.query.all()

        return [pup.json() for pup in puppies]



api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')


if __name__ == '__main__':
    app.run(debug=True)
