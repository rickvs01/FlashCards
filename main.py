from tkinter import *

import pandas
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")



# ----------------------------- IS KNOWN --------------------------- #
def is_known() :
    data_dict.remove(current_card)
    random_word()
    new_list = pandas.DataFrame(data_dict)
    new_list.to_csv("data/words_to_learn.csv", index=False)


# ----------------------------- FLIP CARD -------------------------- #
def flip_card() :
    global current_card, flip_timer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image=CARD_BACK)
    #flip_timer = window.after(3000, func=flip_card)


# ------------------------------ RANDOM WORD ------------------------ #
def random_word() :
    global flip_timer
    global current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill ="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=CARD_FRONT)
    flip_timer = window.after(6000, func= flip_card)

# ----------------------------- UI SETUP ------------------------------ #
window = Tk()

CARD_FRONT = PhotoImage(file="images/card_front.png")
CARD_BACK = PhotoImage(file="images/card_back.png")
CORRECT = PhotoImage(file="images/right.png")
INCORRECT = PhotoImage(file="images/wrong.png")

window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_background = canvas.create_image(400, 263, image=CARD_FRONT)
card_title = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(column=0, row=1, columnspan=2)

# Labels
# Language_Label = Label(text="French", font=LANGUAGE_FONT, bg="white")
# Language_Label.grid(column=0, row=1,columnspan=2, sticky ="n")
# Buttons

Correct_button = Button(image=CORRECT, highlightthickness=0, command=is_known)
Correct_button.grid(column=1, row=2)

Incorrect_button = Button(image=INCORRECT, highlightthickness=0, command=random_word)
Incorrect_button.grid(column=0, row=2)

random_word()
window.mainloop()
