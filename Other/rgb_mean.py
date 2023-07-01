import cv2


image = cv2.imread("rgb_m.jpg")

# Define the region of interest (x, y, width, height)
roi = (100, 100, 200, 200)


x, y, w, h = roi
roi_image = image[y:y+h, x:x+w]


mean_color = cv2.mean(roi_image)


rgb_mean_color = (mean_color[2], mean_color[1], mean_color[0])

print("Mean Color (RGB):", rgb_mean_color)
