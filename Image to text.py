# OCR (Optical Character Recognition) is the process of electronical conversion of Digital images into 
# machine-encoded text.

# Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and 
# “read” the text embedded in images.

# Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation 
# script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, 
# including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print 
# the recognized text instead of writing it to a file.

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('qoute.tiff')
# print(type(image))

text = pytesseract.image_to_string(image)

print(text)