import math							#import math
from astropy.io import fits			#import fits
import numpy as np					#import numpy
import matplotlib.pyplot as plt		#import matplotlib


mosaic = fits.open('mosaic.fits')	#loads fit file into mosaic
hdr = mosaic[0].header				#loads hdr with header data
image = mosaic[0].data				#loads image with image data

image[30:40, 10:20] = 500			#set pixels y=31 to 40 and x=11 to 20 to 500
mosaic.writeto('newimage.fits', clobber=True)	#writes modified image to new fits file

plt.imshow(image)					#renders image for matplotlib
plt.show()