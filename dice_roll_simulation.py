import tkinter as tk
from PIL import Image, ImageTk
import random

#creates window to show
window = tk.Tk()
window.geometry("750x560")
window.title("Dice Roll")



dice=["1.png","2.png","3.png","4.png","5.png","6.png"]

image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image1)

label1.image=image1
label2.image=image2

label1.place(x=0, y=100)
label2.place(x=400, y=100)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1

    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2


button=tk.Button(window, text="Roll", bg="green", fg="white", font="Times 20 bold", command=dice_roll)

button.place(x=330,y=0)


window.mainloop()