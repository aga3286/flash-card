from tkinter import *
import pandas as pd
import random
import os


if os.path.exists('data/words_to_learn.csv'):
    file_path = 'data/words_to_learn.csv'
else:
    file_path = 'data/french_words.csv'
df = pd.read_csv(file_path)
fr2eng = df.to_dict(orient='records')

chosen_word = None

def next_card():
    global chosen_word
    global flip_card_id
    window.after_cancel(flip_card_id)
    chosen_word = random.choice(fr2eng)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=chosen_word['French'], fill='black')
    canvas.itemconfig(front, image=card_front_img)
    flip_card_id = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(front, image=card_back_img)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=chosen_word['English'], fill='white')

def i_know():
    fr2eng.remove(chosen_word)
    df_to_learn = pd.DataFrame(fr2eng)
    df_to_learn.to_csv('data/words_to_learn.csv', index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_card_id = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
front = canvas.create_image(407, 270, image=card_front_img)
title =canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'))


wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=i_know)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
