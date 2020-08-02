import pytesseract
from PIL import Image

resim = Image.open("test2.jpg")

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"

text = pytesseract.image_to_string(resim, lang="tur")

print(text)