# Sept. 5 2020 shi3z 
# MIT Licence

import os
import random
from PIL import Image
from imageio import imwrite
import numpy as np

clusters = np.load("download/kmeans_centers.npy")


# Load Image 
im = Image.open('shi3z.png')
im = im.resize((32,32))

imr = np.array(im)

def dist(x,y):   # Get Euclidean distance
    return np.sqrt(np.sum((x-y)**2))

def find_index(a): # Find the closest color from the lookup table.
	# Oh, you know how to write more complete code. But I wanted to save time investigating.
	mind = 10000  # mind:minium distance
	minidx = -1   # minidx: index of minimum distance color of CLUT.
	for i in range(len(clusters)): 
		d = dist(a/127.5-1.0,clusters[i])
		if mind > d:
			mind = d
			minidx = i
	return minidx # Return minimum index


# RGB Image to palettized Image
result = []
for y in range(32):
	for x in range(32):
		result.append(find_index(imr[y,x]))

samples = np.array(result)
np.save("shi3z.npy",samples) #save numpy data

# Confirm generated image
samples = np.reshape(np.rint(127.5 * (clusters[samples] + 1.0)), [32, 32, 3]).astype(np.uint8)
imwrite("res.png", samples)
