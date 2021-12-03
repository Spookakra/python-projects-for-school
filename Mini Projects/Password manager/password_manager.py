#lasspass2
from cryptography.fernet import Fernet

'''
#create a key file named "key.key"
def write_key():
    key = Fernet.generate_key()
    with open("Key.key", "wb") as key_file:
        key_file.write(key)'''
    
#loads the key file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("What is the master password?")
#encryption 😏

key = load_key() + master_pwd.encode()
fer = Fernet(key)



#view existing passwords
def view():
    with open('passwords.txt', 'r') as f:  
        for line in f.readlines():
            data = (line.rstrip())
            user , passw = data.split("|")
            print("User:", user, "| Password:", 
            str(fer.decrypt(passw.encode())))

    

#add new passwords
def add():
    name = input('account name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:  
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones(view, add)?, Press q to quit").lower()
    if mode == "q":
        break
#ifthen
#select the mode
    if mode == "view":
        view()
    elif mode == "add":
        add()  

    else: 
        print("Invalid Mode.")
        continue

#python file opening modes ig 
#w is "write" create or orveride a file
#r "read mode" reads a file 
#a "apend mode" allows you to add to the end of a file or create a new file if it does not exist if it does you can write and read it
#rb "read/bites mode" read bits or sum idk thats what the guy said