import numpy as np

def sky_noise(array, x1, x2, y1, y2):
    num_pixels = (x2-x1)*(y2-y1)
    total = 0
    for y in range (y1, y2):
        for x in range (x1, x2):
            total += array[y][x]

    average = total/((x2-x1)*(y2-y1))      
    return average