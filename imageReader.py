import PIL
from PIL import Image
from pytesseract import * 
import enum
from googletrans import Translator

def extractImage (image: str, lang: str) -> str:
    img = Image.open(image)
    extractText = pytesseract.image_to_string(img, lang=lang)
    resualt = trasnlator(extractText)
    print ("The Texts are: " + extractText)
    print ("The Trans are: " + resualt.text)
    return resualt.text

def trasnlator (extractText: str) -> str:
    translator = Translator()
    resault = translator.translate(extractText, src='auto', dest='fa')
    return resault

if __name__ ==  '__main__': 
    sampleImageReader = extractImage('./allImages.dir/rdr2.jpg', lang='eng')
    print (sampleImageReader)


#################################################################|
################ Image Text Reader ##############################|
#################################################################|
 

