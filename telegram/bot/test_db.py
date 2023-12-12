import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

# Check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bot_chatbotuser';")
table_exists = cursor.fetchone()

if table_exists:
    print("Table bot_chatbotusers exists!")
else:
    print("Table bot_chatbotusers does not exist.")

cursor.close()
