from models import User, ConcreteFood1, ConcreteFood2, ConcreteFood3, Restaurant

users = []
product = {}  # {'id': objectFood}


def register(email):
    for user in users:
        if user.email == email:
            print("bache zerang!! khodeti. ma hamchin useri darim. boro login kon")
            return
    user = User(email)
    users.append(user)
    return f"your pass: {user.passw}.savesh kon"


def authenticate(email, passw):
    for user in users:
        if user.email == email:
            if str(user.passw) == str(passw):
                return user
    return False


def login(email, passw):
    valid_user = authenticate(email, passw)
    if valid_user:
        print("welcome!")
        return valid_user
    print("yechizi ro eshteb zadi")
    return None
