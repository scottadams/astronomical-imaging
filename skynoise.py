import numpy as np

#THIS FUNCTION IS NO LONGER USED. THIS FUNCTION IS KEPT JUST IN CASE ITS NEEDED LATER
def sky_noise(array, x1, x2, y1, y2):   #define function
#Function to get the average value of pixels across a patch of sky
    num_pixels = (x2-x1)*(y2-y1)        #calculate number of pixels in grid
    total = 0                           #initiate sum of pixels
    for y in range (y1, y2):            #initiate first loop
        for x in range (x1, x2):        #initiate second loop
            total += array[y][x]        #add pixel value to total

    average = total/num_pixels          #calculate average of pixels
    return average                      #return average