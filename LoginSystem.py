


#make a log in system

def add_user():
    with open('Guest.txt', 'a') as file_object:
            name = input("whats your name?")
            password = input("whats your password?")
            if len(password) <= 3:
                print("password too short. try again")
                add_user()
            else:
                pass
            user = f"{name};{password}"
            print("\nregistered")
            file_object.write(f"{user}\n")


def login():
    with open('Guest.txt') as file_object:
        name = input("enter your username")
        password = input("enter your password")
        signin = f"{name};{password}"
        if signin in file_object.read():
            print("logged in")
        else:
            make_new_user_question()

def make_new_user_question():
    print("user not found. like to make a new account?")
    answer = input("")
    if answer.lower() == "yes":
        add_user()
    else:
        print("goodbye")
        quit()

login()






