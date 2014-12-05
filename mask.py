import numpy as np


def perim(borderdepth,image):
	imgheight = image.shape[0]-1
	imgwidth = image.shape[1]-1
	perimask = np.ma.make_mask(image, copy=True, shrink=True,dtype=np.bool)

	perimask[:,:] = False

	for y in range(0,borderdepth):						
		perimask[y,:]=True
		perimask[imgheight-y,:]=True
	
	for x in range(0,borderdepth):
		perimask[:,x]=True
		perimask[:,imgwidth-x]=True

	return perimask


def sector(shape,centre,radius,angle_range):
    """
    Return a boolean mask for a circular sector. The start/stop angles in  
    `angle_range` should be given in clockwise order.
    """

    x,y = np.ogrid[:shape[0],:shape[1]]
    cx,cy = centre
    tmin,tmax = np.deg2rad(angle_range)

    # ensure stop angle > start angle
    if tmax < tmin:
            tmax += 2*np.pi

    # convert cartesian --> polar coordinates
    r2 = (x-cx)*(x-cx) + (y-cy)*(y-cy)
    theta = np.arctan2(x-cx,y-cy) - tmin

    # wrap angles between 0 and 2*pi
    theta %= (2*np.pi)

    # circular mask
    circmask = r2 <= radius*radius

    # angular mask
    anglemask = theta <= (tmax-tmin)

    return circmask*anglemask