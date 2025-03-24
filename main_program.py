import MyModule

# Lists to store the usernames and passwords
usernames = []
passwords = []

# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Change Name or Password")
    print("4. Recover Forgotten Password")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        # Register a new user
        MyModule.register_user(usernames, passwords)
    elif choice == '2':
        # User login
        MyModule.login_user(usernames, passwords)
    elif choice == '3':
        # Change username or password
        MyModule.change_credentials(usernames, passwords)
    elif choice == '4':
        # Recover forgotten password
        MyModule.recover_password(usernames, passwords)
    elif choice == '5':
        print("Goodbye!")
        break  # Exit the loop and end the program
    else:
        print("Invalid choice, please try again.")
