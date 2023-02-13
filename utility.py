# import modules
import sqlite3


# Class Books definition.
class Books:

    # ************************** class init ************************************
    def __init__(self, title, author, qty):
        self.title = title
        self.author = author
        self.qty = qty

    # ****************************** add book (setter) ***************************
    def add_book(self):
        title, author, qty = '', '', 0
        print('Please enter a new book details')
        while True:
            if title == '':
                title = input('Please enter the book title: ')
            elif author == '':
                author = input('Please enter the book author: ')
            elif qty == 0:
                try:
                    qty = int(input('Please enter how many books are available: '))
                except ValueError:
                    print('Please enter an integer:')
                    continue
                else:
                    break
        new_book = (title, author, qty)
        self.db_add_book(new_book)
        return 'Book added successfully'

    # ****************************** (getter) ************************************
    def get_book(self):
        t = (self.title, self.author, self.qty)
        return t

    # ****************************** Create database and table *******************
    def db_first_connect(self):
        db = sqlite3.connect("my_books")
        cursor = db.cursor()
        result = 'ok'
        try:
            cursor.execute(" CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT,  author TEXT, qty INTEGER)")
        except Exception:
            result = 'Database already exist'
        finally:
            db.close()
        return result

    # ******************************  Database add book *************************
    def db_add_book(self, book):
        db = sqlite3.connect("my_books")
        cursor = db.cursor()
        cursor.execute(f'''INSERT INTO books( title, author, qty)
                           VALUES(?,?,?)''', book)
        db.commit()
        db.close()

    # ****************************** Read all books from database ***************
    def read_all(self):
        books = []
        db = sqlite3.connect("my_books")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books")
        for record in cursor:
            books.append(record)
        db.close()
        return books

    # ****************************** Search book by title or author *************
    # partial mach supported. Return a list of books
    def search(self, ):
        books = []
        search_text = input('Please enter title or author to find the book: ')
        while True:
            if search_text == '':
                search_text = input('Please enter title or author to find the book: ')
                continue
            else:
                break
        db = sqlite3.connect("my_books")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                       (f'%{search_text}%', f'%{search_text}%'))
        for record in cursor:
            books.append(record)
        db.close()
        return books

    # ****************************** Update book by id **************************
    # Update the database record with received id.
    # If title or author or quantity are not supplied will remain unchanged
    # If id is not in the table no record is affected
    def update(self):
        db = sqlite3.connect("my_books")
        cursor = db.cursor()
        id, title, author, _qty = 0, '', '', ''
        while True:
            if id <= 0:
                try:
                    id = int(input('Please enter the book id you want to update: '))
                except ValueError:
                    print('Please enter a positive integer:')
                    continue
            if title == '' and author == '' and _qty == '':
                print(f'''You can chose to update book title and author and quantity.
                (Leave empty the fields you do not want to update, chose at list one.) ''')
                title = input('Please enter title : ')
                author = input('Please enter author : ')
                _qty = input('Please enter quantity : ')
                continue
            if _qty == '':
                cursor.execute(f'SELECT qty FROM books WHERE id={id}')
                for record in cursor:
                    qty = int(record[0])
            else:
                try:
                    qty = int(_qty)
                except ValueError:
                    print('Please enter a positive integer:')
                    _qty = input('Please enter quantity : ')
                    continue
                break
            break

        if title == ''.strip():
            cursor.execute(f'SELECT title FROM books WHERE id={id}')
            for record in cursor:
                title = record[0]
        if author == ''.strip():
            cursor.execute(f'SELECT author FROM books WHERE id={id}')
            for record in cursor:
                author = record[0]
        cursor.execute(f'''UPDATE books 
                           SET title="{title}" , author="{author}", qty={qty}
                           WHERE id={id} ''')
        db.commit()
        cursor = db.cursor()
        return 'update successfully'

    # ****************************** Delete book by id **************************
    # If id is not in the table no record is affected
    def delete_book(self):
        id = 0
        while True:
            try:
                id = int(input('Please enter how many books are available: '))
            except ValueError:
                print('Please enter a positive integer:')
                continue
            if id <= 0:
                continue
            break
        db = sqlite3.connect("my_books")
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM books WHERE id={id} ")
        db.commit()
        cursor = db.cursor()
        return "delete successfully"
