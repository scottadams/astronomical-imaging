<<<<<<< HEAD
from astropy.io import fits                 #import fits
=======
from astropy.io import fits #import fits
>>>>>>> fff8cd7cfb40e7866d56fa7946173ecb52be2465
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

def calc(image):
<<<<<<< HEAD
    shape = image.shape
    freqarray = []
    #frequencies = open('frequencies.txt','a')
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if image[x,y] > 1000 and image[x,y] < 5000:
                freqarray.append(image[x,y])
    return freqarray
                #frequencies.write(str(image[x,y]))
                #frequencies.write(", ")
    #frequencies.close

mosaic = fits.open('mosaic.fits')   #loads fit file into mosaic
hdr = mosaic[0].header              
image = mosaic[0].data              
=======
	shape = image.shape
	freqarray = []
	#frequencies = open('frequencies.txt','a')
	for x in range(0, shape[0]):
		for y in range(0, shape[1]):
			if image[x,y] > 1000 and image[x,y] < 5000:
				freqarray.append(image[x,y])
	return freqarray
#frequencies.write(str(image[x,y]))
#frequencies.write(", ")
#frequencies.close

mosaic = fits.open('mosaic.fits') #loads fit file into mosaic
hdr = mosaic[0].header
image = mosaic[0].data
>>>>>>> fff8cd7cfb40e7866d56fa7946173ecb52be2465

x = calc(image)

# the histogram of the data
<<<<<<< HEAD
n, bins, patches = plt.hist(x, 1500, normed=1, facecolor='green', alpha=0.75)
=======
n, bins, patches = plt.hist(x, 2000, normed=1, facecolor='green', alpha=0.75)
>>>>>>> fff8cd7cfb40e7866d56fa7946173ecb52be2465

# add a 'best fit' line
# y = mlab.normpdf( bins, mu, sigma)
# l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('frequency')
plt.ylabel('counts')
plt.title(r'histogram')
<<<<<<< HEAD
plt.axis([3300, 3600, 0, 0.06])
plt.grid(True)
plt.show()

=======
plt.axis([3300, 3600, 0, 0.1])
plt.grid(True)
plt.show()
>>>>>>> fff8cd7cfb40e7866d56fa7946173ecb52be2465
