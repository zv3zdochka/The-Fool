import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split

images = np.load(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Datasets\images.npy")
labels = np.load(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Datasets\labels.npy")


images = images.astype('float32') / 255


num_classes = len(np.unique(labels))
labels = keras.utils.to_categorical(labels, num_classes)




X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(40, 80, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


batch_size = 32
epochs = 10
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_test, y_test))


score = model.evaluate(X_test, y_test, verbose=0)
print("Точность модели на тестовой выборке:", score[1])
model.save("Rank_recog_model")