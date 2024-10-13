import tkinter as tk
import random
import time

class RPGDiceRoller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RPG Dice Roller")
        self.geometry("600x300")
        self.configure(bg="#2d2d2d")

        # Label to display the result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 40), fg="white", bg="#2d2d2d")
        self.result_label.pack(pady=50)

        # Button for each dice type
        self.create_dice_buttons()

    def create_dice_buttons(self):
        dice_types = [4, 6, 8, 10, 12, 20]
        button_frame = tk.Frame(self, bg="#2d2d2d")
        button_frame.pack(pady=20)

        for dice in dice_types:
            btn = tk.Button(button_frame, text=f"W{dice}", font=("Helvetica", 20),
                            command=lambda d=dice: self.roll_dice(d), bg="#4caf50", fg="white")
            btn.pack(side=tk.LEFT, padx=10)

    def roll_dice(self, dice_type):
        # Animation for rolling the dice
        for _ in range(10):
            self.result_label.config(text=str(random.randint(1, dice_type)))
            self.update()
            time.sleep(0.1)

        # Final result
        result = random.randint(1, dice_type)
        self.result_label.config(text=str(result))

if __name__ == "__main__":
    app = RPGDiceRoller()
    app.mainloop()
