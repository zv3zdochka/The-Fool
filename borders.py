import cv2
import numpy as np
import time

#t = time.time()
target_resolution = (1920, 1080)

# Load the image
image = cv2.imread("im4.png")

# Resize to target_resolution

# Define the regions of interest (x, y, width, height)
regions_of_interest = [
    (20, 250, 180, 550),
    (200, 270, 1780, 560),
    (30, 555, 1850, 900),
]

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a color filter to detect white color
lower_white = np.array([220, 220, 220])
upper_white = np.array([255, 255, 255])
mask = cv2.inRange(image, lower_white, upper_white)

# Apply morphological operations to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=0)

# Find contours on the processed image
contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Minimum and maximum allowed dimensions for rectangles
min_rectangle_size = 80  # Minimum width or height
max_rectangle_size = 400  # Maximum width or height

# Iterate over the contours and draw rectangles only within the specified regions of interest
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if min_rectangle_size <= w <= max_rectangle_size and min_rectangle_size <= h <= max_rectangle_size:
        for roi in regions_of_interest:
            roi_x, roi_y, roi_w, roi_h = roi
            if roi_x <= x <= roi_x + roi_w and roi_y <= y <= roi_y + roi_h:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Display the selected region in a separate window
                #selected_image = image[y:y+h, x:x+w]
                #cv2.imshow("Selected Image", selected_image)
                #cv2.waitKey(0)
                break

# Display the result
#print(time.time() - t)
image = cv2.resize(image, (1280, 720))
cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()