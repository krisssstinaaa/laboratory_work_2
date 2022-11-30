from PIL import Image, ImageDraw
file = open('DS0.txt', 'r')

image = Image.new('RGB', (540, 960), (255, 255, 255))
img_draw = ImageDraw.Draw(image) 

for line in file.readlines():

    x, y = map(int, line.split(' '))
    img_draw.point((x, y), (0, 0, 0))

file.close()
image.save('result.png')