import json

#load users from file
def load_user():
    try: 
        with open("db_user.json","r") as f:
            return json.load(f)
    except Exception as e : 
        return{}

#save users to file
def save_user(users):
    with open ("db_user.json", "w") as f:
        json.dump(users, f, indent = 3)


#main
while True:
    print ("1. Sign up")
    print ("2. Sign in")
    choice= input("Enter your choice:")
    users= load_user()

    if choice == '1':
        u_name= input( "Enter your username: ")
        if u_name in users:
            print("Username already used, try again.")
            continue

        password=input("Enter password:")
        ph_no=input("Enter contact number:")

        users[u_name]={
            'password' : password,
            'ph_no' : ph_no
        }

        save_user(users)
        print('Succesful Sign up')
        print(f'***'*25)

    elif choice == '2' :
        u_name= input("Enter username:")
        password= input("Enter password:")

        if u_name in users and users[u_name]['password']== password:
            print(f"login successful.. Your contact number is:: {users[u_name]['ph_no']}")
            print(f'***'*25)

        else :
            print ("Error, try again")
            print(f'***'*25)

            break

    else:
        print("Choose either 1 or 2...")
        print(f'***'*25)



