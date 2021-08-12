from flask_sql import db, Puppy

## CREATE
add_puppy = Puppy('Rufus',5)
db.session.add(add_puppy)
db.session.commit()

## READ
all_puppies = Puppy.query.all() # list of puppy objects
for i in all_puppies:
    print(i)

## SELECT (By ID)

puppy_one = Puppy.query.get(1)

## FILTER
query_string = Puppy.query.filter_by(name='Franky')
print(query_string.all())

## UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age = 10

db.session.add(first_puppy)
db.session.commit()

## DELETE

puppy = Puppy.query.get(2)
db.session.delete(puppy)
db.session.commit


## READ
all_puppies = Puppy.query.all() # list of puppy objects
for i in all_puppies:
    print(i)
