from PIL import Image

image = Image.open("ALLES.enc.png").convert("F")

for i in range(500):
    for j in range(500):
        pixel = image.getpixel((i, j))
        print(pixel)


# image.show()


