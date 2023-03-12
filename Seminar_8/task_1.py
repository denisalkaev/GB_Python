import sqlite3 as sql

def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
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

def save_to_phonebook(data: tuple):
    cursor.execute("INSERT INTO phonebook VALUES (?,?,?)", data)
    conn.commit()

def read_file(file):
    for i in file:
        surename, name, phone = i
        print(surename, name, phone)

def show_all_contacts():
    res = cursor.execute("SELECT * FROM phonebook ORDER BY 1,2,3").fetchall()
    read_file(res)

def search_contacts()

if __name__ == '__main__':
    conn = sql.connect('example.db')
    cursor = conn.cursor()
    # data = ask_user()
    create_phonebook()
    # show_tables()
    # remove_table('stocks')
    # show_tables()
    save_to_phonebook(('Alkaev', 'Ivan', 79934))
    show_all_contacts()
    conn.close()