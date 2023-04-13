"""
Program: number_guesser.gui
Author: Tony Ehlert
Last date modified: 4/12/2023

The purpose of this program is generate a GUI that creates a NumberGuesser object and allows the user to play a
number guessing game

The input is data needed to create and run the GUI along with user input via mouse clicks
The output is GUI displays of the game results
"""
import tkinter as tk
from tkinter.constants import *
from tkinter import messagebox

from Topic1.NumberGuesser import NumberGuesser

'''
FUNCTIONS BELOW HERE
'''
number_guesser = NumberGuesser()


def enable_game():
    number_guesser._guessed_list = []
    nums_guessed_lbl.config(text=("Numbers Guessed: " + str(number_guesser._guessed_list)))
    for btn in num_buttons:
        btn.config(state=NORMAL)


def click_guess(guess, btn_clicked):
    if number_guesser.add_guess(guess):
        tk.messagebox.showinfo("Winner", "YOU GUESSED CORRECTLY")
        number_guesser._guessed_list = []
        nums_guessed_lbl.config(text=("Numbers Guessed: " + str(number_guesser._guessed_list)))
        for btn in num_buttons:
            btn.config(state=NORMAL)
    else:
        btn_clicked.config(state=DISABLED)
        nums_guessed_lbl.config(text=("Numbers Guessed: " + str(number_guesser._guessed_list)))


'''
FUNCTIONS ABOVE HERE
'''

# create main window
main_window = tk.Tk()

'''
MODULE CODE BELOW HERE
'''

# set title of main_window
main_window.title("Number Guessing Game")

# set default size of main window
main_window.geometry("300x300")

# create start button
start_btn = tk.Button(main_window, text="START", width=25, command=lambda: enable_game())
start_btn.grid(row=1, column=1, rowspan=1, columnspan=3)

# create choice buttons
num_buttons = []

btn_num_one = tk.Button(main_window, text='1', state=DISABLED, command=lambda: click_guess(1, btn_num_one))
btn_num_one.grid(row=3, column=1)
num_buttons.append(btn_num_one)

btn_num_two = tk.Button(main_window, text='2', state=DISABLED, command=lambda: click_guess(2, btn_num_two))
btn_num_two.grid(row=3, column=2)
num_buttons.append(btn_num_two)

btn_num_three = tk.Button(main_window, text='3', state=DISABLED, command=lambda: click_guess(3, btn_num_three))
btn_num_three.grid(row=3, column=3)
num_buttons.append(btn_num_three)

btn_num_four = tk.Button(main_window, text='4', state=DISABLED, command=lambda: click_guess(4, btn_num_four))
btn_num_four.grid(row=4, column=1)
num_buttons.append(btn_num_four)

btn_num_five = tk.Button(main_window, text='5', state=DISABLED, command=lambda: click_guess(5, btn_num_five))
btn_num_five.grid(row=4, column=2)
num_buttons.append(btn_num_five)

btn_num_six = tk.Button(main_window, text='6', state=DISABLED, command=lambda: click_guess(6, btn_num_six))
btn_num_six.grid(row=4, column=3)
num_buttons.append(btn_num_six)

btn_num_seven = tk.Button(main_window, text='7', state=DISABLED, command=lambda: click_guess(7, btn_num_seven))
btn_num_seven.grid(row=5, column=1)
num_buttons.append(btn_num_seven)

btn_num_eight = tk.Button(main_window, text='8', state=DISABLED, command=lambda: click_guess(8, btn_num_eight))
btn_num_eight.grid(row=5, column=2)
num_buttons.append(btn_num_eight)

btn_num_nine = tk.Button(main_window, text='9', state=DISABLED, command=lambda: click_guess(9, btn_num_nine))
btn_num_nine.grid(row=5, column=3)
num_buttons.append(btn_num_nine)

btn_num_ten = tk.Button(main_window, text='10', state=DISABLED, command=lambda: click_guess(10, btn_num_ten))
btn_num_ten.grid(row=6, column=2)
num_buttons.append(btn_num_ten)

# create end/exit button
exit_button = tk.Button(main_window, text="Exit", width=25, command=main_window.destroy)
exit_button.grid(row=8, column=1, rowspan=1, columnspan=3)

# create label for numbers guessed
nums_guessed_lbl = tk.Label(main_window, text=("Numbers Guessed: " + str(number_guesser._guessed_list)))
nums_guessed_lbl.grid(row=9, column=1, rowspan=1, columnspan=4)

'''
MODULE CODE ABOVE HERE
'''

# run main_window.mainloop()
main_window.mainloop()
