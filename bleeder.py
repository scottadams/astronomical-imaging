import mask as ms
import merge

def bleed(image, borderdepth):
    
    imgheight = image.shape[0]-1
    imgwidth = image.shape[1]-1

    master = ms.perim(image, borderdepth)

    mask1 = ms.rectangle(image, 1430, 1445, 0, imgheight)

    master = merge.merge(master, mask1)

    mask1 = ms.rectangle(image, 1400, 1475, 0, 500)

    master = merge.merge(master, mask1)

    mask1 = ms.rectangle(image, 1160, 1650, 420, 450)

    master = merge.merge(master, mask1)
    
    mask1 = ms.rectangle(image, 1010, 1700, 308, 333)

    master = merge.merge(master, mask1)

    mask1 = ms.rectangle(image, 1288, 1523, 115, 140)

    master = merge.merge(master, mask1)

    mask1 = ms.rectangle(image, 1417, 1457, 3000, 3500)

    master = merge.merge(master, mask1)

    mask1 = ms.rectangle(image, 1423, 1450, 2800, 3000)

    master = merge.merge(master, mask1) 

    mask1 = ms.circle(image, [3215,1436], 62)

    master = merge.merge(master, mask1) 

    return master