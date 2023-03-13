import sqlite3 as sql

def ask_user():
    last_name = input('Input surename: ')
    first_name = input('Input name: ')
    phone_number = int(input('Input phone mumber: '))
    return last_name, first_name, phone_number

def create_phonebook():
    cursor.execute('CREATE TABLE IF NOT EXISTS phonebook (surename text, name text, number int)')
    conn.commit()

def remove_table(table_name):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()

def show_tables():
    res = cursor.execute("SELECT name FROM sqlite_master").fetchall()
    print(res)

def read_file(file: tuple):
    for i in file:
        surename, name, phone = i
        print(surename, name, phone)

def ask_search():
    search_param = input('1 - by SURENAME, 2 - by NAME, 3 - by PHONE NUMBER: ')
    what = None
    if search_param == '1':
        what = input('Input surename for search: ')
    elif search_param == '2':
        what = input('Input name for search: ')
    elif search_param == '3':
        what = input('Input phone number for search: ')
    return search_param, what

def save_to_phonebook():
    print('-- Add new contact --'.upper())
    contact = ask_user()
    cursor.execute("INSERT INTO phonebook VALUES (?,?,?)", contact)
    conn.commit()

def show_all_contacts():
    print('-- All contacts --'.upper())
    res = cursor.execute("SELECT * FROM phonebook ORDER BY 1,2,3").fetchall()
    if len(res) == 0:
        print('Nothing found')
    else:
        read_file(res)

def search_contacts(params: tuple):
    if params[0] == '1':
        res = cursor.execute("SELECT * FROM phonebook WHERE surename=? ORDER BY 1,2,3", (params[1],)).fetchall()
    elif params[0] == '2':
        res = cursor.execute("SELECT * FROM phonebook WHERE name=? ORDER BY 1,2,3", (params[1],)).fetchall()
    elif params[0] == '3':
        res = cursor.execute("SELECT * FROM phonebook WHERE number=? ORDER BY 1,2,3", (params[1],)).fetchall()
    return res

def remove_contacts(params: tuple):
    if params[0] == '1':
        cursor.execute("DELETE FROM phonebook WHERE surename=?", (params[1],))
    elif params[0] == '2':
        cursor.execute("DELETE FROM phonebook WHERE name=?", (params[1],))
    elif params[0] == '3':
        cursor.execute("DELETE FROM phonebook WHERE number=?", (params[1],))
    conn.commit()

def search_process():
    print('-- What contacts are you looking for? --'.upper())
    params = ask_search()
    data = search_contacts(params)
    if len(data) == 0:
        print('Nothing found')
    else:
        read_file(data)

def update_process():
    print('-- What contacts do you want to update? --'.upper())
    params = ask_search()
    data = search_contacts(params)
    if len(data) == 0:
        print('Nothing found')
    else:
        read_file(data)
        arg = input('\nAre you sure to remove it? (Y/N):')
        if arg.upper() == 'Y':
            print('\nInput new data')
            i, j, k = ask_user()
            contact = (i, j, k, data[0][-1])
            cursor.execute("UPDATE phonebook SET surename=?, name=?, number=? WHERE number=?", contact)
            conn.commit()

            print('\nUpdate is completed')
            data = search_contacts(('3',contact[-2]))
            read_file(data)

def remove_process():
    print('-- What contacts do you want to remove? --'.upper())
    params = ask_search()
    data = search_contacts(params)
    if len(data) == 0:
        print('Nothing found')
    else:
        read_file(data)
        arg = input('\nAre you sure to remove it? (Y/N):')
        if arg.upper() == 'Y':
            remove_contacts(params)
            print('Data was removed')

def main_menu():

    while True:
        print('\n-- Welcome to phonebook --'.upper())
        user_choice = input('1 - Look through all phonebook\n'
                            '2 - Add new contact\n'
                            '3 - Find contact\n'
                            '4 - Update contact\n'
                            '5 - Remove contact\n'
                            '0 - Exit\n')
        if user_choice == '1':
            show_all_contacts()
        elif user_choice == '2':
            save_to_phonebook()
        elif user_choice == '3':
            search_process()
        elif user_choice == '4':
            update_process()
        elif user_choice == '5':
            remove_process()
        elif user_choice == '0':
            print('\n-- Goodbye --'.upper())
            break

if __name__ == '__main__':
    conn = sql.connect('example.db')
    cursor = conn.cursor()
    main_menu()
    conn.close()