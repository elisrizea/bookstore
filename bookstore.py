# import modules
import utility
from tabulate import tabulate

# Instantiate class and check if db is created (if not create db)
book = utility.Books('First book', 'First author', 4)
print(book.db_first_connect())

# Save colors in constants to decorate the console output
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'
MAG = '\u001b[35m'

# Display main menu
while True:
    print(f' {BLUE}********************** Main Menu **********************\n')

    menu = input(f'''Select one of the following Options below:
                {MAG}v{BLUE}    - {MAG}V{BLUE}iew all books
                {MAG}a{BLUE}    - {MAG}A{BLUE}dd a new book
                {MAG}d{BLUE}    - {MAG}D{BLUE}elete a book using id
                {MAG}u{BLUE}    - {MAG}U{BLUE}pdate a book title or author using id
                                (leave title or author field empty and it will not update)
                {MAG}s{BLUE}    - {MAG}S{BLUE}earch for a book using title or author
                                (partial mach will show results)
                {MAG}e{BLUE}    - {MAG}E{BLUE}xit
{MAG}Enter your choice: {END}''').strip().lower()

    # Request input and call the necessary function
    if menu == 'v':
        print(f"""
{BLUE}================ View all books =========================={END}""")
        # Print a table with all books
        table = [[f'{BLUE}Id{END}', f'{BLUE}Book title{END}', f'{BLUE}Author{END}', f'{BLUE}Quantity{END}']]
        for my_book in book.read_all():
            table.append(
                [f'{GREEN}{my_book[0]}{END}', my_book[1],
                 my_book[2], my_book[3]])
        if len(table) == 1:
            print('No books found matching your search')
        else:
            print(tabulate(table, tablefmt="rounded_grid", ))
        continue
    elif menu == 'a':
        print(f"""
{BLUE}================ Add a new book: =========================={END}""")
        # Add a new book
        book.add_book()
        continue
    elif menu == 'd':
        print(f"""
{BLUE}================ Delete a book by id: =========================={END}""")
        # Delete a book by id
        print(book.delete_book())
        continue
    elif menu == 'u':
        print(f"""
{BLUE}================ Update a book by id: =========================={END}""")
        # Update a book by id
        print(book.update())
        continue
    elif menu == 's':
        print(f"""
{BLUE}================ Search for a book: =========================={END}""")
        # Print a table with all books
        table = [[f'{BLUE}Id{END}', f'{BLUE}Book title{END}', f'{BLUE}Author{END}', f'{BLUE}Quantity{END}']]
        for my_book in book.search():
            table.append(
                [f'{GREEN}{my_book[0]}{END}', my_book[1],
                 my_book[2], my_book[3]])
        if len(table) == 1:
            print('No books found matching your search')
        else:
            print(tabulate(table, tablefmt="rounded_grid", ))
        continue
    # Exit script
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print(
            f'{RED}Please try again and type: '
            f'{GREEN}v{END} or {GREEN}a{END} or {GREEN}d{END} or {GREEN}u{END} or {GREEN}s{END} or {GREEN}e{END}')
        continue
