import sqlite3

connection = sqlite3.connect("soulhero.db")

cursor = connection.cursor()

cursor.execute(
    "SELECT username, journey_state FROM players"
)

for row in cursor.fetchall():
    print(row)

connection.close()