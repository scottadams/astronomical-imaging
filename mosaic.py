import math							#import math
from astropy.io import fits			#import fits
import numpy as np					#import numpy
import numpy.ma as ma 				#import masked arrays
import matplotlib.pyplot as plt		#import matplotlib
import mask as ms 					#import mask
import printer as p 				#import printer
import merge                        #import merge
import scan


mosaic = fits.open('mosaic.fits')	#loads fit file into mosaic
hdr = mosaic[0].header				#loads hdr with header data
image = ma.array(mosaic[0].data)				#loads image with image data

master = ms.perim(image, 50)
image.mask = master

pos = scan.scan(image)
print pos

p.plot(image)

############ MIGHT BE USEFUL LATER ##############
#image[30:40, 10:20] = 500						#set pixels y=31 to 40 and x=11 to 20 to 500
#mosaic.writeto('newimage.fits', clobber=True)	#writes modified image to new fits file

#mag = hdr['MAGZPT']-2.5*np.log10(image)        #convert pixel count to magnitude
