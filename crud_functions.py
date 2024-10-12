import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')


def base():
    for i in range(1, 5):
        cursor.execute("INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
                       (i, f"Продукт: {i}", f"Описание: {i}", i * 100))
    connection.commit()


base()


def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products")
    list = cursor.fetchall()
    return list


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
);
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    users_list = cursor.execute('SELECT username FROM Users WHERE username=?', (username,)).fetchall()
    connection.commit()
    return True if len(users_list) > 0 else False
