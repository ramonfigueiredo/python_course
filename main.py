from scipy import ndimage
import imageio
import matplotlib.pyplot as plt

# Load an image
image = imageio.imread('images/RFP_YouTube_Profile_Picture.png')

# Gaussian blur
blurred_image = ndimage.gaussian_filter(image, sigma=3)

# Display images
plt.imshow(image, cmap=plt.cm.gray)
plt.imshow(blurred_image, cmap=plt.cm.gray)
plt.show()