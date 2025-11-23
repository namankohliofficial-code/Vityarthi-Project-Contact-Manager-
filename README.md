[README Python Project.md](https://github.com/user-attachments/files/23697567/README.Python.Project.md)
# Contact Book Manager - Python Edition

**Author:** Naman Kohli  
**Registration No:** 25BAI10865  
**Course:** Introduction to Python Programming  
**Program:** BTECH-CSE (AIML) - First Year, First Semester  
**Date:** November 2025

---

## What is this?

Hey! So this is my Contact Book Manager project for the Python course. Basically, I got tired of only having my contacts on my phone - if I'm working on my laptop and need someone's number, I had to pick up my phone every time. Plus, I wanted to organize contacts better (like separating college friends from family) which my phone doesn't do well.

So I built this simple command-line program in Python that lets me manage contacts right from my laptop. Nothing fancy, but it gets the job done!

## Why I Made This

Honestly, I keep losing track of people's contact info. Sometimes I save them in my phone, sometimes in WhatsApp, sometimes I just remember them (which... doesn't work out great). I needed one place where I could store everything and actually find people when I need them.

Also, for this project I wanted to do something practical that I'd actually use, not just another "hello world" program.

## What It Does

The program is pretty straightforward - here's what you can do:

### Main Features
1. **Add Contacts** - Save name, phone, email, address, notes, and category
2. **View All Contacts** - See everyone in your contact book (sorted alphabetically)
3. **Search** - Find contacts by typing their name, phone, or email
4. **Filter by Category** - Show only Family, Friends, Work, or Other contacts
5. **Edit Contacts** - Update any information for existing contacts
6. **Delete Contacts** - Remove contacts you don't need (asks for confirmation so you don't accidentally delete someone)
7. **Statistics** - See how many contacts you have in each category

### Categories I'm Using
- **Family** - Parents, siblings, relatives
- **Friends** - College friends, school friends, etc.
- **Work** - Professional contacts, internship people
- **Other** - Everything else (delivery guys, neighbors, random people)

## How to Run This Thing

### What You Need
- Python 3.6 or higher (check with `python --version`)
- That's it! No external libraries needed

### Running the Program

1. Download/copy the `contact_book.py` file
2. Open your terminal/command prompt
3. Navigate to the folder where you saved it
4. Run this command:
   ```bash
   python contact_book.py
   ```
5. Follow the menu options!

### First Time Setup
The program creates a `contacts.json` file automatically to save your contacts. This file appears in the same folder as the program. Don't delete it unless you want to lose all your contacts!

## How I Built It

### Technologies Used
- **Python 3** - The main programming language
- **JSON** - To store contacts in a file (so they don't disappear when you close the program)
- **Regular Expressions (regex)** - For validating phone numbers and emails
- **datetime module** - To track when contacts were added

### Project Structure
```
contact-book-manager/
├── contact_book.py      # Main program (all the code)
├── contacts.json        # Auto-created file that stores your contacts
├── README.md           # This file you're reading
├── statement.md        # Problem statement and requirements
└── Project_Report.pdf  # Detailed documentation
```

### Key Python Concepts I Used

Since this is for an intro to Python course, here's what I learned/practiced:

1. **Functions** - Split everything into separate functions (add_contact, search_contacts, etc.)
2. **Lists and Dictionaries** - Contacts are stored as dictionaries in a list
3. **File Handling** - Reading and writing JSON files
4. **Input Validation** - Making sure phone numbers and emails are valid
5. **Loops** - For displaying menus and going through contacts
6. **Conditional Statements** - For menu choices and validation
7. **String Methods** - For searching and formatting text
8. **Exception Handling** - Try/except blocks to handle errors
9. **Regular Expressions** - Pattern matching for validation

## Example Usage

Here's what using the program looks like:

```
==================================================
     📒 CONTACT BOOK MANAGER
==================================================

1. Add New Contact
2. View All Contacts
3. Search Contacts
4. Filter by Category
5. Edit Contact
6. Delete Contact
7. Statistics
8. Exit
==================================================

Enter your choice (1-8): 1

==================================================
ADD NEW CONTACT
==================================================
Enter name (required): Rahul Kumar
Enter phone number (required): 9876543210
Enter email (optional, press Enter to skip): rahul@vit.ac.in
Select category:
1. Family
2. Friends
3. Work
4. Other
Enter choice (1-4): 2
Enter address (optional, press Enter to skip): Hostel A, VIT
Enter notes (optional, press Enter to skip): Same batch, sits next to me in Python class

✓ Contact 'Rahul Kumar' added successfully!
```

## Features I'm Proud Of

### Input Validation
The program checks:
- Phone numbers must have at least 10 digits
- Email addresses must be in proper format (something@something.something)
- Can't have two contacts with the same phone number
- Required fields can't be left empty

### Data Persistence
Your contacts are saved automatically in `contacts.json`. Even if you close the program and come back later, everything is still there!

### Search is Smart
You can search by name, phone, or email - it looks through all of them. Also case-insensitive, so searching "rahul" will find "Rahul Kumar".

### User-Friendly
- Clear menus and instructions
- Confirmation before deleting (so you don't mess up)
- Helpful error messages
- Shows emojis for better readability (📞✉️📍📝)

## Challenges I Faced

Not gonna lie, this took me longer than I thought it would. Here are some things that tripped me up:

### 1. Time Management (3-4 days total)
- **Day 1**: Planned the structure, wrote basic add/view functions
- **Day 2**: Added search, filter, and edit features
- **Day 3**: Worked on validation and bug fixing
- **Day 4**: Final testing and documentation

Balancing this with other assignments was tough. I mostly worked on it after 8 PM when I was done with classes.

### 2. JSON File Handling
Initially, I tried to write to the file after every operation, but messed up the format a few times. Had to learn about `json.dump()` and `json.load()` properly. Also dealt with encoding issues when using emojis.

### 3. Input Validation
Getting the regex patterns right for phone and email validation was annoying. Spent a good hour debugging why some valid phone numbers weren't working (forgot to handle spaces and hyphens).

### 4. Preventing Duplicates
Had to figure out how to check if a phone number already exists without messing up the edit function (because editing shouldn't flag your own number as duplicate).

### 5. Menu Loop Logic
Getting the menu to work smoothly with proper screen clearing and pausing took some trial and error. The `clear_screen()` function works differently on Windows vs Mac/Linux which I didn't know initially.

## What I Learned

This project taught me:
- How to structure a bigger Python program (not just small scripts)
- Working with files and JSON data
- Importance of validation (users can input weird stuff!)
- Breaking problems into smaller functions
- Debugging skills (used a LOT of print statements)
- How to make terminal programs more user-friendly

The most interesting part was probably implementing the search feature - figuring out how to search through all the fields and display results nicely.

## Known Issues / Things That Could Be Better

Being honest about what's not perfect:
- **No undo feature** - If you delete someone by accident, they're gone
- **Basic search** - Only does simple text matching, no fuzzy search
- **No contact photos** - Just text info
- **Command-line only** - No graphical interface (maybe next semester?)
- **No import/export** - Can't backup to Excel or import from phone

## Future Plans

If I have time later (probably not this semester), I'd like to add:
- Backup/restore feature
- Export to CSV
- Birthday reminders
- Favorite contacts
- Better formatting for phone numbers
- Option to add multiple phone numbers per person

## Testing

I tested the program with:
- ✓ Adding 10+ contacts with different info
- ✓ Searching by names, phones, and emails
- ✓ Editing contacts and making sure changes save
- ✓ Deleting contacts and confirming they're gone
- ✓ Trying to add invalid phone numbers and emails (should show errors)
- ✓ Trying to add duplicate phone numbers (should block it)
- ✓ Closing and reopening to make sure data persists
- ✓ Each category filter
- ✓ Statistics with different numbers of contacts

Tested on:
- Windows 11 (my laptop)
- Python 3.11

## Files Included in Submission

1. **contact_book.py** - The main program
2. **README.md** - This file with usage instructions
3. **statement.md** - Problem statement and why I built this
4. **Project_Report.pdf** - Detailed technical documentation
5. **contacts.json** - Example data file (will be created when you run the program)

## Credits

- Built entirely by me (Naman Kohli)
- Used Python documentation for learning about JSON and regex
- Stack Overflow helped when I got stuck on the regex patterns
- No external tutorials or code copied - wrote everything from scratch based on what we learned in class

## Final Thoughts

This was my first "real" Python project beyond classroom exercises. It's not perfect, but it works and I actually use it! Learned a ton while building it.

If you're checking this for grading - all the code is original, I can explain any part of it, and I genuinely spent time on making it functional and clean. Hope you like it!

---

**License:** Free to use for educational purposes

**Contact:** 
- Name: Naman Kohli
- Reg No: 25BAI10865
- Course: Introduction to Python Programming
- Program: BTECH-CSE(AIML), Semester 1

---

*README last updated: November 23, 2025*
