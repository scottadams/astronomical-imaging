import numpy as np

def smooth(image):
	m = np.median(image[5000<image])
	image[image == 0] = m

	return image
	
