class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.issued:
                book.issued = True
                print(f"Book '{book.title}' issued.")
                return
        print("Book not available for issuing.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.issued:
                book.issued = False
                print(f"Book '{book.title}' returned.")
                return
        print("This book was not issued or doesn't exist.")

    def display_books(self):
        print("Available books in the library:")
        for book in self.books:
            status = "Issued" if book.issued else "Available"
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            isbn = input("Enter ISBN of the book to issue: ")
            library.issue_book(isbn)
        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()