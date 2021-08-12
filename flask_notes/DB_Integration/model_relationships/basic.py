# create db table entries

from models import db, Puppy,Toy,Owner

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())


rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)


kinkade = Owner('Kinkade',rufus.id)

toy1 = Toy('ball',rufus.id)
toy2 = Toy('Chewy Bone',rufus.id)

db.session.add_all([kinkade,toy1,toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()

print(rufus)

print(rufus.report_toys())
