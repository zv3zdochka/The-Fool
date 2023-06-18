# The-Fool-Game


This project aims to develop a computer vision system that can recognize and identify playing cards placed on a table. The system utilizes Python and the OpenCV library to process and analyze images from a screen. After card recognition, I want to add the ability to play cards with a person using a machine learning-based algorithm. The project will be divided into two stages:

1. Card and Event Recognition
2. Full-fledged Human-Player Game


## Using Libraries

1. OpenCV
2. Numpy

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository

## Card and Event Recognition

We started with card recognition, for this we first convert the image into an image of a certain resolution
```python
# Screen
sizes screen_width = 1920
screen_height = 1080

# Resolution of the target image
target_resolution = (screen_width, screen_height)

image = cv2.resize(image, (screen_width, screen_height))
```

we translate it into an image with shades of gray
```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

then we apply a filter to highlight white cards from a blue-blue background 

```python
lower_white = np.array([220, 220, 220])
upper_white = np.array([255, 255, 255])
mask = cv2.inRange(image, lower_white, upper_white)
```

and with the help of morphological operations, we reduce noise 
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=3)
```

now we contour our image in certain areas and check the quadrilaterals for size compliance 

``python
contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
``
that's all we get our processed image 

//image


