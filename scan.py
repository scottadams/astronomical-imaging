#THIS FUNCTION IS NO LONGER USED BUT IS KEPT IN CASE ITS USEFUL LATER
def scan(image, limit):
    shape = image.shape
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if image[x, y] >= limit:
                return[x, y]