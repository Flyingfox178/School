import tensorflow as tf
import numpy
from PIL import Image

img0 = Image.open("/workspaces/School/MNIST_dataset_example0.png").convert('L')
imgarr = numpy.asarray(img0)
imgarr = imgarr/255
print(imgarr)
#img0.reshape(28,28)
#img0 = img0[numpy.newaxis,:,:]

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10) #, activation='softmax')
])

predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

model.fit(x_train,y_train,epochs=2)
model.evaluate(x_test,y_test,verbose=2)

propability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
    ])

#propability_model(x_test[:5])


prediction = model.predict(imgarr)
print(prediction)
numpy.argmax(prediction)

#print(x_test[5])
#print(x_test[6])