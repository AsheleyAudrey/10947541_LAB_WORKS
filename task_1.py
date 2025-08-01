 # Import the OpenCV library for image processing
 import cv2 
# Import matplotlib for image visualization
import matplotlib.pyplot as plt
# Load the image from file
image1 = cv2.imread('example.jpg')
# Convert the image to grayscale (single channel intensity image)
gray_image = cv2.cvtColor(the_image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Original Image', image)
plt.imshow(gray_image, cmap='gray') 
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Print out the dimensions of the original and grayscale images
print("Original Image Shape:", image1.shape)        # Format: (height, width, color channels)
print("Grayscale Image Shape:", gray_image.shape)      # Format: (height, width)

# Save grayscale image
cv2.imwrite('photo_gray.jpg', gray_image)

