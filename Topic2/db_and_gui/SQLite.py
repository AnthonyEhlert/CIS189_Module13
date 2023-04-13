"""
Program: SQLite.py
Author: Tony Ehlert
Last date modified: 4/14/2023

The purpose of this program is to create a class that contains the required methods to create, read, update, and delete
a SQL database

The input is necessary info and code to define and create the class
The output is none
"""
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid  # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid  # returns the row id of the cursor object, the student id


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows  # return the rows


def select_all_students(conn):
    """
    Query all rows of the student table

    :param conn: the connection object
    :return: records of the connection object
    """

    # create cursor object
    cur = conn.cursor()

    # create SQL query statement
    query_stmnt = "SELECT * FROM student"

    # execute query_stmnt using cursor object
    cur.execute(query_stmnt)

    # create variable to hold records obtained from cursor object
    rows = cur.fetchall()

    # return rows variable
    return rows


def select_id(conn, fname, lname):
    """
    Query the student table for id of matching firstnmae and lastname

    :param conn: the connection object
    :return: id of the matched object
    """

    # create cursor object
    cur = conn.cursor()

    # create SQL query statement
    query_stmnt = "SELECT id FROM person WHERE firstname=? AND lastname=?"

    # execute query_stmnt using cursor object
    cur.execute(query_stmnt, (fname, lname))

    # create variable to hold records obtained from cursor object
    student_id = cur.fetchone()

    # return rows variable
    return student_id
