import cv2
import numpy as np

# Load the image
image = cv2.imread('table_image.jpg')

# Define the regions of interest (x, y, width, height)
regions_of_interest = [
    (100, 100, 200, 200),
    (300, 200, 150, 250),
]

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a color filter to detect white color
lower_white = np.array([200, 200, 200])
upper_white = np.array([255, 255, 255])
mask = cv2.inRange(image, lower_white, upper_white)

# Apply morphological operations to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Find contours on the processed image
contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours and draw rectangles only within the specified regions of interest
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    for roi in regions_of_interest:
        roi_x, roi_y, roi_w, roi_h = roi
        if roi_x <= x <= roi_x + roi_w and roi_y <= y <= roi_y + roi_h:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break

# Display the result
cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
