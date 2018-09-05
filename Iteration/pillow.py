from PIL import Image
size = width, height = 320, 240
image = Image.new("RGB", size, "white")
image.show()
del image
