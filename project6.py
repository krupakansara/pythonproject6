import os
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.filename="journal.txt"

    #Add a new entry
    def add_entry(self):
        try:
            entry = input("Entry your journal entry:")

            if entry == "":
                print("Entry cannot be empty")
                return
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                file = open(self.filename,"x")
                file.close()

            except FileExistsError:
                pass 
            file = open(self.filename,"a")
            file.write(time + "|" + entry + "\n")
            file.close()

            print("Entry added successfully!")
        except PermissionError:
            print("File Error:",e)

    #View all entries
    def view_entries(self):
        print("opening journal...")
        try:
            file = open(self.filename,"r")
            print("Journal file open successfully")

            entries = file.read()
            file.close()

            if entries=="":
                print("Your journal is empty")
            else:
                print("\n==All Journal entries==")
                print(entries)
            
        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
            print("file error:",e)

        except OSError as e:
            print("File error: ",e)

        print("Returning to main menu...")

    #Search for an entry
    def search_entry(self):
        try:
            keyword=input("Enter keyword or date: ")

            if keyword ==  "":
                print("Please enter a keyword or date")
                return

            file = open(self.filename, "r")
            found = False 

            for entry in file:
                if keyword.lower() in entry.lower():
                    print(entry,end="")
                    found = True 

            file.close()

            if found == False:
                print("No matching entry found")

        except FileNotFoundError:
            print("Journal file does not exist")

        except PermissionError:
            print("permission denied")

        except OSError as e :
            print("File error", e)

    #Delete all entries
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("Journal file does not exist")
                return

            confirm = input("Delete all entries? (yes/no): ")

            if confirm.lower() == "yes":
                file = open(self.filename, "w")
                file.close()

                os.remove(self.filename)
                print("All entries deleted successfully!")

            elif confirm.lower() == "no":
                print("Deletion cacelled")

            else:
                print("Please enter yes or no")

        except PermissionError:
            print("Permission denied")

        except OSError as e :
            print("File error: ",e)

    #Main menu
    def run(self):
        while True:
            print("\n=====PERSONAL JOURNAL======")
            print("1. Add a new entry")
            print("2. View all entries")
            print("3. Search for an entry")
            print("4. Delete all Entries")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print("Thank you for using personal Journal")
                break

            else:
                print("Invalid choice. Try again.")

journal = JournalManager()
journal.run()




        
