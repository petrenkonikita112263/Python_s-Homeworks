import random

"""
Exercise 2
For this exercise we will have several steps.

Create a class called GuessingGame.
The class doesn't need any user provided arguments for instantiation.
In the init method have the class set a self.rand_choice attribute
to a random integer between 0-10 (use import random)
Now create a method in the class called reset_random that will reset this self.rand_choice attribute
Now create a method called guess that uses the input() function to accept
a user guess for the random number. This method should print out a statement indicating whether
or not the user guess was correct. Bonus: Add logic that will report back
to the user to guess higher or lower next time they call the guess() method.
"""


class GuessingGame:
    # Create your methods here
    def __init__(self) -> None:
        self.rand_choice = random.randint(0, 10)

    def reset_random(self) -> None:
        print("Resetting Random Choice")
        self.__init__()

    def guess(self) -> None:
        user_number = int(input("Please input your guess (0-10): "))
        if user_number < self.rand_choice:
            print("Guess Lower!")
            self.guess()
        elif user_number > self.rand_choice:
            print("Guess High!")
            self.guess()
        else:
            print("Correct Guess!")
