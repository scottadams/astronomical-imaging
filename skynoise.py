import numpy as np

def sky_noise(array, x1, x2, y1, y2):   #define function
    num_pixels = (x2-x1)*(y2-y1)        #calculate number of pixels in grid
    total = 0                           #initiate sum of pixels
    for y in range (y1, y2):            #initiate first loop
        for x in range (x1, x2):        #initiate second loop
            total += array[y][x]        #add pixel value to total

    average = total/num_pixels          #calculate average of pixels
    return average                      #return average