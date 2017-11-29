from PIL import Image

type = ["c", "d", "h", "s"] 
edit = []

for val in range(4):
	for count in range(1,14):
		if count < 10:
			num = "0" + str(count)
		else:
			num = str(count)
		
		edit.append(str(type[val]) + str(num) + ".png")

edit.append("z01.png")
edit.append("z02.png")
edit.append("x01.png")
edit.append("x02.png")

print "edit start"

for val in range(len(edit)):
	img = Image.open(edit[val], "r")
	img.thumbnail((img.size[0] / 2, img.size[1] / 2), Image.ANTIALIAS)
	img.save(edit[val], "PNG", quality = 100, optimize = True)

print "completed"

