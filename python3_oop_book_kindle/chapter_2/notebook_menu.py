import sys
from notebook import Notebook


class Menu:
    def __init__(self):
        """ create instance of notebook"""
        self.notebook = Notebook()
        # choices dictionary
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    @staticmethod
    def display_menu():
        print("""
        
        Notebook Menu
        
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Notes
        5. Quit
        
        """)

    def run(self):
        """ run method
        displays menu for choices
        gets choice from user
        get the value of choice, save as 'action'
        if valid action, executes action eg. self.add_note()
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                # call action by appending empty brackets
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        """ get and display notes """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_notes(self):
        """ search for notes """
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        """ create a new note, and add memo """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        print("'show note' to get id's")
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """ exit return code zero """
        print("Exiting")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
