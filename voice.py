from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 


from pdfminer.high_level import extract_text
 
text = extract_text("file.pdf", page_numbers = range(1))
 
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=text, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("audio.mp3") 
  
# Playing the converted file 
os.system("mpg321 audio.mp3")