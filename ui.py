from tkinter import *
import random

BACKGROUND_COLOR = "#7491d4"


class AppUI:
    def __init__(self, quotes):
        self.quotes = quotes
        self.root = Tk()
        self.root.title("Words of Wisdom")
        self.root.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.canvas = Canvas(width=400, height=250, bg="white", highlightthickness=0)
        self.quote_text = self.canvas.create_text(200, 125, text="Quote", width=300, font=("Arial", 20, "italic"),
                                                  fill="black")
        self.author_text = self.canvas.create_text(200, 200, text="Author", font=("Arial", 15, "bold"), fill="black")
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.new_quote = Button(text="New Quote", command=self.get_quote, highlightthickness=0,
                                font=("Arial", 18, "bold"),
                                bg=BACKGROUND_COLOR, borderwidth=0)
        self.spacer = Label(text=" ", bg=BACKGROUND_COLOR)
        self.spacer.grid(row=1, column=0)
        self.new_quote.grid(row=2, column=0, columnspan=2)

        self.label= Label(text="Made by: Benjamin Rifleman 2022", bg=BACKGROUND_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.label.grid(row=3, column=0, columnspan=2)

        # mke window have a minimum size
        self.root.minsize(500, 400)
        self.get_quote()


        self.root.mainloop()

    def get_quote(self):
        quote = random.choice(self.quotes)
        self.canvas.itemconfig(self.quote_text, text=quote["text"])
        self.canvas.itemconfig(self.author_text, text=quote["author"])
