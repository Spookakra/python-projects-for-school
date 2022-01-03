
def add():
    name = input('Name: ')
    number = input("Number: ")

    with open('work in progress\contact book\contacts.txt', 'a') as f:
        f.write(name + "|" + number + "\n")

def view():
    with open('work in progress\contact book\contacts.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, number = data.split("|")
            print("Name:", name, "| Number:", number)






while True:
    mode = input("Would you like to 'add' a new contact or view existing ones, press q to quit? ").lower()
    
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
