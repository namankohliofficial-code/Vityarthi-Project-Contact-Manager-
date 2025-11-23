"""
Contact Book Manager
A simple contact management system for storing and organizing contacts

Created by: Naman Kohli
Registration: 25BAI10865
Course: Introduction to Python Programming
Date: November 2025
"""

import json
import os
import re
from datetime import datetime

# file where contacts will be saved
CONTACTS_FILE = 'contacts.json'

contacts = []  # this will store all the contacts


def clear_screen():
    """clears the terminal screen"""
    # works differently on windows vs mac/linux
    if os.name == 'nt':
        os.system('cls')  # windows
    else:
        os.system('clear')  # mac/linux


def load_contacts():
    """Load contacts from the json file when program starts"""
    global contacts

    try:
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, 'r') as f:
                contacts = json.load(f)
            print(f"Loaded {len(contacts)} contact(s) from file")
        else:
            print("No saved contacts found. Starting fresh!")
            contacts = []
    except:
        # if something goes wrong just start with empty list
        print("Couldn't load contacts. Starting with empty list.")
        contacts = []


def save_contacts():
    """saves all contacts to json file"""
    try:
        with open(CONTACTS_FILE, 'w') as f:
            json.dump(contacts, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False


# validates phone number
def validate_phone(phone):
    # remove all the formatting stuff like spaces, dashes, etc
    clean = re.sub(r'[\s\-\(\)\+]', '', phone)

    # check if its at least 10 digits
    if len(clean) >= 10 and clean.isdigit():
        return True
    else:
        return False


def validate_email(email):
    """check if email looks valid"""
    if not email:  # email is optional so empty is ok
        return True

    # basic email pattern - has to have @ and a dot
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    return False


def check_duplicate(phone, current_id=None):
    """check if phone already exists in contacts"""
    for contact in contacts:
        # skip current contact when editing
        if contact['phone'] == phone and contact['id'] != current_id:
            return True
    return False


def get_new_id():
    """generate new id for contact"""
    if len(contacts) == 0:
        return 1
    # find max id and add 1
    max_id = 0
    for c in contacts:
        if c['id'] > max_id:
            max_id = c['id']
    return max_id + 1


def add_contact():
    """add a new contact to the list"""
    print("\n" + "="*50)
    print("ADD NEW CONTACT")
    print("="*50)

    # get contact info from user
    name = input("Enter name (required): ").strip()
    if not name:
        print("Error: Name is required!")
        input("\nPress Enter to continue...")
        return

    phone = input("Enter phone number (required): ").strip()
    if not phone:
        print("Error: Phone number is required!")
        input("\nPress Enter to continue...")
        return

    # validate phone
    if not validate_phone(phone):
        print("Error: Phone number must have at least 10 digits")
        input("\nPress Enter to continue...")
        return

    # check duplicate
    if check_duplicate(phone):
        print("Error: This phone number already exists!")
        input("\nPress Enter to continue...")
        return

    email = input("Enter email (optional, press Enter to skip): ").strip()
    if email:  # only validate if they entered something
        if not validate_email(email):
            print("Error: Email format is invalid")
            input("\nPress Enter to continue...")
            return

    # category selection
    print("\nSelect category:")
    print("1. Family")
    print("2. Friends")
    print("3. Work")
    print("4. Other")
    cat = input("Enter choice (1-4): ").strip()

    # convert number to category name
    if cat == '1':
        category = 'Family'
    elif cat == '2':
        category = 'Friends'
    elif cat == '3':
        category = 'Work'
    elif cat == '4':
        category = 'Other'
    else:
        category = 'Other'  # default

    address = input("Enter address (optional, press Enter to skip): ").strip()
    notes = input("Enter notes (optional, press Enter to skip): ").strip()

    # create the contact dict
    new_contact = {
        'id': get_new_id(),
        'name': name,
        'phone': phone,
        'email': email,
        'category': category,
        'address': address,
        'notes': notes,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    contacts.append(new_contact)

    # save to file
    if save_contacts():
        print(f"\nSuccess! Added {name} to contacts")
    else:
        print("\nAdded to list but couldn't save to file")

    input("\nPress Enter to continue...")


def view_all():
    """show all contacts in alphabetical order"""
    clear_screen()

    if len(contacts) == 0:
        print("\n" + "="*50)
        print("No contacts yet!")
        print("="*50)
        input("\nPress Enter to continue...")
        return

    print("\n" + "="*50)
    print(f"ALL CONTACTS (Total: {len(contacts)})")
    print("="*50)

    # sort by name
    sorted_list = sorted(contacts, key=lambda x: x['name'].lower())

    # display each contact
    count = 1
    for contact in sorted_list:
        print(f"\n[{count}] {contact['name']}")
        print(f"    Phone: {contact['phone']}")

        if contact['email']:
            print(f"    Email: {contact['email']}")

        print(f"    Category: {contact['category']}")

        if contact['address']:
            print(f"    Address: {contact['address']}")

        if contact['notes']:
            print(f"    Notes: {contact['notes']}")

        print(f"    Added on: {contact['created_at']}")
        print("-" * 50)
        count += 1

    input("\nPress Enter to continue...")


def search_contacts():
    """search for contacts by name, phone or email"""
    clear_screen()
    print("\n" + "="*50)
    print("SEARCH CONTACTS")
    print("="*50)

    search_term = input("\nEnter search term: ").strip().lower()

    if not search_term:
        print("Please enter something to search")
        input("\nPress Enter to continue...")
        return

    # find matches
    results = []
    for c in contacts:
        # check in name, phone, and email
        if search_term in c['name'].lower():
            results.append(c)
        elif search_term in c['phone']:
            results.append(c)
        elif c['email'] and search_term in c['email'].lower():
            results.append(c)

    if len(results) == 0:
        print(f"\nNo contacts found matching '{search_term}'")
        input("\nPress Enter to continue...")
        return

    print(f"\nFound {len(results)} contact(s):")
    print("="*50)

    for i, contact in enumerate(results, 1):
        print(f"\n[{i}] {contact['name']}")
        print(f"    Phone: {contact['phone']}")
        if contact['email']:
            print(f"    Email: {contact['email']}")
        print(f"    Category: {contact['category']}")
        if contact['address']:
            print(f"    Address: {contact['address']}")
        if contact['notes']:
            print(f"    Notes: {contact['notes']}")
        print("-" * 50)

    input("\nPress Enter to continue...")


def filter_by_category():
    """show contacts from specific category only"""
    clear_screen()
    print("\n" + "="*50)
    print("FILTER BY CATEGORY")
    print("="*50)

    print("\nSelect category:")
    print("1. Family")
    print("2. Friends")
    print("3. Work")
    print("4. Other")

    choice = input("\nEnter choice (1-4): ").strip()

    # map choice to category
    category_map = {
        '1': 'Family',
        '2': 'Friends',
        '3': 'Work',
        '4': 'Other'
    }

    if choice not in category_map:
        print("Invalid choice!")
        input("\nPress Enter to continue...")
        return

    selected_category = category_map[choice]

    # filter contacts
    filtered = []
    for c in contacts:
        if c['category'] == selected_category:
            filtered.append(c)

    if len(filtered) == 0:
        print(f"\nNo contacts in '{selected_category}' category")
        input("\nPress Enter to continue...")
        return

    print(f"\nShowing {len(filtered)} contact(s) in '{selected_category}':")
    print("="*50)

    # sort and display
    filtered_sorted = sorted(filtered, key=lambda x: x['name'].lower())

    for idx, contact in enumerate(filtered_sorted, 1):
        print(f"\n[{idx}] {contact['name']}")
        print(f"    Phone: {contact['phone']}")
        if contact['email']:
            print(f"    Email: {contact['email']}")
        if contact['address']:
            print(f"    Address: {contact['address']}")
        if contact['notes']:
            print(f"    Notes: {contact['notes']}")
        print("-" * 50)

    input("\nPress Enter to continue...")


def edit_contact():
    """edit an existing contact's information"""
    clear_screen()

    if len(contacts) == 0:
        print("\nNo contacts to edit!")
        input("\nPress Enter to continue...")
        return

    print("\n" + "="*50)
    print("EDIT CONTACT")
    print("="*50)

    # show all contacts with numbers
    print()
    for i in range(len(contacts)):
        print(f"{i+1}. {contacts[i]['name']} - {contacts[i]['phone']}")

    try:
        selection = int(input("\nEnter contact number to edit (0 to cancel): "))

        if selection == 0:
            return

        if selection < 1 or selection > len(contacts):
            print("Invalid number!")
            input("\nPress Enter to continue...")
            return

        # get the contact to edit
        idx = selection - 1
        contact = contacts[idx]

        print(f"\nEditing: {contact['name']}")
        print("(Press Enter to keep current value)")
        print()

        # name
        new_name = input(f"Name [{contact['name']}]: ").strip()
        if new_name:
            contact['name'] = new_name

        # phone
        new_phone = input(f"Phone [{contact['phone']}]: ").strip()
        if new_phone:
            if not validate_phone(new_phone):
                print("Invalid phone number!")
                input("\nPress Enter to continue...")
                return
            if check_duplicate(new_phone, contact['id']):
                print("This phone number already exists!")
                input("\nPress Enter to continue...")
                return
            contact['phone'] = new_phone

        # email
        new_email = input(f"Email [{contact['email']}]: ").strip()
        if new_email:
            if not validate_email(new_email):
                print("Invalid email format!")
                input("\nPress Enter to continue...")
                return
            contact['email'] = new_email

        # category
        print("\nCategory:")
        print("1. Family  2. Friends  3. Work  4. Other")
        cat_choice = input(f"Choice (current: {contact['category']}): ").strip()
        if cat_choice == '1':
            contact['category'] = 'Family'
        elif cat_choice == '2':
            contact['category'] = 'Friends'
        elif cat_choice == '3':
            contact['category'] = 'Work'
        elif cat_choice == '4':
            contact['category'] = 'Other'
        # if empty, keep current

        # address
        new_address = input(f"Address [{contact['address']}]: ").strip()
        if new_address:
            contact['address'] = new_address

        # notes  
        new_notes = input(f"Notes [{contact['notes']}]: ").strip()
        if new_notes:
            contact['notes'] = new_notes

        # save changes
        if save_contacts():
            print("\nContact updated successfully!")
        else:
            print("\nUpdated in memory but couldn't save to file")

    except ValueError:
        print("Please enter a valid number!")

    input("\nPress Enter to continue...")


def delete_contact():
    """delete a contact from the list"""
    clear_screen()

    if len(contacts) == 0:
        print("\nNo contacts to delete!")
        input("\nPress Enter to continue...")
        return

    print("\n" + "="*50)
    print("DELETE CONTACT")
    print("="*50)

    # show contacts
    print()
    for i in range(len(contacts)):
        print(f"{i+1}. {contacts[i]['name']} - {contacts[i]['phone']}")

    try:
        num = int(input("\nEnter contact number to delete (0 to cancel): "))

        if num == 0:
            return

        if num < 1 or num > len(contacts):
            print("Invalid number!")
            input("\nPress Enter to continue...")
            return

        contact_to_delete = contacts[num - 1]

        # confirm deletion
        confirm = input(f"\nAre you sure you want to delete '{contact_to_delete['name']}'? (yes/no): ").strip().lower()

        if confirm == 'yes' or confirm == 'y':
            # remove from list
            contacts.pop(num - 1)

            if save_contacts():
                print(f"\nDeleted '{contact_to_delete['name']}' successfully")
            else:
                print("\nDeleted from memory but couldn't save to file")
        else:
            print("\nDeletion cancelled")

    except ValueError:
        print("Please enter a valid number!")

    input("\nPress Enter to continue...")


def show_stats():
    """display statistics about contacts"""
    clear_screen()
    print("\n" + "="*50)
    print("CONTACT STATISTICS")
    print("="*50)

    total = len(contacts)

    if total == 0:
        print("\nNo contacts yet. Add some to see statistics!")
        input("\nPress Enter to continue...")
        return

    # count by category
    family_count = 0
    friends_count = 0
    work_count = 0
    other_count = 0

    for c in contacts:
        if c['category'] == 'Family':
            family_count += 1
        elif c['category'] == 'Friends':
            friends_count += 1
        elif c['category'] == 'Work':
            work_count += 1
        else:
            other_count += 1

    # count emails
    email_count = 0
    for c in contacts:
        if c['email']:
            email_count += 1

    print(f"\nTotal Contacts: {total}")
    print("\nBy Category:")
    print(f"  Family:  {family_count}")
    print(f"  Friends: {friends_count}")
    print(f"  Work:    {work_count}")
    print(f"  Other:   {other_count}")

    print(f"\nContacts with email: {email_count}")
    print(f"Contacts without email: {total - email_count}")

    # find newest and oldest
    if len(contacts) > 0:
        sorted_by_date = sorted(contacts, key=lambda x: x['created_at'])
        print(f"\nNewest contact: {sorted_by_date[-1]['name']}")
        print(f"Oldest contact: {sorted_by_date[0]['name']}")

    input("\nPress Enter to continue...")


def show_menu():
    """displays the main menu"""
    clear_screen()
    print("\n" + "="*50)
    print("       CONTACT BOOK MANAGER")
    print("="*50)
    print("\n1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contacts")
    print("4. Filter by Category")
    print("5. Edit Contact")
    print("6. Delete Contact")
    print("7. Statistics")
    print("8. Exit")
    print("="*50)


# main program
def main():
    """main function that runs the program"""
    print("\n" + "="*50)
    print("  Welcome to Contact Book Manager")
    print("  Created by: Naman Kohli (25BAI10865)")
    print("="*50)
    input("\nPress Enter to start...")

    # load saved contacts
    load_contacts()

    # main loop
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_all()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            edit_contact()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            show_stats()
        elif choice == '8':
            print("\nThank you for using Contact Book Manager!")
            print("Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")
            input("Press Enter to continue...")


# run the program
if __name__ == "__main__":
    main()
