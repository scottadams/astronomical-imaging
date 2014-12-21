import numpy as np

def smooth(image):
	#Function to replace all rogue zeros with the median value of sky
	m = np.median(image[5000>image])
	image[image == 0] = m

	return image
	
