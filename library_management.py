import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT DEFAULT 'Available'
)
""")
conn.commit()


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    print("✅ Book added successfully!")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n📚 Book List:")
    for book in books:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {book[3]}")


def issue_book():
    book_id = int(input("Enter Book ID to issue: "))

    cursor.execute("SELECT status FROM books WHERE id=?", (book_id,))
    result = cursor.fetchone()

    if result and result[0] == "Available":
        cursor.execute("UPDATE books SET status='Issued' WHERE id=?", (book_id,))
        conn.commit()
        print("✅ Book issued successfully!")
    else:
        print("❌ Book not available!")


def return_book():
    book_id = int(input("Enter Book ID to return: "))

    cursor.execute("UPDATE books SET status='Available' WHERE id=?", (book_id,))
    conn.commit()
    print("✅ Book returned successfully!")


def menu():
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


menu()
conn.close()