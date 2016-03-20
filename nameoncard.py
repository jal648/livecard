from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img = Image.open("osper-card-real.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font1 = ImageFont.truetype("kredit back.ttf", 43)
font2 = ImageFont.truetype("kredit front.ttf", 43)
font3 = ImageFont.truetype("kredit shine.ttf", 43)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((130, 473),"JOEL LESLIE",(200,200,200),font=font1)
draw.text((129, 475),"JOEL LESLIE",(100,100,100),font=font2)
draw.text((130, 473),"JOEL LESLIE",(230,230,230),font=font3)

img.save('sample-out.png')