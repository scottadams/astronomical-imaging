#This currently does not work, need to work on the logic. Been testing on test object @[3822,2330]
#Perhap would be better to build test array

import numpy as np

def locate(image, pos):
    maxval = image[pos[0], pos[1]]      #initiate values with
    maxpos = [pos[0], pos[1]]           #intial pixel values

    for y in range(pos[0],pos[0]+100):           #set up for loop in y direction from current pixel to max.
        if image[y, pos[1]]>=maxval:    #check if next pixel is greater than current.
            maxval = image[y, pos[1]]   #if yes then update max
            maxpos = [y, pos[1]]        #pixel values
        else:
            ymid = y                    #if not then fix ymid position

    yrange = 2*(ymid-pos[0])            #calculate 2*distance from inital pixel to final pixel
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

    center = [y,x]                      #define co-ordinates to return

    return center



    """for x in range(pos[1],pos[1]+yrange):   #set up for loop in x direction from current pixel to max.
        if image[ymid, x]>=maxval:          #check if next pixel is greater than current.
            maxval = image[ymid, x]         #if yes then update max
            maxpos = [ymid, x]              #pixel values
            
    for x in range(-pos[1], yrange-pos[1]):
        if image[ymid, -x]>=maxval:
            maxval = image[ymid, -x]
            maxpos = [ymid, -x]"""


