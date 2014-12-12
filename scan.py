def scan(image):
    shape = image.shape
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if image[x, y] >= 40000:
                return[x, y]