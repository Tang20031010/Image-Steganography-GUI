from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import os
from stegano import lsb

root = Tk()
root.title("Image Steganography")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#eee9e9")

def show_image():
    global filename
    filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select Image File', filetypes= (("PNG file", "*.png"), ("JPG file", "*.jpg"), ("JPEG file", "*.jpeg"), ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    l1.configure(image = img, width = 250, height = 250)
    l1.image = img

def hide ():
    global secret
    message = txt1.get("1.0", END)
    secret = lsb.hide(str(filename), message)

def save():
    temp = txt2.get("1.0","end-1c")
    secret.save(temp)

def show():
    clear_message = lsb.reveal(filename)
    txt1.delete(1.0, END)
    txt1.insert(END, clear_message)

def reset_all():
    txt1.delete("1.0", END)
    txt2.delete("1.0", END)
    l1.config(image = '')

Label(root, text = "IMAGE STEGANOGRAPHY", bg= "#eee9e9", fg= "black", font = ("Times", "24", "bold")).place(x =10, y = 20)

f1 = Frame(root, bd = 3, bg = "gray", width = 340, height = 280, relief=GROOVE)
f1.place(x = 10, y = 80)

l1 = Label(f1, bg = "gray")
l1.place(x = 40, y = 10)


f2 = Frame(root, bd = 3, width = 340, height = 210, bg = "white", relief=GROOVE)
f2.place(x = 350, y = 80)

txt1 = Text(f2, font=("Times", "20", "bold"), bg="white", fg = "black", relief=SUNKEN, wrap = WORD)
txt1.place(x = 0, y = 25, width = 320, height = 180)



Label(f2, text = "Input/Output of Secret Message", bg = "black", fg = "white").place(x = 0, y = 2)



f3 = Frame(root, bd = 3, bg = "#eee9e9", width = 330, height = 100, relief=RAISED)
f3.place(x=10, y = 370)

Button(f3, text = "Select Image", width = 10, height = 2, font = ("Times", "14", "bold"), command = show_image).place(x = 20, y = 30)
Button(f3, text = "Save Image", width = 10, height = 2, font = ("Times", "14", "bold"), command = save).place(x = 180, y = 30)
Label(f3, text = "Image file", bg = "#eee9e9", fg = "black").place(x = 20, y = 5)

sb1 = Scrollbar(f2)
sb1.place(x = 320, y = 0, height = 245)

sb1.configure(command = txt1.yview)
txt1.configure(yscrollcommand=sb1.set)


f4 = Frame(root, bd = 3, bg = "#eee9e9", width = 330, height = 100, relief=RAISED)
f4.place(x=360, y = 370)

Button(f4, text = "Hide Message", width = 10, height = 2, font = ("Times", "14", "bold"), command = hide).place(x = 20, y = 30)
Button(f4, text = "Show Message", width = 10, height = 2, font = ("Times", "14", "bold"), command = show).place(x = 180, y = 30)
Label(f4, text = "Hide Message", bg = "#eee9e9", fg = "black").place(x = 20, y = 5)


f5 = Frame(root, bd = 3, width = 340, height = 60, bg = "white", relief=GROOVE)
f5.place(x = 350, y = 300)
txt2 = Text(f5, font = ("Times", "12", "bold"), bg = "white", fg = "black", relief = SUNKEN, wrap = WORD)
txt2.place(x = 0, y = 25, width = 320, height = 25)
Label(f5, text = "Input of Output File Name", bg = "black", fg = "white").place(x = 0, y = 0)

f6 = Frame(root, bd = 3, width = 130, height = 55, bg = "white", relief = GROOVE)
f6.place(x = 540, y = 20)
Button(f6, text = "Reset", width = 10, height = 2, font = ("Times", "14", "bold"), command = reset_all).place(x = 4, y = 1)
root.mainloop()