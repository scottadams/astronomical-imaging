import math							#import math
from astropy.io import fits			#import fits
import numpy as np					#import numpy
import numpy.ma as ma 				#import masked arrays
import matplotlib.pyplot as plt		#import matplotlib
import mask as ms 					#import mask
import printer as p 				#import printer
import merge                        #import merge
import scan							#import scan
import bleeder as bld 				#import bleeder+perim mask maker
import smooth


mosaic = fits.open('mosaic.fits')	#loads fit file into mosaic
hdr = mosaic[0].header				#loads hdr with header data
image = mosaic[0].data				#loads image with image data
image = smooth.zeros(image)			#remove zeros and replace with median

masked_img = ma.array(image)		#create mask copy of image to mask incase we need an unmasked image later

mag = hdr['MAGZPT']-2.5*np.log10(image)        #convert pixel count to magnitude

masked_mag = hdr['MAGZPT']-2.5*np.log10(masked_img)        #create mask copy of mag in case we need and umasked mag later

master = bld.mask_foreground(image, 100)		#create a mask which masks the main foreground objects and border

masked_img.mask = master						#apply the master mask

bright_obj = bld.mask_bright_objs(masked_img, master, 50000, 3500)	

master = merge.merge(master, bright_obj)

masked_img.mask = master

master = bld.catalogue(masked_img, master, 3500)

masked_mag.mask = master

p.plot(masked_img)

############ MIGHT BE USEFUL LATER ############
#image[30:40, 10:20] = 500						#set pixels y=31 to 40 and x=11 to 20 to 500
#mosaic.writeto('masked.fits', clobber=True)	#writes modified image to new fits file

