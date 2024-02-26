# ----------------------------- INTRO -----------------------------#


# The goal of this project is learning the most frequent 100 words in French using a flash card
# game which shows you the on the front the French word and after 3 seconds it is flipped
# to show you the English equivalent, if you know the word you press on the green button then it
# creates a csv file of the unknown words with the known one removed from it, and so on.
# Note: if you want to start from scratch, you can delete the unknown_words.csv file.


# ----------------------------- CODING -----------------------------#


from tkinter import *
import pandas
import random


try:
    data = pandas.read_csv("./data/unknown_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_dicts = data.to_dict(orient="records")      # To generate a list of dictionaries in each one we have the French
                                                 # word and its English equivalent.

chosen_word = data_dicts[random.randint(0, len(data_dicts)-1)]   # I used -1 because in randint both sides are included.

# ----------------------------- BUTTONS SETUP -----------------------------#


def known_word():
    global data_dicts
    data_dicts.remove(chosen_word)
    to_learn = pandas.DataFrame(data_dicts)
    to_learn.to_csv("./data/unknown_words.csv", index=False)
    game_on()


# ----------------------------- GAME ON -----------------------------#


def show_card(english_word):
    canvas.create_image(400, 263, image=back_card)
    canvas.create_text(400, 140, text="English", fill="white", font=("Helvetica", 22, "italic"))
    canvas.create_text(400, 230, text=english_word, fill="white", font=("Helvetica", 28, "bold"))


def game_on():
    global chosen_word, flip_timer
    window.after_cancel(flip_timer)
    chosen_word = data_dicts[random.randint(0, len(data_dicts)-1)]
    canvas.create_image(400, 263, image=front_card)
    canvas.create_text(400, 140, text="French", fill="black", font=("Helvetica", 22, "italic"))
    canvas.create_text(400, 230, text=chosen_word["French"], fill="black", font=("Helvetica", 28, "bold"))
    canvas.grid(column=1, row=0, columnspan=3, rowspan=3)
    flip_timer = window.after(3000, show_card, chosen_word["English"])
    print(len(data_dicts))                     # I added this to give you an indication of the words left to learn
                                               # and to test the efficiency of the buttons.


# ----------------------------- UI SETUP -----------------------------#


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Language Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")

known_pic = PhotoImage(file="./images/right.png")
known_button = Button(image=known_pic, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
known_button.grid(column=3, row=4)

unknown_pic = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_pic, bg=BACKGROUND_COLOR, command=game_on)
unknown_button.grid(column=1, row=4)

flip_timer = window.after(3000, show_card, chosen_word["English"])

game_on()

window.mainloop()
