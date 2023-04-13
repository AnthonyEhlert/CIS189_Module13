"""
Program: NumberGuesser.py
Author: Tony Ehlert
Last date modified: 4/7/2023

The purpose of this program is to define a NumberGuesser class that is to be used as part of a number guessing GUI game.

The input is the required information and code to define the class and its methods
The output is prints to the console of the object's info or method results
"""
import random
from Topic1.constants import MAX


class NumberGuesser():
    """NumberGuesser class"""

    def __init__(self):
        self._guessed_list = []
        self._random_num = random.randint(1, MAX)

    def add_guess(self, guess):
        """
        This method adds the number guessed(guess) to the guessed_list and returns a boolean value indicating if
        the guessed number matches the random_num value
        :param guess: int number of guess
        :return: boolean indicating guess matches random_num value
        """
        try:
            guess_as_int = int(guess)
            if (guess_as_int < 1 or guess_as_int > MAX):
                raise ValueError
            else:
                self._guessed_list.append(guess)
                if guess_as_int == self._random_num:
                    return True
                else:
                    return False
        except ValueError:
            print(f"Invalid Guess! Guess must be a whole number between 1 and {MAX}")
            raise ValueError

    def __str__(self):
        return "Guessed List: " + str(self._guessed_list) + ", Correct Number: " + str(self._random_num)

# driver/main()
# if __name__ == "__main__":
#     # create NumberGuesser object
#     number_guesser = NumberGuesser()
#
#     # print statement to check for proper random int generation in object
#     print(number_guesser._random_num)
#
#     # create guessed_num variable from input
#     guessed_num = input("Enter your guess: ")
#
#     try:
#         winner = number_guesser.add_guess(guessed_num)
#     except ValueError:
#         winner = False
#
#     while winner == False:
#         print(number_guesser)
#         guessed_num = input("Incorrect! Enter your next guess: ")
#         try:
#             winner = number_guesser.add_guess(guessed_num)
#         except ValueError:
#             winner = False
#
#     print("CORRECT!")
#     print(number_guesser)
#
#     # garbage collection
#     del number_guesser
