# Problem Statement: Contact Book Manager

**Student:** Naman Kohli (25BAI10865)  
**Program:** BTECH-CSE(AIML), First Year - Semester 1  
**Course:** Introduction to Python Programming  
**Date:** November 2025

---

## The Problem I'm Trying to Solve

### My Personal Struggle

Okay, so here's the thing - I have contacts all over the place. Some are in my phone, some people I only have on WhatsApp, some I've saved in random notes, and some I just... remember (which doesn't work great). 

The main issue is: when I'm working on my laptop and need someone's number, I have to stop what I'm doing, pick up my phone, unlock it, open contacts, and search. It's annoying, especially when I'm in the middle of something.

Plus, my phone's contact app doesn't really let me organize people well. I can't easily see "okay, show me all my college friends" or "show me work contacts only". Everything is just one big list.

### What Other Students Face

Talking to my friends, I realized I'm not alone:

1. **Contacts Scattered Everywhere**
   - Phone contacts for calls
   - WhatsApp for messaging (but those aren't real contacts)
   - Email for college stuff
   - Random notes and papers

2. **No Good Organization**
   - Can't separate college friends from school friends
   - Work/internship contacts mixed with personal
   - No way to add notes like "met at tech fest" or "knows Python well"

3. **Access Issues**
   - Phone contacts not available on laptop
   - Can't easily share contact info with others
   - Switching phones = pain

4. **Finding People Takes Time**
   - Scrolling through long lists
   - Remembering how you saved someone's name
   - "Was it Rahul or Rahul Kumar or Rahul K?"

5. **Risk of Losing Everything**
   - Phone gets lost/broken = bye bye contacts
   - No easy backup method
   - Google sync doesn't always work

## Who Needs This?

Mainly people like me:
- **First-year students** managing lots of new contacts (seniors, batchmates, club members)
- **Anyone working on group projects** who needs to quickly find team members
- **People who switch between devices** (phone and laptop)
- **Anyone who wants better organization** than what phone contacts offer

## What I'm Building

A Python-based command-line contact manager that runs on my laptop. Super simple, no fancy stuff, just practical.

### What It Should Do

**Core Features:**
1. Add new contacts with full details (name, phone, email, address, notes)
2. View all my contacts in one place
3. Search by name, phone, or email
4. Organize contacts into categories (Family, Friends, Work, Other)
5. Edit contact information when things change
6. Delete contacts I don't need anymore
7. See statistics (how many contacts in each category, etc.)

**Important Requirements:**
- Save contacts permanently (not just in memory)
- Validate phone numbers and emails (so I don't save garbage data)
- Prevent duplicate phone numbers
- Easy to use with clear menus
- Should work offline (no internet needed)

## Why Python?

- It's what we're learning this semester
- Good for file handling (saving contacts)
- Has built-in JSON support (easy to store data)
- Can make command-line programs easily
- No need for complex setup or external libraries

## My Approach

### Technical Decisions

**Data Storage:** Using JSON files because:
- Easy to read and edit manually if needed
- Python has built-in JSON support
- Can store complex data (dictionaries/lists)
- No database setup required

**Structure:** Command-line interface because:
- Simpler to build (no GUI needed)
- Works on any system with Python
- Faster to use once you get used to it
- Focuses on functionality over looks

**Validation:** Using regex (regular expressions) for:
- Phone number format checking
- Email validation
- Learned about regex in class, good chance to practice

### Data Structure

Each contact will have:
```
{
    "id": unique number,
    "name": "Person's Name",
    "phone": "Phone Number",
    "email": "Email Address",
    "category": "Family/Friends/Work/Other",
    "address": "Physical Address",
    "notes": "Any extra info",
    "created_at": "When I added them"
}
```

## What Success Looks Like

I'll consider this project successful if:

1. ✓ I can add, view, edit, search, and delete contacts
2. ✓ Contacts are saved permanently (survive closing the program)
3. ✓ Phone and email validation works correctly
4. ✓ Can't add duplicate phone numbers
5. ✓ Search works across names, phones, and emails
6. ✓ Categories help me organize contacts
7. ✓ The program doesn't crash with weird inputs
8. ✓ Code is clean enough that I can explain any part
9. ✓ I actually use it myself (not just for grades)

## What I'm NOT Building

Being realistic about scope (first year, limited time):

- ❌ No graphical interface - just command line
- ❌ No cloud sync or multi-device support
- ❌ No contact photos/avatars
- ❌ No import from phone contacts
- ❌ No integration with email or messaging apps
- ❌ No fancy features like birthday reminders (yet)

This is intentional - I want to focus on core functionality and do it well, rather than adding a bunch of half-working features.

## Expected Learning Outcomes

What I hope to learn from this project:

### Python Skills
- Working with functions and organizing code properly
- File handling (reading/writing JSON)
- Lists and dictionaries for data management
- String manipulation and validation
- User input handling
- Error handling with try/except
- Regular expressions for pattern matching

### Programming Concepts
- How to structure a real program (not just exercises)
- CRUD operations (Create, Read, Update, Delete)
- Data persistence (saving things permanently)
- Input validation importance
- User experience in command-line apps
- Testing and debugging strategies

### Soft Skills
- Time management (balancing with other work)
- Problem-solving when stuck
- Documentation writing
- Project planning

## Time Estimation

**Total Time:** About 3-4 days of actual work

- **Day 1 (3-4 hours):** Planning, basic structure, add/view functions
- **Day 2 (3-4 hours):** Search, filter, edit, delete features
- **Day 3 (2-3 hours):** Validation, error handling, bug fixing
- **Day 4 (2-3 hours):** Testing, documentation, final polish

Most work happened after 8 PM when I'm done with classes. Time management was tough with other assignments, but I blocked out specific times for this.

## Challenges I Expect

Based on what I know about my skills:

1. **JSON File Handling** - Haven't worked much with files before
2. **Regex for Validation** - Regex is still confusing to me
3. **Menu System** - Making the interface smooth and user-friendly
4. **Bug Fixing** - Always takes longer than expected
5. **Duplicate Checking** - Especially when editing existing contacts
6. **Documentation** - Writing clear explanations takes time

## Real-World Application

This isn't just an assignment - I genuinely need this. Uses:

- Quick access to college contacts from my laptop
- Organized way to store internship/work contacts
- Notes field for context ("met at hackathon", "Python expert", etc.)
- Separate from phone (backup if phone dies)
- Easy to find people for group projects

## Resources I'll Use

- Python documentation (official docs)
- Class notes and lecture examples
- Stack Overflow (when stuck on specific issues)
- Regex tutorials for validation patterns
- Trial and error (lots of testing)

I'm writing all code myself - no copy-pasting from GitHub or tutorials. If I reference something, I'll understand it first, then implement it my way.

## Evaluation Criteria (My Understanding)

What I think will be evaluated:

1. **Functionality (40%)** - Does it work? All features implemented?
2. **Code Quality (25%)** - Clean, readable, well-organized?
3. **Documentation (20%)** - Clear README, comments, reports?
4. **Problem Solving (15%)** - Did I solve a real problem? Validation and error handling?

I'm focusing on making sure it actually works well rather than adding unnecessary features.

## Conclusion

This project solves my actual problem of managing contacts between phone and laptop, while letting me practice Python concepts we've learned. It's scoped appropriately for first year (not too simple, not too complex), and I'll actually use it after submission.

Most importantly - it's my own work, built from scratch, solving something I personally care about.

---

**Problem Statement Prepared by:** Naman Kohli  
**Registration:** 25BAI10865  
**Date:** November 23, 2025