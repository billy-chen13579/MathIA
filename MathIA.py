import tkinter as tk
import random

class DiceRollerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Roller")
        self.geometry("300x300")
        
        self.side1_label = tk.Label(self, text="Side 1")
        self.side1_label.grid(row=0, column=0)
        self.side1_entry = tk.Entry(self)
        self.side1_entry.insert(0, "1")
        self.side1_entry.grid(row=0, column=1)
        
        self.side2_label = tk.Label(self, text="Side 2")
        self.side2_label.grid(row=1, column=0)
        self.side2_entry = tk.Entry(self)
        self.side2_entry.insert(0, "2")
        self.side2_entry.grid(row=1, column=1)
        
        self.side3_label = tk.Label(self, text="Side 3")
        self.side3_label.grid(row=2, column=0)
        self.side3_entry = tk.Entry(self)
        self.side3_entry.insert(0, "3")
        self.side3_entry.grid(row=2, column=1)
        
        self.side4_label = tk.Label(self, text="Side 4")
        self.side4_label.grid(row=3, column=0)
        self.side4_entry = tk.Entry(self)
        self.side4_entry.insert(0, "4")
        self.side4_entry.grid(row=3, column=1)
        
        self.side5_label = tk.Label(self, text="Side 5")
        self.side5_label.grid(row=4, column=0)
        self.side5_entry = tk.Entry(self)
        self.side5_entry.insert(0, "5")
        self.side5_entry.grid(row=4, column=1)
        
        self.side6_label = tk.Label(self, text="Side 6")
        self.side6_label.grid(row=5, column=0)
        self.side6_entry = tk.Entry(self)
        self.side6_entry.insert(0, "6")
        self.side6_entry.grid(row=5, column=1)
        
        self.roll_button = tk.Button(self, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=6, column=1)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=7, column=1)
        
    def roll_dice(self):
        sides = [int(self.side1_entry.get()), int(self.side2_entry.get()), int(self.side3_entry.get()), 
                 int(self.side4_entry.get()), int(self.side5_entry.get()), int(self.side6_entry.get())]
        
        result = random.choice(sides)
        self.result_label.configure(text="You rolled a " + str(result))
        

if __name__ == '__main__':
    app = DiceRollerGUI()
    app.mainloop()
