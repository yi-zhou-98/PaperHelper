from PIL import Image
import numpy as np
import math
import cv2

img = Image.open("1.png")
Img = img.convert('L')

threshold = 130
 
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
 
photo = Img.point(table, '1')

w = photo.width
h = photo.height

inih = 0
endh = 0

ph = np.array(photo)
for x in range(h):
    if(ph[x][0] != False):
        inih = x
        break

for x in range(inih,h):
    if(ph[x][0] == False):
        endh = x-1
        break

new = Img.crop((0,inih,w,endh))


ratio = 400/(new.height) 
finw = math.floor(ratio*new.width) 

final = new.resize((1000,400))

table = []
threshold = 170
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
 
fin = final.point(table, '1')

fin = fin.convert('RGB')

fin.save("0.png")


