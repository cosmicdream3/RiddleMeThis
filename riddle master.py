import random
from tkinter import *

# (Lower & upper limit) questions
MAX = 8
MIN = 1



class Application(Frame):
    """The GUI application (Riddle Me This)."""

    __slots__ = "number", "tries", "question", "ans", "qlabel", "list_done"

    def __init__(self, master):
        """Initialize Frame."""
        Frame.__init__(self, master)

        master.minsize(width=500, height=200)

        self.list_done = []

        self.qlabel = Label(self)

        self.grid()

        self.reset()

    def set_game(self):
        qno = self.number

        self.list_done.append(qno)

        if self.number == 1:
            self.question = "The word 'elloh'is jumbled. Guess the right word."
            self.ans = "hello"
        elif self.number == 2:
            self.question = "Forwards I am heavy. Backwards I am not. What am I?"
            self.ans = "ton"

        elif self.number == 3:
            self.question = "black white and read all over?"
            self.ans = "news paper"

        elif self.number == 4:
            self.question = "What has words, but never speaks??"
            self.ans = "book"

        elif self.number == 5:
            self.question = "What has a head and a tail but no body?"
            self.ans ="coin"

        elif self.number == 6:
            self.question = "What loses its head every morning and gets it back every night?"
            self.ans ="pillow"


        elif self.number == 7:
            self.question = "It stalks the countryside with ears that can’t hear. What is it?"
            self.ans ="corn"


        elif self.number == 8:
            self.question = " I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?"
            self.ans ="shadow"


    def create_widgets(self):
        """Program all the widgets to be used."""
        if self.qlabel is not None:
            self.qlabel.grid_forget()

        self.qlabel = Label(self, text = self.question)

        self.qlabel.grid(row=0, column=0, columnspan=2, sticky=W)

        #Label(self, text = self.question).grid(row=0, column=0, columnspan=2, sticky=W)
        #Aligns widgets in certain location

        Label(self,
              text="Try to guess the answer"
              ).grid(row=1, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Rounds done : 0"
              ).grid(row=0, column=2, columnspan=1, sticky=W)

        Label(self,
              text="Guess"
              ).grid(row=2, column=0, sticky=W)


        # Entry widget to allow guessing
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        # Submit button to obtain guess
        Button(self,
               text="Enter",
               command=self.get_guess
               ).grid(row=2, column=2, columnspan=4, sticky=W)
        Button(self,
               text="Reset",
               command=self.reset
               ).grid(row=1, column=2, columnspan=1, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=3, column=0, columnspan=3)

    def get_guess(self):
        """Obtain the player's guess and verify it."""
        try:
            guess = str(self.guess_ent.get())
        except(ValueError):
            self.display_message("Invalid entry. Try again.")
        else:
            self.tries += 1
            if self.tries == 10:
                self.display_message("You win!!")
                self.guess_ent.grid_forget()
                #Label(self, text="     You won!!                    ").grid(row=3, column=0, columnspan=3)
                #print("You won!!")
                #exit(0)
            Label(self,
                  text="Rounds done : " + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)
            self.check_guess(guess)

    def next_question(self):

        self.number = random.randrange(MIN, MAX + 1)
        while self.number in self.list_done:
            self.number = random.randrange(MIN, MAX + 1)

        self.set_game()

        #Label(self, text="                                       ").grid(row=0, column=0, columnspan=2, sticky=W)

        self.qlabel.grid_forget()

        self.qlabel = Label(self, text=self.question)

        #Label(self, text=self.question).grid(row=0, column=0, columnspan=2, sticky=W)

        self.qlabel.grid(row=0, column=0, columnspan=2, sticky=W)


        #self.qlabel.text = self.question

    def check_guess(self, guess):
        """
        Verify if the player's guess is correct.
        Keyword argument:
        guess - the int value to be verified
        """

        if self.ans in guess.lower() :
            self.next_question()
            self.display_message("Correct (clear and answer next question)")
            return

        else:
            self.display_message("Wrong! Game Over!")
            self.guess_ent.grid_forget()
            #Label(self, text = "     Wrong Answer. Game Over!     ").grid(row=3, column=0, columnspan=3)
            #print("Wrong Answer. Game Over!")
            #exit(0)
            return

        '''if guess < MIN or guess > MAX:
            self.display_message("Invalid Input, Guess Out Side Of Range.")
            self.tries -= 1  # This try doesn't count
            return
        # If guess equals the number, end current game.
        if guess == self.number:
            self.resetgame()
            return
        # Otherwise, see if guess is higher or lower than the chosen number.
        if guess < self.number:
            self.display_message("Guess Higher...")
            return
        elif guess > self.number:
            self.display_message("Guess Lower...")
            return
        '''



    def display_message(self, message):
        """
        Display a message on the text box.
        Keyword argument:
        message -- the message to be displayed
        """
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

    def reset(self):
        """Prepare for a new game."""
        # Word to be guessed by player.
        self.number = random.randrange(MIN, MAX + 1)
        while self.number in self.list_done:
            self.number = random.randrange(MIN, MAX + 1)

        self.tries = 0

        self.set_game()

        self.create_widgets()
        '''self.number = random.randrange(MIN, MAX + 1)
        self.display_message("Game Reset. Please enter another number to play again.")
        self.tries = 0
        Label(self,
              text="Number Of Tries: " + str(self.tries)
              ).grid(row=0, column=2, columnspan=1, sticky=W)'''
    def resetgame(self):
        self.display_message("Congrats! You guessed correctly. The number was " + \
                             str(self.number) + ". And it only took you " + \
                             str(self.tries) + " tries!" + " Click The Reset Button To Play Again" )


def main():
    """Kickstart Riddle Me This."""
    root = Tk()
    root.title("Riddle Master ")
    app = Application(root)
    root.mainloop()



# start Riddle Me This
main()
