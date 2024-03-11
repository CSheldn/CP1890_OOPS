import sqlite3

conn = sqlite3.connect('Movies.sqlite')

c = conn.cursor()
query = """CREATE TABLE if NOT EXISTS Movies 
            (id INTEGER PRIMARY KEY,
            title VARCHAR(30),
            release_year INT,
            mins INT,
            category VARCHAR(30));"""

c.execute(query)


def title():
    print("The Movie List program")


def menu():
    print("COMMAND MENU\n"
          "cat  - View movies by category \n"
          "year - View movies by year \n"
          "add  - Add a movie \n"
          "del  - Delete a movie \n"
          "exit - Exit program \n")
