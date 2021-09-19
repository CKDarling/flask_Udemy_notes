

# Process is simple for both libraries.
# Create a password, hash password, store the hash, check the hash when user logs in with password. 

from flask_bcrypt import Bcrypt
print('Bcrypt\n---------------------------------------------------------------')
bcrypt = Bcrypt()

password = 'supersecretpassword47'

hashed_pwd = bcrypt.generate_password_hash(password)

print(password)
print(hashed_pwd)


check = bcrypt.check_password_hash(hashed_pwd,'wrongpwd')
print(check)


check = bcrypt.check_password_hash(hashed_pwd,'supersecretpassword47')
print(check)


print('Werkzeug\n---------------------------------------------------------------')
from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('supersecretpassword47')

print(hashed_pass)

check = check_password_hash(hashed_pass,'notcorrectpwd')
print(check)

check = check_password_hash(hashed_pass,'supersecretpassword47')
print(check)
