from routing import find_route


while True:
    print("""
        yeki az 2ta kar zir ra anjam bedeh:
            1. login ---> 1 ro bezan
            2. register ---> 2 ro bezan
    """)
    act = int(input("your selection: "))
    if act == 1:
        login_func = find_route("login")
        if login_func:
            email = input("emaileto bezan: ")
            passw = input("passeto bezan: ")
            login_func(email, passw)
        else:
            print("chenin routi nadarim")
    elif act == 2:
        register_func = find_route("register")
        if register_func:
            email = input("emaileto bezan: ")
            print(register_func(email))
        else:
            print("chenin routi nadarim")
    else:
        print("cheshato va kon. faghat 1 va 2")
