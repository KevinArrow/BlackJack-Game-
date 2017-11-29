from PIL import Image

edit = ["start.png"]

print "edit start"

for val in range(len(edit)):
	img = Image.open(edit[val], "r")
	img.thumbnail((img.size[0] / 2, img.size[1] / 2), Image.ANTIALIAS)
	img.save(edit[val], "PNG", quality = 100, optimize = True)

print "completed"

