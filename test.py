from tensorflow import keras
# from keras.models import load_model

from pconv_layer import PConv2D
# from tensorflow.keras.preprocessing import image

# fileName = "Starbucks_01.jpg"
# filePath = f"{fileName}"
# maskPath = f"Mask_{fileName}"


# img = image.load_img(filePath, target_size=(32, 32, 3))
# mask = image.load_img(maskPath, target_size=(32, 32, 3))
print("xy")


# model = load_model('model_ipc', custom_objects={'PConv2D': PConv2D})

model = keras.models.load_model('model_ipc', custom_objects={'PConv2D':PConv2D})
print(model.get_config())