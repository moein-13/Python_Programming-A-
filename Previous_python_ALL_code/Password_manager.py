master_pwd = input("What is the master password ? ")
def view ():
    with open ("passwords.txt" , "r") as file:
        for line in file.readlines():
            data = line.rstrip()   # strip is using for at the end extra space.
            user , passw = data.split("|")
            print("User :" , user , "password :", passw)

def add():
    name = input("Account name : ")
    pwd = input ("passwords : ")

    with open ("passwords.txt" , "a") as file :
        file.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new pass or view existing ones (view add ) , press q to quit.").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue


