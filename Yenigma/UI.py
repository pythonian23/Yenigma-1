#  from Yenigma import Yenigma, Enigma
import tkinter as tk
from tkinter import ttk


class Lamp:
    def __init__(self, text, loc):
        self.body = tk.Label(subFrame[loc[1]], text=text, bg="black", fg="#aaaaaa", font=("Arial", 24, "bold"), padx=20, pady=10)
        self.body.grid(row=0, column=loc[0])


def main():
    pass


root = tk.Tk()
root.title("Yenigma")

root.config(background="#dddddd")
root.resizable(False, False)

m = tk.Frame(root)

m.pack()

lamps = [[], [], []]
qwerty = ("QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM")
lampBoard = tk.Frame(m, bg="black")
subFrame = [tk.Frame(lampBoard), tk.Frame(lampBoard), tk.Frame(lampBoard)]
for line in range(len(qwerty)):
    for letter in range(len(qwerty[line])):
        lamps[line].append(None)
        lamps[line][-1] = Lamp(qwerty[line][letter], (letter, line))

for frame in subFrame:
    frame.pack(fill="none", expand=True)

lampBoard.pack()


optionBoard = tk.Frame(m, bg="#dddddd")

version = tk.StringVar()
version.set("Enigma")

chooseVersion = tk.Frame(optionBoard, pady=5, bg="#dddddd")
menu = ttk.OptionMenu(chooseVersion, version, "Enigma", "Yenigma", "Enigma")
SetVersion = tk.Button(optionBoard, text="Reset")

menu.pack()

chooseVersion.grid(row=0, column=0)
optionBoard.pack(fill=tk.BOTH)

SetVersion.grid(row=0, column=1)


root.mainloop()


main()
