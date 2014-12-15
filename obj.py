#This currently does not work, need to work on the logic. Been testing on test object @[3722,2330]
#Perhap would be better to build test array

import numpy as np

def locate(image, pos):
    maxval = image[pos[0], pos[1]]      #initiate values with
    maxpos = [pos[0], pos[1]]           #intial pixel values

    for y in range(pos[0],pos[0]+50):   #set up for loop in y direction from current pixel to max.
        if image[y, pos[1]]>=maxval:    #check if next pixel is greater than current.
            maxval = image[y, pos[1]]   #if yes then update max
            maxpos = [y, pos[1]]        #pixel values

    ymid = maxpos[0]

    """yrange = (ymid-pos[0])            #calculate 2*distance from inital pixel to final pixel
    xmin = pos[1]-yrange                #set-up minimum x value
    xmax = pos[1]+yrange                #set up maximum x value

    maxval = image[ymid, xmin]          #restablish max values and positions
    maxpos = [ymid, xmin]               #knowing that we now have y (approximately) correct

    for x in range(xmin, xmax):         #set up for loop in x direction.
        if image[ymid, x]>=maxval:      #check if next pixel is greater than current.
            maxval = image[ymid, x]     #if yes then update max
            maxpos = [y, x]             #pixel values
        else:
            xmid = x                    #if not then fix xmid position

    center = [y,x]                      #define co-ordinates to return"""

    return ymid



