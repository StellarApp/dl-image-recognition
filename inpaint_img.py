import cv2
from keras.models import model_from_json
import tensorflow as tf
import keras
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from pathlib import Path
# from pconv_layer import PConv2D

fileName = "starbucks_01.jpg"
filePath = f"{fileName}"
maskPath = f"mask_{fileName}"

# Reading an image in default mode
img = cv2.imread(filePath)
mask = cv2.imread(maskPath)

# Load the json file that contains the model's structure
f = Path("model.json")
model_structure = f.read_text()

model = model_from_json(model_structure)

# model = load_model('/data/Auditory_Emotion_Recognition/model_attention/fianl_emotion_model.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})
model = load_model(model)
model.load_weights("model_weights.h5")

image_to_test = image.image_to_array(img)

inputs = [img.reshape((1,)+img.shape), mask.reshape((1,)+mask.shape)]
model.prdict(inputs)