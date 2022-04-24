import tkinter as tk
import tkinter.messagebox as msgbox
import itertools as it
import copy
import random as rd
class game_gui:
    def __init__(self, root, length=5, guesses=6):
        self.g = game()
        self.guesses = guesses
        self.length = length

        self.frame = tk.Frame(root, bg="#121213")
        self.frame.pack(pady=20)
        self.labels = [[tk.Label(self.frame, text="", borderwidth=4, relief=tk.RIDGE, width=9, height=4, fg="white", bg="#121213") for _ in range(self.length)] for _ in range(self.guesses)]
        for i, j in it.product(range(self.guesses), range(self.length)):
            self.labels[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="NESW")

        values = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "⌫"]]
    
        self.frame2 = tk.Frame(root, width=1000, height=400, bg="#121213")
        self.frame2.pack(pady=20, side=tk.BOTTOM)
        self.buttons = [[tk.Button(self.frame2, text=letter, width=6, height=4, fg="white", bg="#818384", borderwidth=0) for letter in value] for value in values]
        self.buttons[0][0].configure(command=lambda: self.input("Q"))
        self.buttons[0][1].configure(command=lambda: self.input("W"))
        self.buttons[0][2].configure(command=lambda: self.input("E"))
        self.buttons[0][3].configure(command=lambda: self.input("R"))
        self.buttons[0][4].configure(command=lambda: self.input("T"))
        self.buttons[0][5].configure(command=lambda: self.input("Y"))
        self.buttons[0][6].configure(command=lambda: self.input("U"))
        self.buttons[0][7].configure(command=lambda: self.input("I"))
        self.buttons[0][8].configure(command=lambda: self.input("O"))
        self.buttons[0][9].configure(command=lambda: self.input("P"))
        self.buttons[1][0].configure(command=lambda: self.input("A"))
        self.buttons[1][1].configure(command=lambda: self.input("S"))
        self.buttons[1][2].configure(command=lambda: self.input("D"))
        self.buttons[1][3].configure(command=lambda: self.input("F"))
        self.buttons[1][4].configure(command=lambda: self.input("G"))
        self.buttons[1][5].configure(command=lambda: self.input("H"))
        self.buttons[1][6].configure(command=lambda: self.input("J"))
        self.buttons[1][7].configure(command=lambda: self.input("K"))
        self.buttons[1][8].configure(command=lambda: self.input("L"))
        self.buttons[2][0].configure(command=lambda: self.enter())
        self.buttons[2][1].configure(command=lambda: self.input("Z"))
        self.buttons[2][2].configure(command=lambda: self.input("X"))
        self.buttons[2][3].configure(command=lambda: self.input("C"))
        self.buttons[2][4].configure(command=lambda: self.input("V"))
        self.buttons[2][5].configure(command=lambda: self.input("B"))
        self.buttons[2][6].configure(command=lambda: self.input("N"))
        self.buttons[2][7].configure(command=lambda: self.input("M"))
        self.buttons[2][8].configure(command=lambda: self.backspace())
        try:
            import keyboard as kb
            kb.on_press_key("q", lambda e: self.input("Q"))
            kb.on_press_key("w", lambda e: self.input("W"))
            kb.on_press_key("e", lambda e: self.input("E"))
            kb.on_press_key("r", lambda e: self.input("R"))
            kb.on_press_key("t", lambda e: self.input("T"))
            kb.on_press_key("y", lambda e: self.input("Y"))
            kb.on_press_key("u", lambda e: self.input("U"))
            kb.on_press_key("i", lambda e: self.input("I"))
            kb.on_press_key("o", lambda e: self.input("O"))
            kb.on_press_key("p", lambda e: self.input("P"))
            kb.on_press_key("a", lambda e: self.input("A"))
            kb.on_press_key("s", lambda e: self.input("S"))
            kb.on_press_key("d", lambda e: self.input("D"))
            kb.on_press_key("f", lambda e: self.input("F"))
            kb.on_press_key("g", lambda e: self.input("G"))
            kb.on_press_key("h", lambda e: self.input("H"))
            kb.on_press_key("j", lambda e: self.input("J"))
            kb.on_press_key("k", lambda e: self.input("K"))
            kb.on_press_key("l", lambda e: self.input("L"))
            kb.on_press_key("enter", lambda e: self.enter())
            kb.on_press_key("z", lambda e: self.input("Z"))
            kb.on_press_key("x", lambda e: self.input("X"))
            kb.on_press_key("c", lambda e: self.input("C"))
            kb.on_press_key("v", lambda e: self.input("V"))
            kb.on_press_key("b", lambda e: self.input("B"))
            kb.on_press_key("n", lambda e: self.input("N"))
            kb.on_press_key("m", lambda e: self.input("M"))
            kb.on_press_key("backspace", lambda e: self.backspace())
        except ImportError:
            pass

        for i in range(len(values)):
            for j in range(len(values[i])):
                if i==0:
                    self.buttons[i][j].grid(row=i, column=j*2, columnspan=2, padx=3, pady=3, sticky="NESW")
                elif i==1:
                    self.buttons[i][j].grid(row=i, column=j*2+1, columnspan=2, padx=3, pady=3, sticky="NESW")
                else:
                    if j==0:
                        self.buttons[i][j].grid(row=i, column=j*2, columnspan=3, padx=3, pady=3, sticky="NESW")
                    elif j==8:
                        self.buttons[i][j].grid(row=i, column=j*2+1, columnspan=3, padx=3, pady=3, sticky="NESW")
                    else:
                        self.buttons[i][j].grid(row=i, column=j*2+1, columnspan=2, padx=3, pady=3, sticky="NESW")


    def input(self, arg):
        if self.g.location[1] < self.length:
            print(arg)
            self.labels[self.g.location[0]][self.g.location[1]].configure(text=arg)
            self.g.guess[self.g.location[1]] = arg
            self.g.location[1] += 1

    def enter(self):
        if len(self.g.guess) == len(self.g.word) and "" not in self.g.guess:
            print(self.g.guess)
            if("".join(self.g.guess) not in self.g.words):
                msgbox.showwarning(title="Error", message=f"{''.join(self.g.guess)} not in word list.")
                return
            results = self.g.compare()
            for i in range(self.length):
                if results[i] == 0:
                    self.labels[self.g.location[0]][i].configure(bg="#3a3a3c")
                elif results[i] == 1:
                    self.labels[self.g.location[0]][i].configure(bg="#b59f3b")
                elif results[i] == 2:
                    self.labels[self.g.location[0]][i].configure(bg="#538d4e")

            for i in self.buttons:
                for j in i:
                    if j.cget("text") in self.g.green:
                        j.configure(bg="#3a3a3c")
                    elif j.cget("text") in self.g.yellow:
                        j.configure(bg="#b59f3b")
                    elif j.cget("text") in self.g.black:
                        j.configure(bg="#538d4e")


            self.g.location[0] += 1
            self.g.location[1] = 0
            self.g.guess = [""]*len(self.g.word)

            again = None
            if(sum(results) == 10):
                again = msgbox.askquestion(title="Congratulations", message=f"You won in {self.g.location[0]} guesses. Would you like to play again?")
            elif self.g.location[0] >= self.guesses:
                again = msgbox.askquestion(title="You Lost", message=f"You lost! The word was {''.join(self.g.word)}. Would you like to play again?")

            if again == "yes":
                print(again)
                self.g = game()
                self.frame.destroy()
                self.frame2.destroy()
                self.__init__(root)
            elif again == "no":
                print(False)
                root.destroy()
    def backspace(self):
        if self.g.location[1] > 0:
            print("bs")
            if(self.g.location[1] == self.length):
                self.g.location[1] -= 1
                self.g.guess[self.g.location[1]] = ""
                self.labels[self.g.location[0]][self.g.location[1]].configure(text="")
            else:
                self.g.guess[self.g.location[1]] = ""
                self.g.location[1] -= 1
                self.labels[self.g.location[0]][self.g.location[1]].configure(text="")
        
class game:
    def __init__(self):
        with open("targets.txt") as f:
            self.targets = [x.strip() for x in f.readlines()]
        with open("words.txt") as f:
            self.words = [x.strip() for x in f.readlines()]
        self.word = [*rd.choice(self.targets)]
        self.location = [0, 0]
        self.guess = [""]*len(self.word)
        self.unused = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.black = ""
        self.yellow = ""
        self.green = ""
    def compare(self):
        temp = [0]*len(self.word)
        word_temp = copy.deepcopy(self.word)
        guess_temp = copy.deepcopy(self.guess)
        for index, letter in enumerate(guess_temp):
            if letter == word_temp[index]:
                temp[index] = 2
                word_temp[index] = "-" 
                guess_temp[index] = "-"
        for index, letter in enumerate(guess_temp):
            if letter != "-" and letter in word_temp:
                temp[index] = 1
                word_temp[index] = "-" 
                guess_temp[index] = "-"
        
        for guess, value in zip(self.guess, temp):
            if value == 0:
                self.unused = self.unused.replace(guess, "")
                self.black += guess
            elif value == 1:
                self.unused = self.unused.replace(guess, "")
                self.yellow += guess
            elif value == 2:
                self.unused = self.unused.replace(guess, "")
                self.yellow = self.yellow.replace(guess, "")
                self.green += guess
        return temp

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wordle")
    root.state("zoomed")
    root.configure(bg="#121213")
    g = game_gui(root)
    root.mainloop()