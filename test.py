from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import textwrap
#pip install pillow

foto = filedialog.askopenfilename(title="Выберите файл", filetypes=[("All Files", "*.*")])
im1 = Image.new('RGB', (500, 600), (255, 255, 255))
im2 = Image.open(foto)


text = input("Напишите текст: ")
a = ('\n'.join(textwrap.wrap(text)))
im2_size = im2.resize((425, 425))
im1.paste(im2_size, (35, 10))
im1.save("hoto.jpg", quality=90)

im2_size.close()
im1.close()
im2.close()


img = Image.open("hoto.jpg")
font = ImageFont.truetype("arial.ttf", 16)
idraw = ImageDraw.Draw(img)
idraw.text((15, 450), a, fill="black", font=font)
img.save("result.jpg")
img = Image.open("result.jpg")
img.show()

