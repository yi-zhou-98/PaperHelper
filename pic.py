from PIL import Image

img = Image.open('1.png')
box = img.getbbox();
img = img.crop(list(box))
size = img.size

# img.thumbnail((500, 200) )
# img
proportion = size[0] / size[1] #长宽比例
width = 400
height = int(400 / proportion)
img.thumbnail((width, 100)) #等比将长度设置为400px 稍后设置宽度
size = img.size

#补白
padding = Image.new('RGB', (400, 100), 'white')

#补白
left = int((400 - size[0]) / 2)
padding.paste(img,(left, 0))
img = padding

table = []
threshold = 80
for i in range(0, 256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
        
img = img.convert('L').point(table, '1')
img = img.convert('RGB')
img.save('trans.png')