import cv2
import matplotlib.pyplot as plt

# Load color image
image = cv2.imread('photo.jpg')

# Convert color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Save converted images
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)

# Display converted images
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot histogram of grayscale
plt.hist(gray.ravel(), 256, [0,256])
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('grayscale_histogram.png')
plt.show()
