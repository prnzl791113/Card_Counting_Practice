import os
import random
import tkinter as tk
from PIL import Image, ImageTk

# Definition of the Card class
class Card:
    def __init__(self, value, suit, count, image):
        self.value = value
        self.suit = suit
        self.count = count
        self.image = image

# Utility functions for directory and file operations
def filesInDir(directory):
    files = os.listdir(directory)
    files.remove('.DS_Store')
    return files

def classifier(file_name):
    arr = []
    for name in file_name:
        val, _, sui = name.split("_")
        sui = sui[:-4]
        count = -1
        if val.isdigit():
            count = 0 if int(val) > 6 and int(val) < 10 else (-1 if int(val) == 10 else 1)
        PCard = Card(val, sui, count, name)
        arr.append(PCard)
    return arr

# Initialize the deck
FILE_PATH = '_____' # Add your file path to the card images here
all_cards = filesInDir(FILE_PATH)
Deck = classifier(all_cards)

NUM_DECK = 0
try:
    NUM_DECK = int(input("Enter the number of deck in a shoe: "))
except ValueError:
    print("Enter a valid number")
totalDeck = [i for i in Deck for _ in range(NUM_DECK)]
random.shuffle(totalDeck)

# Global variables
current_count = 0
deck_remaining = NUM_DECK
totalCount = 0
current_card_index = 0

# GUI window setup
root = tk.Tk()
status_window = tk.Toplevel(root)
status_window.geometry('200x200')

# GUI components and their configuration
count_label = tk.Label(status_window, text=f"Current Count is: {totalCount}")
count_label.pack()
image_label = tk.Label(root)
image_label.pack()

# Functions related to GUI updates and event handling
def update_image():
    global totalCount, current_card_index, totalDeck

    card = totalDeck[current_card_index]
    print(card.suit, card.value, card.count, card.image, totalCount)
    totalCount += card.count

    path_to_image = FILE_PATH + card.image
    new_image = Image.open(path_to_image)
    photo = ImageTk.PhotoImage(new_image)
    image_label.config(image=photo)
    image_label.image = photo

    count_label.config(text=f"Current Count is {totalCount}")

    current_card_index += 1
    if current_card_index < len(totalDeck):
        root.after(1000, update_image)

def on_press(event):
    if event.char == 'q':
        print("Program terminated by user")
        root.destroy()

# Event bindings and main application loop
root.bind("<KeyPress>", on_press)
update_image()
print("Completed Execution")
root.mainloop()
