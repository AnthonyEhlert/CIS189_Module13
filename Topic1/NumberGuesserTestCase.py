"""
Program: NumberGuesserTestCase.py
Author: Tony Ehlert
Last date modified: 4/12/2023

The purpose of this program is to test the NumberGuesser class and its methods
The input is tests and necessary variables to test the NumberGuesser class
The output is results of tests
"""
import unittest

from Topic1.NumberGuesser import NumberGuesser
from Topic1.constants import MAX


class NumberGuesserTestCase(unittest.TestCase):
    def setUp(self):
        self.number_guesser = NumberGuesser()

    def tearDown(self):
        del self.number_guesser

    def test_object_created(self):
        self.assertTrue(len(self.number_guesser._guessed_list) == 0)
        self.assertTrue(self.number_guesser._random_num in range(1, MAX + 1))

    def test_add_guess_match(self):
        # manually set self._random_num variable
        self.number_guesser._random_num = 1

        self.assertTrue(self.number_guesser.add_guess(1))
        self.assertEqual(self.number_guesser._guessed_list, [1])

    def test_add_guess_no_match(self):
        # manually set self._random_num variable
        self.number_guesser._random_num = 2

        self.assertFalse(self.number_guesser.add_guess(1))
        self.assertEqual(self.number_guesser._guessed_list, [1])

    def test_add_guesses(self):
        # manually set self._random_num variable
        self.number_guesser._random_num = 10

        self.assertFalse(self.number_guesser.add_guess(1))
        self.assertFalse(self.number_guesser.add_guess(2))
        self.assertFalse(self.number_guesser.add_guess(4))
        self.assertFalse(self.number_guesser.add_guess(3))
        self.assertTrue(self.number_guesser.add_guess(10))
        self.assertEqual(self.number_guesser._guessed_list, [1, 2, 4, 3, 10])

    def test_add_guess_invalid_input(self):
        with self.assertRaises(ValueError):
            self.number_guesser.add_guess('abc')
        with self.assertRaises(ValueError):
            self.number_guesser.add_guess('-1')
        with self.assertRaises(ValueError):
            self.number_guesser.add_guess('11')
        with self.assertRaises(ValueError):
            self.number_guesser.add_guess('1.1')

    def test_str(self):
        # manually set self._random_num variable
        self.number_guesser._random_num = 10

        self.assertFalse(self.number_guesser.add_guess(1))
        self.assertEqual(self.number_guesser.__str__(), "Guessed List: [1], Correct Number: 10")


if __name__ == "__main__":
    NumberGuesserTestCase.main()
