import requests
import os
from PIL import Image

im = Image.open('D:\log.png')
print(im.format, im.size, im.mode)

url = 'http://www.runoob.com/design-pattern/factory-pattern.html'
