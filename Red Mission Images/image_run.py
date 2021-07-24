from PIL import Image
from pytesseract import pytesseract

TESSERACT = r"PATH TO EXE IN YOUR MACHINE"

decoder_image = Image.open("cover_image.PNG")
image_link = Image.open("image_link.PNG")
decoder_image.putalpha(200)
decoder_image = decoder_image.resize(image_link.size)
image_link.paste(decoder_image, (0, 0), decoder_image)
image_link.show()

pytesseract.tesseract_cmd = TESSERACT
text = pytesseract.image_to_string(image_link)
print(text[:-1])
