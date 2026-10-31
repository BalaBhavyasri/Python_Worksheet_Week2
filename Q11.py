class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        for book in self.books:
            if book["name"] == book_name:
                print("Book already exists.")
                return

        self.books.append({
            "name": book_name,
            "available": True
        })
        print("Book added successfully.")

    def issue_book(self, book_name):
        for book in self.books:
            if book["name"] == book_name:
                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return

        print("Book not found.")

    def return_book(self, book_name):
        for book in self.books:
            if book["name"] == book_name:
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")

    def display_books(self):
        print("\nAvailable Books:")
        found = False

        for book in self.books:
            if book["available"]:
                print(book["name"])
                found = True

        if not found:
            print("No books available.")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)

    elif choice == "2":
        name = input("Enter book name to issue: ")
        library.issue_book(name)

    elif choice == "3":
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == "4":
        library.display_books()

    elif choice == "5":
        print("Thank you for using the Library System.")
        break

    else:
        print("Invalid choice.")