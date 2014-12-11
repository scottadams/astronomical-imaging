import math							#import math
from astropy.io import fits			#import fits
import numpy as np					#import numpy
import numpy.ma as ma 				#import masked arrays
import matplotlib.pyplot as plt		#import matplotlib
import mask as ms 					#import mask


mosaic = fits.open('mosaic.fits')	#loads fit file into mosaic
hdr = mosaic[0].header				#loads hdr with header data
image = mosaic[0].data				#loads image with image data

mag = hdr['MAGZPT']-2.5*np.log10(image)			#convert pixel count to magnitude
mask = ms.perim(50, image)						#create mask

z = ma.array(image)								#create maskable array using image data
z.mask = mask 									#set mask as mask

shape = z.shape
result = np.zeros(shape)
for x in range(0, shape[0]):
    for y in range(0, shape[1]):
        if z[x, y] >= 60000:
            print[x, y]



plt.imshow(z)					#renders image for matplotlib
plt.colorbar()					#show colour scale
plt.show()						#draws image


############ MIGHT BE USEFUL LATER ##############
#image[30:40, 10:20] = 500						#set pixels y=31 to 40 and x=11 to 20 to 500
#mosaic.writeto('newimage.fits', clobber=True)	#writes modified image to new fits file
