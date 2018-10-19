# class code
from PIL import Image

xmin, xmax = -0.38338774873898274, -0.38338772978761426
ymin, ymax = 0.653138066992824, 0.6531380859441924*1.25

imgx, imgy = 512, 512

maxIt = 256

image = Image.new("RGB",(imgx, imgy))

for y in range(imgy):
	cy = y * (ymax-ymin) / (imgy-1) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin) / (imgx-1) + xmin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		r = i
		g = (i*50)%256
		b = 255-i

		image.putpixel((x,y),(r,g,b))

image.show()













