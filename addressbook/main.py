import sqlite3

exit = False

conn = sqlite3.connect("addressbook/addressbook.db")
cur = conn.cursor()

#Line below creates the table.
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
    cur.execute("DELETE FROM contacts WHERE name=?", (name,)) #Comma after variable is necessary.
    print(f"Contact '{name}' deleted successfully.")
    conn.commit()


while not exit:
    print("Welcome to the addressbook, enter your command here. type 'help' for help.")
    userinput = input("- ")
    if(userinput == "help"):
        print("- add   |   Add a new contact to the addressbook.")
        print("- del   |   Remove contacts from addressbook.")
        print("- get   |   Get contacts from addressbook.")
    elif(userinput == "add"):
        name = input("Contact's name: ")
        phone = input("Contact's phone number: ")
        email = input("Contact's email address: ")
        address = input("Contact's address: ")
        city = input("Contact's city: ")
        create_contact(name, phone, email, address, city)
        conn.commit()
        
    elif(userinput == "get"):
        res = cur.execute("SELECT * FROM contacts")
        x = res.fetchall()
        print("")
        print("----------------------All Contacts--------------------")
        for i in x:
            #snap hiet nog niets van. :D
            formatted_line = '{:<12} {:<15} {:<10}'.format(i[1], i[2], i[3])
            print(formatted_line)
        print("--------------------End of Contacts--------------------")
        print("")
    elif(userinput == "del"):
        
        name = input("Enter contacts name to delete the contact: ")
        remove_contact(name)
        conn.commit()

    elif(userinput == 'x'):
        conn.close()
        exit = True
    else:
        print(f"Command '{userinput} does not exist.")