"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import sqlite3

# TODO 14.1 - 14.3 Opening a database connection with SQLite
print("=" * 10, "Section 14.1-14.3 opening a database connection", "=" * 10)
# establish a connection to an SQL database named dogs.db using dogs_connection as a variable
# Note: A new database should be created if it does not yet exist
dogs_connection = sqlite3.connect('dogs.db')
# create a cursor for working with your database named dogs_cursor
dogs_cursor = dogs_connection.cursor()
# NOTE: the following statement will delete the Dogs table if it exists
# This statement is included for testing purposes to ensure a clean slate
# each time you re-run your program (remove the # )
dogs_cursor.execute("""DROP TABLE IF EXISTS Dogs""")

# TODO 14.4 Creating a Table
print("=" * 10, "Section 14.4 creating a table", "=" * 10)
# the following variable will be used in your execute command
table_structure = """CREATE TABLE IF NOT EXISTS Dogs 
                  (DogID INTEGER PRIMARY KEY NOT NULL, 
                  DogName TEXT, OwnerName TEXT, Breed TEXT)"""
# use the cursor variable to execute the SQL command in table_structure
dogs_cursor.execute(table_structure)
# commit the changes using the database connection variable dogs_connection
dogs_connection.commit()

# TODO 14.5 Adding data to a table
print("=" * 10, "Section 14.5 adding data to a table", "=" * 10)
# complete the following statement to add a total of four records to the table
# the first record has been added for you (remove the # from each line)
dogs_cursor.execute('''INSERT INTO Dogs (DogID, DogName, OwnerName, Breed)
                    VALUES ('2', 'Donovan', "Ben", "Golden Retriever")
                    ''')
dogs_cursor.execute("""INSERT INTO Dogs (DogID, DogName, OwnerName, Breed)
                    VALUES ("581321", "Zoey", "Ade", "Mix")
                    """)
dogs_cursor.execute("""INSERT INTO Dogs (DogID, DogName, OwnerName, Breed)
                    VALUES ("314159", "Lacy", "Ryan", "Australian Blue Heeler")
                    """)
dogs_cursor.execute("""INSERT INTO Dogs (DogID, DogName, OwnerName, Breed)
                    VALUES ("235711", "Gia", "Aron and Darren", "Unknown")
                    """)
# commit your changes to make them visible to other database users
dogs_connection.commit()

# TODO 14.6 Querying data with SELECT
print("=" * 10, "Section 14.6 querying data with SELECT", "=" * 10)
# write an execute statement to select all columns (fields) from the Dogs table
dogs_cursor.execute("SELECT DogID, DogName, OwnerName, Breed FROM Dogs")
# fetch all of the results into a list variable
results = dogs_cursor.fetchall()
# use a for loop to display the results
for i in results:
    print(f"{i[0]:10} {i[1]:10} {i[2]:20} {i[3]:30}")

# TODO 14.6-14.7 updating specific records
print("=" * 10, "Section 14.6-14.7 updating specific records", "=" * 10)
# add a WHERE clause to the following statement to select the dog with DogID 2
# (remove the # to test)
dogs_cursor.execute("""SELECT * FROM Dogs WHERE DogID == 2""")

# fetch and display the record found
print(dogs_cursor.fetchall())
# write an execute statement to update the record with DogID 2 to have OwnerName "Unknown"
dogs_cursor.execute('''UPDATE Dogs
                    SET OwnerName = "Unknown"
                    WHERE DogID == 2''')
dogs_connection.commit()
# Select, fetch and display the updated record with DogID 2
dogs_cursor.execute("""SELECT * FROM Dogs WHERE DogID == 2""")
results = dogs_cursor.fetchall()
for i in results:
    print(f"{i[0]:10} {i[1]:10} {i[2]:20} {i[3]:30}")

# commit your changes (changes are only visible to your program until committed)
dogs_connection.commit()
# close your connection to the database
dogs_connection.close()