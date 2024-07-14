from requests import *
import os

try:
	wa = "https://zenquotes.io/api/image"
	res = get(wa)
	print(res)

	filename = input("enter filename")
	if not os.path.exists(filename):
		f = open(filename, "wb")
		f.write(res.content)
		f.close()
	
	else:
		print("file already exists")

except Excepiton as e:
	print("issues ", e)