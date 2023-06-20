import cv2

def resize_image(input_image_path, output_image_path, new_width, new_height):

    image = cv2.imread(input_image_path)


    resized_image = cv2.resize(image, (new_width, new_height))


    cv2.imwrite(output_image_path, resized_image)


input_path = "back.png"
output_path = "back.png"


resize_image(input_path, output_path, 780, 440)

