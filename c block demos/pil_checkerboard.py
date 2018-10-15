import random
from PIL import Image

def checkerboard():
	r = 255;
	for i in range(500):
		if i%50 == 0:
			if r == 255:
				r = 0
			else:
				r = 255
		for j in range(500):
			if j%50 == 0:
				if r == 255:
					r = 0
				else:
					r = 255
			image.putpixel((i,j),(r,0,0))

			
		

imgx = 500
imgy = 500

image = Image.new("RGB",(imgx, imgy))

checkerboard()

image.save("snakes_image.png", "PNG")