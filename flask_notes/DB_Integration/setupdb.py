from flask_sql import db, Puppy


db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Franky',2)

# Not added as of yet
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])
db.session.commit()

# Prints id after added into the db
print(sam.id)
print(frank.id)
