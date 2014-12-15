import mask as ms
import merge
import numpy as np
import numpy.ma as ma
import bleeder as bld

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

def obj_rad(image, bg, n_obj):

    master = ms.perim(image, 0)

    for y in range (0,n_obj):
        
        max = image.max()
        list = image.flatten()
        location = np.where(list == max)[0]

        length = location.size

        for z in range (0, length-1):

            ycoord = int(location[z]/2570)
            xcoord = location[z]-(2570*ycoord)

            pos = [ycoord, xcoord]
            print pos
            mask = bld.obj_mask(image, pos, bg)

            master = merge.merge(master, mask)

    return master

def obj_mask(image, pos, bg):

    imgheight = image.shape[0]-1
    imgwidth = image.shape[1]-1

    for x in range (1,imgwidth-pos[1]):
        a = [image[pos[0],pos[1]+x-2], image[pos[0],pos[1]+x-1], image[pos[0],pos[1]+x]]
        b = np.array(a)
        m = np.median(b)
        if m<bg:
            mask = ms.circle(image, pos, x)
            return mask                    










