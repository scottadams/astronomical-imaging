import math							#import math
from astropy.io import fits			#import fits

mosaic = fits.open('mosaic.fits')	#loads fit file into mosaic
hdr = mosaic[0].header				#loads hdr with header data
image = mosaic[0].data				#loads image with image data
m = hdr['MAGZPT']-2.5*log10(image)	#attempt at doing math on image values
