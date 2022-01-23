# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 21:28:23 2021

@author: E
"""

import matplotlib.pyplot as plt
img = plt.imread('images-black/img001.jpeg')
print( img.shape )

img = plt.imread('images-black/img001.jpeg')[:, :, 0]

plt.imshow(img) 
plt.colorbar()

plt.set_cmap('gray')
plt.imshow(img)
plt.colorbar()

plt.imread('images-black/img001.jpeg')[:, :, 0].astype(float)

diff = np.abs(img - bg)
diff2 = np.abs(img - bg)
threshold = 40.
diff2[diff>threshold] = 1.
diff2[diff<=threshold] = 0.



