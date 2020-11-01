import sys, os
import matplotlib.pyplot as plt
from PIL import Image

IMAGE_DIR = sys.argv[1]

imageList = dict()
for (dirpath, dirnames, filenames) in os.walk(IMAGE_DIR):
  for filename in filenames:
    if 'final' in filename:
      imageList[filename] = Image.open(str(os.sep.join([dirpath, filename])))

r, c = 2, 5
f, axarr = plt.subplots(r, c)
sortedImages = sorted(imageList.keys())
imageNum = 0
for i in range(r):
  for j in range(c):
    axarr[i, j].axes.xaxis.set_visible(False)
    axarr[i, j].axes.yaxis.set_visible(False)
    axarr[i, j].imshow(imageList[sortedImages[imageNum]], cmap='gray', vmin=0, vmax=255)
    imageNum += 1


plt.savefig(IMAGE_DIR + '_outputs.png')
plt.show()
