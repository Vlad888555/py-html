from PIL import Image as PilImage, ImageDraw, ImageFont
from tkinter import *
from tkinter import filedialog
import textwrap
#pip install pillow

def add_foto():
    text = text_add.get()
    foto = filedialog.askopenfilename(title="Выберите файл", filetypes=[("All Files", "*.*")])
    im1 = PilImage.new('RGB', (500, 600), (255, 255, 255))
    im2 = PilImage.open(foto)


    a = ('\n'.join(textwrap.wrap(text, width=60)))
    im2_size = im2.resize((425, 425))
    im1.paste(im2_size, (35, 10))
    im1.save("hoto.jpg", quality=90)

    im2_size.close()
    im1.close()
    im2.close()


    img = PilImage.open("hoto.jpg")
    font = ImageFont.truetype("arial.ttf", 16)
    idraw = ImageDraw.Draw(img)
    idraw.text((15, 450), a, fill="black", font=font)
    img.save("result.jpg")
    img.show()


root = Tk()

root['bg'] = 'white'
root.title("-Времени")
root.wm_attributes("-topmost", 0.7)
root.geometry('500x500')

root.resizable(False, False)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

frame = Frame(root, bg="red")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="Верните мое время", bg='gray', font=40)
title.pack()

btn = Button(frame, text="Ok", bg='yellow', command=add_foto)
btn.pack()

text_add = Entry(frame, bg='white', width=50)
text_add.pack()


root.mainloop()