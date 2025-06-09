from user import User

users=[User(1, "Krystian",'krystian123!'), User(2, "Waldemar","waldek321@"), User(3,"Piotr","piotrek312#")]
username_table={u.username: u for u in users}
userid_table={u.id: u for u in users}
def authenticate(username, password):
    user=username_table.get(username)
    if user and user.password == password:
        return user
    else:
        return None

def identity(payload):
    user_id=payload['identity']
    return userid_table.get(user_id)
    
    