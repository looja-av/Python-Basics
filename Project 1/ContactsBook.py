# import json

# FILENAME="contact.json"

# def load_contacts():
#     try:
#         with open(FILENAME,"r") as file:
#             return json.load(file)
        
#     except(FileNotFoundError,json.JSONDecodeError):
#         return{}
    
# def save_contacts(contacts):
#     with open(FILENAME,"w") as file:
#         json.dump(contacts, file, indent=4)

# def add_contact(contacts):
#     name=input("Enter name:")
#     phone=input("Enter phone num")
#     email=input("Enter email address")

#     contacts[name]={"phone": phone, "email": email}
#     save_contacts(contacts)
#     print("☑️Contact added successsfully")

# def view_contacts(contacts):
#     if not contacts:
#         print("👎NO contacts found! ")
#         return
    
#     print("\n Contact list:")
#     for name, info in contacts.items():
#         print(f"{name}-{info['phone']} | {info['email']}")

# def search_contact(contacts):
#     query= input("Enter name or phone number to search:")

#     for name, info in contacts.items():
#         if query.lower() in name.lower() or query in info["phone"]:
#             print(f"\n☑️ Found:{name}- 📞{info['phone']} | {info['email']} ")
#             return
        
#     print("Contacts not found!")

# def update_contact(contacts):
#     name= input("Enter the name of the contacts to update:")

#     if name in contacts:
#         print(f"Current details: 📞 {contacts[name]['phone']} | ✉️ {contacts[name]['email']}")
#         new_phone = input("Enter new phone number (or press Enter to keep current): ")
#         new_email = input("Enter new email (or press Enter to keep current): ")

#         if new_phone:
#             contacts[name]["phone"] = new_phone
#         if new_email:
#             contacts[name]["email"] = new_email

#         save_contacts(contacts)
#         print("✅ Contact updated successfully!")
#     else:
#         print("❌ Contact not found!")

# def delete_contact(contacts):
#     name = input("Enter the name of the contact to delete: ")

#     if name in contacts:
#         del contacts[name]
#         save_contacts(contacts)
#         print("✅ Contact deleted successfully!")
#     else:
#         print("❌ Contact not found!")

# def main():
#     contacts= load_contacts()

#     while True:
#         print("\n Contact Book Menu:")
#         print("1. Add Contacts")
#         print("2.View Contacts")
#         print("3. Search Contact")
#         print("4.Update Contact")
#         print("5. Delete Contact")
#         print("6. Exit")

#         choice=input("Choose an option:")

#         if choice =="1":
#             add_contact(contacts)

#         elif choice=="2":
#             view_contacts(contacts)

#         elif choice=="3":
#             search_contact(contacts)

#         elif choice=="4":
#             update_contact(contacts)

#         elif choice=="5":
#             delete_contact(contacts)

#         elif choice=="6":
#             print("Existing.. Have a great day")
#             break

#         else:
#             print("Invalid chocie! Tryagain")

# if __name__ == "__main__":
#     main()


import json
FILENAME= "contacts.json"

def load_contacts():
    try:
        with open(FILENAME,"r") as file:
            return json.load(file)
        
    except(FileNotFoundError, json.JSONDecodeError):
        return{}
    
def save_contacts(contacts):
    with open(FILENAME,"w") as file:
        json.dump(contacts,file, indent=4)

def add_contacts(contacts):
    name=input("Enter your name")
    phone=input("Enter phone number:")
    email=input("Enter your email")

    contacts[name]={"Phone":phone, "email":email}
    save_contacts(contacts)
    print("Contacts added successfully")

def view_contacts(contacts):
    if not contacts:
        print("X= No contacts found!")
        return
    
    print("\n Contact List:")
    for name, info in contacts.items():
        print(f"{name}- {info['phone']} | {info["email"]}")

def search_contacts(contacts):
    query=input("Enter name or phone number to search")

    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info["phone"]:
            print(f"\n Found:{name} - {info['phone']} | {info['email']}")
            return
        
    print("Contacts not found!")

def update_contact(contacts):
    name=input("Enter the name of the contact to update:")

    if name in contacts:
        print(f"Current Details: {contacts[name]['phone']} | {contacts[name]['email']}")
        new_phone= input("Enter new phone  number")
        new_email=input("Enter new email")

        if new_phone:
            contacts[name]["phone"] = new_phone
        if new_email:
            contacts[name]["email"]= new_email

        save_contacts(contacts)
        print("Contacts saved succesfully")
    else:
        print("No contacts found")

def delete_contact(contacts):
    name=print("Enter the name of the contact to delete:")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contacts deleted successfully")
    else:
        print("contact not found!")

def main():
    contacts=load_contacts()
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

    


    








