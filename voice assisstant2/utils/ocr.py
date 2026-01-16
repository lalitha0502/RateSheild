import pytesseract
from PIL import Image
import pyautogui


def read_screen():
    img = pyautogui.screenshot()
    text = pytesseract.image_to_string(img)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR"
    return text
