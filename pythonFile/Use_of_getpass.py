import getpass

passwd = getpass.getpass('Password: ')

if passwd == "Urvashi":
    print("You are authenticated")
else:
    print("You are not authenticated")