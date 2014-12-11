def initial():
	import math							#import math
	from astropy.io import fits			#import fits
	import numpy as np					#import numpy
	import numpy.ma as ma 				#import masked arrays
	import matplotlib.pyplot as plt		#import matplotlib
	import mask as ms 					#import mask


	mosaic = fits.open('mosaic.fits')	#loads fit file into mosaic
	hdr = mosaic[0].header				#loads hdr with header data
	image = mosaic[0].data				#loads image with image data