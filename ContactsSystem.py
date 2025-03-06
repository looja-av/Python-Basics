import json

Filename="contacts.json"

def load_contacts():
    try:
        with open(Filename,"r") as file:
            return json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        return{}
    
def save_contacts(contacts):
    with open(Filename,"w") as file:
        json.dump(contacts,file, indent=4 )

def add_contacts(contacts):
    name=input("ENter name:")
    phone=input("Enter phonenumber")
    email=input("Enter email")

    contacts[name]={"phone":phone,"email":email}
    save_contacts(contacts)
    print("Contacts added successfully😁")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available")
        return
    
    print("Contacts List")
    for name,info in contacts.items():
        print(f"{name}- {info['phone']} | {info['email']}")

def search_contacts(contacts):
    query=input("Enter the name and contacts of the person")

    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info["phone"]:
            print(f"\n Found🤝:{name}- {info['phone']} | {info['email']}")
            return
    
    print("Contatcs nott found")

def update_contact(contacts):
    name=input("Enter the contacts name, you wanna update")

    if name in contacts:
        print(" Current details: {contacts[name]['phone']} | {contacts[name]['email']}")
        new_phone=input("Enter the new phone contact details (or keep the usual one and click enter)")
        new_email=input("Enter the new email or click enter to continue with the same one")

        if new_phone:
            contacts[name]["phone"]=new_phone
        if new_email:
            contacts[name]["email"]=new_email

        save_contacts(contacts)
        print("Contacts updated successfully")

    else:
        print("Contact not found!")

def delete_contact(contacts):
    name=input("Enter the name of the user you wanna delete")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("The contact is successfully deleted")

    else:
        print("Contacs not found!")

def main():
    contacts= load_contacts()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contacts")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice=input("Choose an option:")

        if choice=="1":
            add_contacts(contacts)
        elif choice=="2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("🚀 Exiting... Have a great day!")
            break
        else:
            print("Invalid user input")

if __name__=="__main__":
    main()

    


    







