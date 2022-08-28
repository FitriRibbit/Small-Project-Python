from unittest import result
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Administrator/Desktop/project python/file img/myqrcode.png')

result = decode(img)

print(result)