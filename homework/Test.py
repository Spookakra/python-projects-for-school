from PIL import Image

#img  = Image.open(path)     
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
   
try: 
    img  = Image.open("homework\yeah.gif") 
except IOError:
    pass
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.