from user import User

users = [User(1,'Jose','Password'),
         User(2,'Kinkade','Password')
        ]

user_table = {u.username: u for u in users}

user_id_table = {u.id: u for u in users}

def auth(username,password):
    # Check if exists, return users
    user = user_table.get(username,None)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return user_id_table.get(user_id,None)
