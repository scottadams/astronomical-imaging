import numpy as np
import numpy.ma as ma

def merge(mask1, mask2):
    combi = np.ma.mask_or(mask1, mask2)
    return combi