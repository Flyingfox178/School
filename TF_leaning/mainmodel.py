import tensorflow as tf
import numpy
from PIL import Image

model = tf.keras.models.load_model("my_model.keras")

img0 = Image.open("example9.png").convert('L')
imgarr = numpy.asarray(img0)
imgarr = imgarr/255
print(imgarr)
imgarr = imgarr[numpy.newaxis,:,:]

prediction = model.predict(imgarr)
print(prediction)
print(numpy.argmax(prediction))
