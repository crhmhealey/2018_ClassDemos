from PIL import Image

xa, xb = -0.38338774873898274, -0.38338772978761426
ya, yb = 0.653138066992824, .95*0.6531380859441924

imgx, imgy = 512, 512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y * (yb-ya) / (imgy - 1) + ya
	for x in range(imgx):
		cx = x * (xb-xa) / (imgx - 1) + xa
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c

		r = i
		g = (i*50)%256
		b = 256-i

		image.putpixel((x, y),(r,g,b))

image.show()