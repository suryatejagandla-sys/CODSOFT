# Contact Book (CLI) - stores contacts in contacts.json
import json, os
FILE = os.path.join(os.path.dirname(__file__), "contacts.json")

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE,"r") as f:
        return json.load(f)

def save(lst):
    with open(FILE,"w") as f:
        json.dump(lst,f,indent=2)

def list_contacts(lst):
    if not lst:
        print("No contacts.")
        return
    for i,c in enumerate(lst,1):
        print(f"{i}. {c.get('name')} - {c.get('phone')} - {c.get('email','')}")

def add_contact(lst):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    addr = input("Address (optional): ").strip()
    lst.append({"name":name,"phone":phone,"email":email,"address":addr})
    save(lst)
    print("Added.")

def search(lst):
    q = input("Search by name or phone: ").strip().lower()
    res = [c for c in lst if q in c.get('name','').lower() or q in c.get('phone','')]
    if not res:
        print("No results.")
        return
    for c in res:
        print(c)

def update_contact(lst):
    list_contacts(lst)
    try:
        i = int(input("Contact number to update: "))
        c = lst[i-1]
        print("Leave blank to keep current value.")
        name = input(f"Name [{c.get('name')}]: ").strip() or c.get('name')
        phone = input(f"Phone [{c.get('phone')}]: ").strip() or c.get('phone')
        email = input(f"Email [{c.get('email','')}]: ").strip() or c.get('email')
        addr = input(f"Address [{c.get('address','')}]: ").strip() or c.get('address')
        lst[i-1] = {"name":name,"phone":phone,"email":email,"address":addr}
        save(lst)
        print("Updated.")
    except Exception as e:
        print("Invalid selection.", e)

def delete_contact(lst):
    list_contacts(lst)
    try:
        i = int(input("Contact number to delete: "))
        lst.pop(i-1)
        save(lst)
        print("Deleted.")
    except Exception as e:
        print("Invalid selection.", e)

def menu():
    lst = load()
    while True:
        print("\nContact Book - Menu")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Search")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        c = input("Choice: ").strip()
        if c == '1':
            list_contacts(lst)
        elif c == '2':
            add_contact(lst)
        elif c == '3':
            search(lst)
        elif c == '4':
            update_contact(lst)
        elif c == '5':
            delete_contact(lst)
        elif c == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    menu()
