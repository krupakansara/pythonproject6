📔 File Operator --- Personal Journal
> A beginner-friendly Python project that lets users create, view,
> search, and delete personal journal entries using text-file handling
> and Object-Oriented Programming (OOP).
---
✨ Project Overview
File Operator is a menu-driven personal journal application built
with Python. It stores journal entries in a text file named
`journal.txt`. Each entry includes a timestamp so the user can keep
track of when it was written.
The project demonstrates file operations, exception handling, classes,
objects, and instance methods.
🎯 Project Objectives
📁 Practise reading from and writing to text files.
📝 Add journal entries with timestamps.
🔎 Search entries using a keyword or date.
🗑️ Delete the journal after asking for confirmation.
🧱 Use a class and object to organise the program.
🛡️ Handle common file errors with exception handling.
🛠️ Technologies Used
Language: Python
Concepts: OOP, classes, objects, instance methods, loops,
conditions, user input, file handling, exception handling
Modules: `os`, `datetime`
Storage: `journal.txt`
🚀 Features
---
Option                  Feature                 Description
---
`1`                     ➕ Add a New Entry      Saves the user's entry
with a date and time.
`2`                     📖 View All Entries     Displays the entries
saved in the journal.
`3`                     🔍 Search for an Entry  Finds entries that
contain a keyword or
date.
`4`                     🗑️ Delete All Entries   Requests confirmation
before deleting the
journal file.
`5`                     🚪 Exit                 Closes the application.
📚 File-Handling Modes
The project demonstrates the following file modes:
`x` --- Create: Creates `journal.txt` if it does not already
exist.
`a` --- Append: Adds a new entry at the end of the file without
replacing existing entries.
`r` --- Read: Reads the journal for viewing or searching.
`w` --- Write: Clears the file's contents before the application
removes the empty journal file during the delete operation.
> ⚠️ **Note:** Opening a file in `w` mode clears its existing contents.
> Use this mode carefully.
🧱 OOP Structure
The application uses a `JournalManager` class to organise the journal
functionality.
`__init__()` --- sets the journal filename.
`add_entry()` --- adds a timestamped entry.
`view_entries()` --- displays saved entries.
`search_entry()` --- searches entries by keyword or date.
`delete_entries()` --- asks for confirmation and deletes the
journal.
`run()` --- displays the main menu and processes the user's choice.
An object of `JournalManager` is created to run the application.
🛡️ Exception Handling
The program handles common file-related problems, including:
`FileExistsError` --- when the journal file already exists during
creation.
`FileNotFoundError` --- when the journal file cannot be found for
reading or searching.
`PermissionError` --- when access to a file is denied.
`OSError` --- for other operating-system or file-operation errors.
▶️ How to Run
Install Python 3 if it is not already installed.
Download or clone this repository.
Open the project folder in VS Code.
Open the terminal in that folder.
Run the program:
    ``` bash
    python project6.py
    ```
Follow the menu displayed in the terminal.
The program creates or uses `journal.txt` in the current working
directory.
🖼️ Project Screenshots
Add the three screenshots to a folder named `screenshots` in your
repository, using these filenames:
1. Main Program
![Screenshot 1](screenshots/Screenshot%202026-10-14%20182555.png)
2. Journal Entries
![Screenshot 2](screenshots/Screenshot%202026-10-14%20182645.png)
3. Search / Menu Output
![Screenshot 3](screenshots/Screenshot%202026-10-14%20182659.png)
🎬 Project Demonstration Video
Place your demonstration video inside the `assets` folder in the
repository.
▶️ Watch the Project Demonstration
📂 Suggested Repository Structure
``` text
File-Operator/
│
├── project6.py
├── README.md
├── journal.txt                 # Created when the program saves an entry
├── screenshots/
│   ├── Screenshot 2026-10-14 182555.png
│   ├── Screenshot 2026-10-14 182645.png
│   └── Screenshot 2026-10-14 182659.png
└── assets/
    └── 2026-10-04 16-30-31.mp4
```
> 📌 GitHub cannot display files directly from a path on your computer
> (such as `C:\\Users\\...`). Copy the screenshots into the repository's
> `screenshots` folder and the video into its `assets` folder, then
> commit and push those files. The links above will work once the files
> are uploaded with the same names.
👩‍💻 Learning Outcome
By completing this project, I practised building a menu-driven Python
application, organising functionality with a class, working with text
files, using different file modes, and handling common file errors.
---
⭐ Thank you for checking out my File Operator project!
