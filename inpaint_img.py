
from keras.models import load_model
from pconv_layer import PConv2Ding

fileName = "Starbucks_01.jpg"
filePath = f"{fileName}"
maskPath = f"Mask_{fileName}"

# Reading an image in default mode
# img = cv2.imread(filePath)
# mask = cv2.imread(maskPath)

img = image.load_img(filePath, target_size=(32, 32, 3))
mask = image.load_img(maskPath, target_size=(32, 32, 3))

# data = [[],[]]
#
# data[0].append(asarray(img))
# data[1].append(asarray(mask))
#
# print(len(data))
# print(len(data[0][0]))
# print(len(data[1][0]))
#
# np.save('data', np.array(data))

# f = open("data.txt", "a")
# f.write(data.__str__())
# f.close()

# f = open("data.txt", "r")
# data = f.read()
# print(len(data[0][0]))


# # Load the json file that contains the model's structure
# f = Path("model.json")
# model_structure = f.read_text()
#
# model = model_from_json(model_structure)
#
model = load_model('model/model_ipc', custom_objects={'PConv2D': PConv2D})
# model = load_model(model)
# model.load_weights("model_weights.h5")

print("test1")
print(model.get_config())
print("test2")
# image_to_test = image.image_to_array(img)
#
# inputs = [img.reshape((1,)+img.shape), mask.reshape((1,)+mask.shape)]
# model.prdict(inputs)