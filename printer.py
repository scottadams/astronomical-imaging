import matplotlib.pyplot as plt		#import matplotlib

def plot(image):
	plt.imshow(image, origin='lower')
	plt.colorbar()
	plt.show()

	return 0