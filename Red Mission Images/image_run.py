from PIL import Image
from pytesseract import pytesseract

TESSERACT = r"PATH TO EXE IN YOUR MACHINE"

decoder_image = Image.open("cover_image.PNG")
image_link = Image.open("image_link.PNG")
# decoder_image.show()
# image_link.show()
