import numpy as np

def zeros(image):
    #Function to replace all rogue zeros with the median value of sky
    
    min = image.min()
    list = image.flatten()                  #flattens the image into a 1D list
    location = np.where(list == min)[0]     #finds the position of all the maxima
    length = location.size                  #calculates how many maxima are present

    for z in range (0, length):             #Loop which repeats as many times as there are maxima
        ycoord = int(location[z]/2570)      #calculates the x and y co-ordinates
        xcoord = location[z]-(2570*ycoord)  #using the fact we know the shape of the original image
        m = np.median(image[ycoord-2:ycoord+2, xcoord-2:xcoord+2])
        image[ycoord, xcoord] = m

    return image
    
def highlight_zeros(image):
    #Function to replace all rogue zeros with the median value of sky
    
    min = image.min()
    list = image.flatten()                  #flattens the image into a 1D list
    location = np.where(list == min)[0]     #finds the position of all the maxima
    length = location.size                  #calculates how many maxima are present
    zeros = np.zeros(image.shape)

    for z in range (0, length):             #Loop which repeats as many times as there are maxima
        ycoord = int(location[z]/2570)      #calculates the x and y co-ordinates
        xcoord = location[z]-(2570*ycoord)  #using the fact we know the shape of the original image
        zeros[xcoord-5:xcoord+5, ycoord-5:ycoord+5] = 40000

    return zeros