import numpy as np
import numpy.ma as ma


def perim(image,borderdepth):
# calculates and applies a boolean perimeter mask of given depth, returning the masked image

    imgheight = image.shape[0]-1
    imgwidth = image.shape[1]-1
    perimask = np.ma.make_mask(image, copy=True, shrink=True,dtype=np.bool)

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

    x,y = np.ogrid[:shape[0],:shape[1]]
    cx,cy = centre

    # convert cartesian --> polar coordinates
    r2 = (x-cx)*(x-cx) + (y-cy)*(y-cy)

    # generate circular mask
    circmask = r2 <= radius*radius

    #maskedimage = ma.array(image)                                #create maskable array using image data
    #maskedimage.mask = circmask                        #set mask as mask

    return circmask

def rectangle(image, x1, x2, y1, y2):
    rectmask = np.zeros(image.shape, dtype=bool)
    rectmask[y1:y2,x1:x2] = True

    return rectmask




