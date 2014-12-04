# Should take image as argument

import numpy as np


borderdepth = 100			# sets border depth to 100 pix






imgheight = image.shape[0]-1
imgwidth = image.shape[1]-1



mask = np.ma.make_mask(image, copy=True, shrink=True,dtype=np.bool) # Creates mask with same dimensions as image
mask[:,:] = False													# Sets all mask values to true


for y in range(0,borderdepth):						
	mask[y,:]=True
	mask[imgheight-y,:]=True

for x in range(0,borderdepth):
	mask[:,x]=True
	mask[:,imgwidth-x]=True

return mask