from __future__ import division
import numpy as np
import numpy.ma as ma



def perim(image,borderdepth):
# calculates and applies a boolean perimeter mask of given depth, returning the masked image

    imgheight = image.shape[0]-1
    imgwidth = image.shape[1]-1
    #perimask = np.zeros(image.shape, dtype=bool)
    perimask = np.ma.make_mask(image, copy=True, shrink=True,dtype=bool)

    perimask[:,:] = False

    for y in range(0,borderdepth):
        perimask[y,:]=True
        perimask[imgheight-y,:]=True
    
    for x in range(0,borderdepth):
        perimask[:,x]=True
        perimask[:,imgwidth-x]=True

    #maskedimage = ma.array(image)                                #create maskable array using image data
    #maskedimage.mask = perimask                                  #set mask as mask

    return perimask


def circle(image,centre,radius):
# calculates and applies a circular mask of given position and radius, returning the masked image

    shape = image.shape

    circmask = np.zeros(image.shape, dtype=bool)

    x,y = np.ogrid[:shape[0],:shape[1]]
    cx,cy = centre

    # convert cartesian --> polar coordinates
    r2 = (x-cx)*(x-cx) + (y-cy)*(y-cy)

    # generate circular mask
    circle = r2 <= radius*radius

    circmask[circle] = True

    return circmask



def rectangle(image, x1, x2, y1, y2):
# calculates a rectangular mask according within the given values
    rectmask = np.zeros(image.shape, dtype=bool)
    rectmask[y1:y2,x1:x2] = True

    return rectmask



def bleedmask(image, x1, x2, y1, y2):
# create a mask by comapring values within an area to the background
    mask = np.zeros(image.shape, dtype=bool)    #create an array of zeros with the same dimensions

    for x in range (x1, x2):                    #examine all the pixels within
        for y in range(y1, y2):                 #the defined area
            if image[y,x]>3449:                 #if pixel value is larger than background
                mask[y,x] = True                #create mask at this point.

    return mask

def ovalmask(image, pos, radx, rady):
    mask = np.zeros(image.shape, dtype=bool)

    for x in range (pos[1]-radx, pos[1]+radx):
        for y in range(pos[0]-rady, pos[0]+rady):
            a = (x-pos[1])/radx
            b = (y-pos[0])/rady
            minor = pow(a, 2.0)
            major = pow(b, 2.0)
            oval = minor + major
            #print 'minor axis {val1}. major axis {val2}. Oval val {val3}.'.format(val1 = a, val2 = b, val3 = oval)
            if oval <= 1 and image[y,x]>3449:
                mask[y,x] = True

    return mask




