import cv2
from keras.models import model_from_json
import tensorflow as tf
import keras
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from pathlib import Path
from pconv_layer import PConv2D

fileName = "starbucks_01.jpg"
filePath = f"{fileName}"
maskPath = f"mask_{fileName}"

# Reading an image in default mode
img = cv2.imread(filePath)
mask = cv2.imread(maskPath)

print(tf.__version__)
print(keras.__version__)


# Load the json file that contains the model's structure
# f = Path("model/model.json")
# model_structure = f.read_text()

# model = load_model("model/model_ia.h5")
# model.load_weights("model/model_weights_ia.h5")

# image_to_test = image.image_to_array(img)
#
# inputs = [img.reshape((1,)+img.shape), mask.reshape((1,)+mask.shape)]
# model.prdict(inputs)