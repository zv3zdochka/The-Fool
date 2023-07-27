import numpy as np
from keras.models import load_model
from PIL import Image

model = load_model("Rank_recog_model")

new_image_path = "path/to/your/new/image.jpg"


def preprocess_image(image_path):
    img = Image.open(image_path)
    img_gray = img.convert("L")
    img_resized = img_gray.resize((40, 80))
    img_array = np.array(img_resized)
    img_array = img_array.reshape(1, 80, 40, 1)
    img_array = img_array.astype('float32') / 255
    return img_array


new_image_array = preprocess_image(new_image_path)

predictions = model.predict(new_image_array)
predicted_label = np.argmax(predictions) + 2
print("Rank:", predicted_label)
