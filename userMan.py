users = {}

def add_user(username, password):
    if username in users:
        print(f"User '{username}' already exists.")
    else:
        if check_passwords(password):
            users[username] = password
            print(f"User '{username}' added.")

def delete_user(username,password):
    if username in users and users[username] == password:
        users.pop(username)
        print(f"User '{username}' deleted.")
    else:
        print(f"User '{username}' not found or Wrong password")

def change_password(username,password, new_password):
    if username in users and users[username] == password:
        if users[username] == new_password:
            print("New password must be different from the old password.")
        else:
            if check_passwords(new_password):
                users[username] = new_password
                print(f"Password for '{username}' changed.")
    else:
        print(f"User '{username}' not found or Wrong password")

def check_passwords(password):
    isWeak = (len(password) >= 6 and not password.isalpha())
    if not isWeak:
        print("Weak password")
    else:
        print("Password is secure.")
    return isWeak

while True:
    print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        u = input("Enter username: ")
        p = input("Enter password: ")
        add_user(u, p)
    elif choice == "2":
        u = input("Enter username: ")
        p = input("Enter password: ")
        delete_user(u,p)
    elif choice == "3":
        u = input("Enter username: ")
        p = input("Enter password: ")
        pNew = input("Enter new password: ")
        change_password(u, p,pNew)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
