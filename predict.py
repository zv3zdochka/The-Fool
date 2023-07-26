import numpy as np
from keras.models import load_model

model = load_model("Rank_recog_model")

img_array = np.random.rand(80, 40, 1)

img_array = img_array.reshape(1, 80, 40, 1)
predictions = model.predict(img_array)
predicted_label = np.argmax(predictions) + 2
print("Rank:", predicted_label)
