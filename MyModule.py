# Function to register a new user
def register_user(usernames, passwords):
    username = input("Enter a username: ")
    if username in usernames:
        print("Username already taken!")
    else:
        password = input("Enter a password: ")
        usernames.append(username)
        passwords.append(password)
        print(f"User {username} registered successfully!")

# Function to login a user
def login_user(usernames, passwords):
    username = input("Enter your username: ")
    if username not in usernames:
        print("Username not found!")
    else:
        password = input("Enter your password: ")
        index = usernames.index(username)
        if passwords[index] == password:
            print(f"Welcome {username}!")
        else:
            print("Incorrect password!")

# Function to change a user's username or password
def change_credentials(usernames, passwords):
    username = input("Enter your username to change your details: ")
    if username not in usernames:
        print("Username not found!")
    else:
        new_username = input("Enter new username (or press Enter to keep the same): ")
        if new_username:
            usernames[usernames.index(username)] = new_username
            username = new_username
        new_password = input("Enter new password (or press Enter to keep the same): ")
        if new_password:
            passwords[usernames.index(username)] = new_password
        print(f"Details for {username} updated successfully!")

# Function to recover a forgotten password
def recover_password(usernames, passwords):
    username = input("Enter your username to recover your password: ")
    if username not in usernames:
        print("Username not found!")
    else:
        index = usernames.index(username)
        print(f"Your password is: {passwords[index]}")

