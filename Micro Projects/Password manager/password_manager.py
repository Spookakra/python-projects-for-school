#lasspass2
from cryptography.fernet import Fernet

#create a key file named "key.key"
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

#loads the key file
def load_key():
    file = open("Mini Projects\Password manager\key.key", "rb")
    key = file.read()
    file.close()
    return key


#encryption 😏
key = load_key()
fer = Fernet(key)



#view existing passwords
def view():
    with open('Mini Projects\Password manager\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())



#add new passwords
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('Mini Projects\Password manager\passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



#ifthen
#select the mode
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

#python file opening modes ig 
#w is "write" create or orveride a file
#r "read mode" reads a file 
#a "apend mode" allows you to add to the end of a file or create a new file if it does not exist if it does you can write and read it
#rb "read/bites mode" read bits or sum idk thats what the guy said