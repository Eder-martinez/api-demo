from PIL import Image

im = Image.open("hollow.jpg")

print(im.format, im.size, im.mode)

box = (100, 100, 500, 500)
region = im.crop(box)
region.save("recorte.png")

r, g, b = region.split()
region = Image.merge("RGB", (b, g, r))
region.save("cambio.png")

out = region.rotate(45)
out.save("giro.png")
