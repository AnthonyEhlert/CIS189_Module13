"""
Program: db_and_gui_assignment.py
Author: Tony Ehlert
Last date modified: 4/14/2023

The purpose of this program is to create a GUI with buttons that enable a user to create a database, add records to
the database, and read from the database

The input is information required to create person and student records
The output is a display of all rows or records for each table
"""
import tkinter as tk
import SQLite as sql
from constants import db_name
from tkinter.constants import *
from tkinter import ttk

from Topic1.NumberGuesser import NumberGuesser

'''
FUNCTIONS BELOW HERE
'''


def create_db_and_tables():
    """
    This method creates the database tables if they do not already exist
    :return:
    """
    sql.create_tables(db_name)


def insert_person():
    """
    This method creates a person tuple by using the get method for the first name and last name entry boxes
    and inserts the information into the student table
    :return:
    """
    # create superset for validation
    char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")

    # perform input validation on entry fields for null values
    try:
        null_check(entry_person_fname.get())
        null_check(entry_person_lname.get())
    except ValueError:
        lbl_insert_results.config(text="PERSON NOT INSERTED! First Name or Last Name Cannot be Empty")
        return

    # perform input validation on entry fields for numeric values
    try:
        if not (char_set.issuperset(entry_person_fname.get()) and char_set.issuperset(entry_person_lname.get())):
            raise ValueError
    except ValueError:
        lbl_insert_results.config(text="PERSON NOT INSERTED! First Name or Last Name Cannot Contain Numbers")
        return

    # create connection
    conn = sql.create_connection(db_name)
    with conn:
        # create person tuple
        person = (entry_person_fname.get(), entry_person_lname.get())
        # print(person)

        # add person to table
        sql.create_person(conn, person)

        # edit insert results label
        label_text = "Person: " + entry_person_fname.get() + " " + entry_person_lname.get() + " inserted"
        lbl_insert_results.config(text=label_text)

        # clear entry items
        entry_person_fname.delete(0, END)
        entry_person_lname.delete(0, END)


def insert_student():
    """
    This method creates a student tuple by querying the person table for the person_id
    and using the get() method for the entry boxes for the major and start date variables.
    After creating the tuple, the data is inserted it into the student table
    :return:
    """
    # create supersets for validation
    char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
    date_set = set(("ABCDEFGHIJLMNOPRSTUVYabcdefghijlmnoprstuvy-./,1234567890 "))

    # perform input validation on entry fields for null values
    try:
        null_check(entry_person_fname.get())
        null_check(entry_person_lname.get())
        null_check(entry_student_startdate.get())
        null_check(entry_student_major.get())
    except ValueError:
        lbl_insert_results.config(text="STUDENT NOT INSERTED! No Fields Can be Empty")
        return

    # perform input validation on entry fields for invalid characters
    try:
        if not (char_set.issuperset(entry_person_fname.get()) and char_set.issuperset(entry_person_lname.get())):
            raise ValueError
        if not (char_set.issuperset(entry_student_major.get()) and date_set.issuperset(entry_student_startdate.get())):
            raise ValueError
    except ValueError:
        lbl_insert_results.config(text="STUDENT NOT INSERTED! A Field Contains Invalid Characters")
        return

    first_name = entry_person_fname.get()
    last_name = entry_person_lname.get()

    # create connection
    conn = sql.create_connection(db_name)
    with conn:
        # create student tuple
        try:
            student_id_record = sql.select_id(conn, first_name, last_name)
            student_id = student_id_record[0]
        except TypeError:
            lbl_insert_results.config(text="STUDENT NOT INSERTED! No Matching Person Record Found")
            return

        student_id = student_id_record[0]
        student = (student_id, entry_student_major.get(), entry_student_startdate.get())
        # print(student)

        # add person to table
        sql.create_student(conn, student)

        # edit insert results label
        label_text = "Student: " + entry_person_fname.get() + " " + entry_person_lname.get() + " inserted"
        lbl_insert_results.config(text=label_text)

        # clear entry items
        entry_person_fname.delete(0, END)
        entry_person_lname.delete(0, END)
        entry_student_major.delete(0, END)
        entry_student_startdate.delete(0, END)


def display_person_table():
    """
    This method queries the person table and displays all the records contained in the table
    :return:
    """
    # create results window
    results_window = tk.Tk()

    # set title of results window
    results_window.title("Person Records")

    # set results_window dimensions
    results_window.geometry("650x300")

    # add blank label for column 0
    lbl_empty_col0 = tk.Label(results_window, text='')
    lbl_empty_col0.grid(row=0, column=0)

    # create connection and query table
    conn = sql.create_connection(db_name)
    with conn:
        # create tree for table data
        tree = ttk.Treeview(results_window, column=("c1", "c2", "c3"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="First Name")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Last Name")
        tree.grid(row=1, column=1, columnspan=4)
        rows = sql.select_all_persons(conn)
        for row in rows:
            tree.insert("", tk.END, values=row)

    results_window.mainloop()


def display_student_table():
    """
    This method queries the person table and displays all the records contained in the table
    :return:
    """
    # create results window
    results_window = tk.Tk()

    # set title of results window
    results_window.title("Student Records")

    # set results_window dimensions
    results_window.geometry("825x300")

    # add blank label for column 0
    lbl_empty_col0 = tk.Label(results_window, text='')
    lbl_empty_col0.grid(row=0, column=0)

    # create connection and query table
    conn = sql.create_connection(db_name)
    with conn:
        # create tree for table data
        tree = ttk.Treeview(results_window, column=("c1", "c2", "c3", "c4"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Major")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Start Date")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="End Date")
        tree.grid(row=1, column=1, columnspan=4)
        rows = sql.select_all_students(conn)
        for row in rows:
            tree.insert("", tk.END, values=row)

    results_window.mainloop()


def null_check(value):
    """
    This method check a value to see if it is null. If null raise ValueError
    :param value: value to check if null
    :return:
    """
    if value == '':
        raise ValueError


'''
FUNCTIONS ABOVE HERE
'''

# create main window
main_window = tk.Tk()

'''
MODULE CODE BELOW HERE
'''

# set title of main_window
main_window.title("Person and Student Database")

# set default size of main window
main_window.geometry("430x375")

# add empty labels for grid limits
lbl_empty_row_limit = tk.Label(main_window, text='')
lbl_empty_row_limit.grid(row=15, column=0)

lbl_empty_col_limit = tk.Label(main_window, text='')
lbl_empty_col_limit.grid(row=0, column=7)

# create Database & Table button
btn_create_db = tk.Button(main_window, text="Create Database & Tables", width=25,
                          command=lambda: create_db_and_tables())
btn_create_db.grid(row=1, column=2, rowspan=1, columnspan=2)

# add empty label for row 2
lbl_empty_row2 = tk.Label(main_window, text='')
lbl_empty_row2.grid(row=2, column=0)

# create Add Person button
btn_add_person = tk.Button(main_window, text='Add Person', command=lambda: insert_person())
btn_add_person.grid(row=3, column=1)

# create Add Student button
btn_add_student = tk.Button(main_window, text='Add Student', command=lambda: insert_student())
btn_add_student.grid(row=3, column=4)

# add empty label for row 4
lbl_empty_row4 = tk.Label(main_window, text='')
lbl_empty_row4.grid(row=4, column=0)

# create labels for person first_name and last_name text boxes
lbl_person_fname = tk.Label(main_window, text="Person First Name")
lbl_person_lname = tk.Label(main_window, text="Person Last Name")
lbl_person_fname.grid(row=5, column=1, columnspan=2)
lbl_person_lname.grid(row=5, column=3, columnspan=2)

# create entry boxes for person first_name and last_name
entry_person_fname = tk.Entry(main_window, width=20)
entry_person_lname = tk.Entry(main_window, width=20)
entry_person_fname.grid(row=6, column=1, columnspan=2)
entry_person_lname.grid(row=6, column=3, columnspan=2)

# create labels for student major and startdate
lbl_student_major = tk.Label(main_window, text="Student Major")
lbl_student_startdate = tk.Label(main_window, text="Student Start Date")
lbl_student_major.grid(row=7, column=1, columnspan=2)
lbl_student_startdate.grid(row=7, column=3, columnspan=2)

# create entry boxes for student major and startdate
entry_student_major = tk.Entry(main_window, width=20)
entry_student_startdate = tk.Entry(main_window, width=20)
entry_student_major.grid(row=8, column=1, columnspan=2)
entry_student_startdate.grid(row=8, column=3, columnspan=2)

# add empty label for row 9
lbl_empty_row9 = tk.Label(main_window, text='')
lbl_empty_row9.grid(row=9, column=0)

# create View Person Table button
btn_view_person_tbl = tk.Button(main_window, text="View Person Table", command=lambda: display_person_table())
btn_view_person_tbl.grid(row=10, column=1)

# create View Student Table button
btn_view_student_tbl = tk.Button(main_window, text="View Student Table", command=lambda: display_student_table())
btn_view_student_tbl.grid(row=10, column=4)

# add empty label for row 11
lbl_empty_row11 = tk.Label(main_window, text='')
lbl_empty_row11.grid(row=11, column=0)

# add label for record insertion results
lbl_insert_results = tk.Label(main_window, text='')
lbl_insert_results.grid(row=12, column=1, columnspan=7)

# add empty label for row 13
lbl_empty_row13 = tk.Label(main_window, text='')
lbl_empty_row13.grid(row=13, column=0)

# create end/exit button
exit_button = tk.Button(main_window, text="Exit", width=25, command=main_window.destroy)
exit_button.grid(row=14, column=2, rowspan=1, columnspan=2)

'''
MODULE CODE ABOVE HERE
'''

# run main_window.mainloop()
main_window.mainloop()
