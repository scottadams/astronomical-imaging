import numpy as np
import numpy.ma as ma

#FUNCTION TO MERGE TWO MASKS TOGETHER
#Common issue can come from merging two masks with differnt dtypes. Don't know why this happens because all
#masks we have are boolean, but the error arises anyway. To be investigated once we've got the rest of
#the program running since with care this error can be avoided or circumnavigated.

def merge(mask1, mask2):
    combi = np.ma.mask_or(mask1, mask2)
    return combi