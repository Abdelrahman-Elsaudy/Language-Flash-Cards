# Language Flash Cards

---

A flash-card game which shows you a word in French on a card then it's flipped after 3 seconds to show you its equivalent in English, 
if you know the word, you should press on the _right_ button and if you don't, you should press on the _wrong_ button, after you press on either one of them it moves to the next word.

![french_screenshot](https://github.com/Abdelrahman-Elsaudy/Language-Flash-Cards/assets/158151388/c096a668-6643-4163-8f20-58a7c958ac80)

![english_screenshot](https://github.com/Abdelrahman-Elsaudy/Language-Flash-Cards/assets/158151388/a4bd612a-8ec8-40ba-b543-45eee695cdbc)


When you press on the _right_ button for a word, it's removed from the list of words that are shown to you to make sure
you can focus on the ones you don't know.

The words that weren't shown to you yet and the ones you pressed the _wrong_ button for, are added to a separate csv file _unknown_words.csv_
which is used to run the app if you close the app and rerun it again.

---

## Applied Skills:

---
**1. Using Pandas Module**

- Reading the data inside the csv file of the words list.
- Writing the unknown words in a separate csv file.

**2. Exception Handling**

```
try:
    data = pandas.read_csv("./data/unknown_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
```
- To handle the error of not finding the unknown_words file when the user opens the app for the first time.

**3. Global Variables**

```
def game_on():
    global chosen_word, flip_timer
```
- Using global variables to summon variables inside a function and edit them then use them again in a different function.

**4. GUI with Tkinter Module**

- Creating interactive user-interface where the French side of the card is shown then it gets flipped to show the English
side, with right and wrong buttons for the user to categorize the words they know and the ones they need to memorize.

---

## Fixed Bugs:

---

- The user might know several words and wants to skip them fast without having to wait for each one to flip and show the English equivalent.
- If the user presses on the same button several times they still flip for each one pressed.
- To fix this we disable the flipping at the beginning of the function then define it again afterwards. 

```
def game_on():
    global chosen_word, flip_timer
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, show_card, chosen_word["English"])
```

---

## User Tips:

---

- To learn the words in a language that can get you by, you can use the most frequently used words instead of the alphabetic sequence.
- You can find a list of the most frequently used words for the language you want to learn on [Wikipedia](https://www.wikipedia.org/).
- Then you can use Google Sheets and GOOGLETRANSLATE command to translate them into the desired language, and use this csv file for this app.

---
_Credits to: 100-Days of Code Course on Udemy._