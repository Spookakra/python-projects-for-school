
def add():
    name = input('Name: ')
    number = input('Number: ')

    with open('Mini Projects\contact book\contacts.txt', 'a') as f:
        f.write(name + "|" + number + "\n")

def view():
    with open('Mini Projects\contact book\contacts.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, number = data.split("|")
            print("Name:", name, "| Number:", number)



while True:
    mode = input("Would you like to 'add' a new contact or 'view' existing ones, press q to quit? ").lower()
    
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

#all i need is ctrl c and ctrl v
#python file opening modes ig:
    #w is "write" create or orveride a file
    #r "read mode" reads a file 
    #a "apend mode" allows you to add to the end of a file or create a new file if it does not exist if it does you can write and read it
    #rb "read/bites mode" read bits or sum idk thats what the guy said