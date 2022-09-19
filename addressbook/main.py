import sqlite3

exit = False

con = sqlite3.connect("addressbook/addressbook.db")
cur = con.cursor()
#cur.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name, phonenumber, email, address, city)")  

class Contact():
    def __init__(self, name, phone_number, email, address="", city=""):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        

def create_contact(name, phone_number, email, address="", city=""):
    #write to sql database
    cur.execute("INSERT INTO contacts (name, phonenumber, email, address, city) VALUES (?, ?, ?, ?, ?)", (name, phone_number, email, address, city))
    print("Contact created successfully")

def remove_contact(name):
    #delete func
    cur.execute("DELETE FROM contacts WHERE name = ?", (name))
    print(f"Contact '{name}' deleted successfully.")


while not exit:
    print("Welcome to the addressbook, enter your command here. type 'help' for help.")
    userinput = input("- ")
    if(userinput == "help"):
        print("- add   |   Add a new contact to the addressbook.")
        print("- get   |   Get contacts from addressbook.")
    elif(userinput == "add"):
        name = input("Contact's name: ")
        phone = input("Contact's phone number: ")
        email = input("Contact's email address: ")
        address = input("Contact's address: ")
        city = input("Contact's city: ")
        create_contact(name, phone, email, address, city)
        con.commit()
        
    elif(userinput == "get"):
        res = cur.execute("SELECT * FROM contacts")
        x = res.fetchall()
        for i in x:
            print(f"{i[1]} - {i[2]} - {i[3]}")
    elif(userinput == "del"):
        
        name = input("Enter contacts name to delete the contact: ")
        remove_contact(name)
        con.commit()

    elif(userinput == 'x'):
        con.close()
        exit = True
    else:
        print(f"Command '{userinput} does not exist.")
