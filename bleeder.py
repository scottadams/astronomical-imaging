#This script contains key functions for masking data points (foreground and borders)
#Hopefully its commented well enough to be followed.
from __future__ import division
import mask as ms
import math
import merge
import numpy as np
import numpy.ma as ma
import bleeder as bld
import printer as p

def mask_foreground(image, borderdepth):
    
    imgheight = image.shape[0]-1                            #defining image size
    imgwidth = image.shape[1]-1                             #for use in function

    master = ms.perim(image, borderdepth)                   #create initial border mask

    #The following mask are created by defining a rectangular area within which bleeding of the main
    #star occurs. Every array element above the background value, defined in 'bleedmask', will be masked.
    #The masks are then merged into the master mask.
    mask1 = ms.bleedmask(image, 1425, 1445, 0, imgheight) 
    master = merge.merge(master, mask1)

    mask1 = ms.bleedmask(image, 1390, 1485, 0, 500)
    master = merge.merge(master, mask1)

    mask1 = ms.bleedmask(image, 1100, 1660, 400, 460)
    master = merge.merge(master, mask1)
    
    mask1 = ms.bleedmask(image, 1000, 1690, 298, 343)
    master = merge.merge(master, mask1)

    mask1 = ms.bleedmask(image, 1278, 1533, 105, 150)
    master = merge.merge(master, mask1)

    mask1 = ms.bleedmask(image, 1417, 1437, 3000, 3500)
    master = merge.merge(master, mask1)

    mask1 = ms.bleedmask(image, 1423, 1450, 2800, 3000)
    master = merge.merge(master, mask1) 

    mask1 = ms.circle(image, [3215,1436], 100)
    master = merge.merge(master, mask1)

    #The following masks are constructed using the same principle as above but mask the
    #remaining principal foreground objects.

    mask1 = ms.ovalmask(image, [2286, 905], 20, 80)
    master = merge.merge(master, mask1)

    mask1 = ms.ovalmask(image, [3320,775], 25, 130)
    master = merge.merge(master, mask1)

    mask1 = ms.ovalmask(image, [2773, 973], 25, 85)
    master = merge.merge(master, mask1)

    mask1 = ms.ovalmask(image, [3757,2133], 20, 65)
    master = merge.merge(master, mask1)

    mask1 = ms.ovalmask(image, [2310,2131], 20, 35)
    master = merge.merge(master, mask1)

    mask1 = ms.ovalmask(image, [1425,2088], 20, 35)
    master = merge.merge(master, mask1)

    return master

def mask_bright_objs(image, master, lower_limit, bg): #This routine generates masks for n number of objects

    #for y in range (0,n_obj):                   #Dictates how many loops of the cycle are done
    while image.max()>lower_limit:

        max = image.max()                       #finds the max value in the image
        list = image.flatten()                  #flattens the image into a 1D list
        location = np.where(list == max)[0]     #finds the position of all the maxima

        length = location.size                  #calculates how many maxima are present

        for z in range (0, length):             #Loop which repeats as many times as there are maxima

            ycoord = int(location[z]/2570)      #calculates the x and y co-ordinates
            xcoord = location[z]-(2570*ycoord)  #using the fact we know the shape of the original image

            pos = [ycoord, xcoord]              #stores the xy co-ordinates in pos
            #print pos                           #print position so we know which pixel is the problem if program fails
            new_mask = bld.obj_mask(image, pos, bg) #creates a circular mask over the image

            master = merge.merge(master, new_mask)  #merges the most recent mask to the master

            image.mask = master                 #applies the mask to the image so that we don't count the same objects when we repeat the loop

    return master                               #returns the master to mosaic


def obj_mask(image, pos, bg):                   #function to determine whether to create circle mask using x radius or y radius

    rad_x = bld.obj_mask_y(image, pos, bg)      #calculate max extent in x direction
    rad_y = bld.obj_mask_x(image, pos, bg)      #calculate max extent in y direction

    #mask = ms.bleedmask(image, pos[1]-rad_x, pos[1]+rad_x, pos[0]-rad_y, pos[0]+rad_y)
    mask = ms.ovalmask(image, pos, rad_x, rad_y)

    return mask


#The following two function do the same thing but for y and x axes respectively
def obj_mask_y(image, pos, bg):

    imgheight = image.shape[0]-1    #load image dimensions for use later

    for y in range (1,imgheight-pos[0]): #create loop from initial position to maximum border
        a = [image[pos[0]+y-2,pos[1]], image[pos[0]+y-1,pos[1]], image[pos[0]+y,pos[1]]] #create an array with the values of 3 successive pixels in the y direction
        b = np.array(a)                  #turn this into a numpy array so we can use numpy operations on it
        m = np.median(b)                #find the median of the array
        if y >= imgheight - pos[0] - 100:   #if y has reached the boundary mask this is max y value
            return y
        if m<bg:                            #if the median is less than back ground, this is max y value.
            return y


def obj_mask_x(image, pos, bg):

    imgheight = image.shape[0]-1
    imgwidth = image.shape[1]-1

    for x in range (1,imgwidth-pos[1]):
        a = [image[pos[0],pos[1]+x-2], image[pos[0],pos[1]+x-1], image[pos[0],pos[1]+x]]
        b = np.array(a)
        m = np.median(b)
        if x >= imgwidth - pos[1] - 100:
            return x
        if m<bg:
            return x



def catalogue(image, master, bg):

    f = open('data.csv', 'w')
    galaxy_count = 0

    f.write('Galaxy Number,X coord,Y coord,X radius,Y radius,Pixel Count \n')

    while image.max()>4000:                   #Dictates how many loops of the cycle are done

        max = image.max()                       #finds the max value in the image
        list = image.flatten()                  #flattens the image into a 1D list
        location = np.where(list == max)[0]     #finds the position of all the maxima

        length = location.size                  #calculates how many maxima are present

        for z in range (0, length):             #Loop which repeats as many times as there are maxima

            ycoord = int(location[z]/2570)      #calculates the x and y co-ordinates
            xcoord = location[z]-(2570*ycoord)  #using the fact we know the shape of the original image

            pos = [ycoord, xcoord]              #stores the xy co-ordinates in pos
            rad_x = bld.obj_mask_x(image, pos, bg)
            rad_y = bld.obj_mask_y(image, pos, bg)

            pixel_count = bld.ovalphotometry(image, pos, rad_x, rad_y)
            #mag = 25.3 - 2.5*math.log(pixel_count,10)
            galaxy_count += 1
            
            f.write('{number},{posx},{posy},{rad_x},{rad_y},{photo} \n'.format(number = galaxy_count, posx = pos[1], posy = pos[0], photo = pixel_count, rad_x = rad_x, rad_y = rad_y))

            new_mask = bld.obj_mask(image, pos, bg) #creates a circular mask over the image

            master = merge.merge(master, new_mask)  #merges the most recent mask to the master

            image.mask = master                     #applies the mask to the image so that we don't count the same objects when we repeat the loop
            print galaxy_count

    return master

def photometry(image, pos, rad):
    sum = 0
    pixel_count = 0
    mask = ma.getmaskarray(image)

    for x in range (pos[1]-1.1*rad, pos[1]+1.1*rad):
        for y in range (pos[0]-1.1*rad, pos[0]+1.1*rad):
            if mask[y,x] == False:
                sum += image[y, x]
                pixel_count += 1

    bg = local_background(image, pos, rad, rad)

    sum = sum - bg*pixel_count

    return sum

def ovalphotometry(image, pos, radx, rady):
    sum = 0
    pixel_count = 0
    mask = ma.getmaskarray(image)


    for x in range (pos[1]-radx, pos[1]+radx):
        for y in range(pos[0]-rady, pos[0]+rady):
            a = (x-pos[1])/radx
            b = (y-pos[0])/rady
            minor = pow(a, 2.0)
            major = pow(b, 2.0)
            oval = minor + major
            if oval <= 1 and mask[y,x] == False:
                sum += image[y,x]
                pixel_count += 1

    bg = local_background(image, pos, radx, rady)

    sum = sum - bg*pixel_count

    return sum


def local_background(image, pos, radx, rady):

    sum = 0
    pixel_count = 0
    mask = ma.getmaskarray(image)

    for x in range (pos[1]-200,pos[1]+200):
        for y in range(pos[0]-200, pos[0]+200):
            a = (x-pos[1])/radx
            b = (y-pos[0])/rady
            minor = pow(a, 2.0)
            major = pow(b, 2.0)
            oval = minor + major
            if oval >= 1 and oval <=4 and mask[y,x] == False:
                sum += image[y,x]
                pixel_count += 1

    bg = int(sum/pixel_count)

    return bg








