import random
from PIL import Image

def checkerboard():
	total = 255
	r = 0
	for i in range(imgy):
		if i%check_size == 0:
			r = total-r
		for j in range(imgx):
			if j%check_size == 0:
				r = total-r
			image.putpixel((i,j),(r,0,0))

# could this helper function help you?
# I didn't use it, but maybe you could.
def rect(x, y, w, h, c):
	for i in range(x, x+w):
		for j in range(y, y+h):
			image.putpixel((i,j),(c,0,0))

num_checks = 8
check_size = 50
imgx = num_checks*check_size
imgy = imgx

image = Image.new("RGB",(imgx, imgy))

checkerboard()

image.save("checkerboard.png", "PNG")