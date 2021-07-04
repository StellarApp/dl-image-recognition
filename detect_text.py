import cv2

testArray = [{'x': 39, 'y': 26}, {'x': 243, 'y': 26}, {'x': 243, 'y': 40}, {'x': 39, 'y': 40}]

def find_bouding_box(array):
    results = dict()
    start_x = array[0]['x']
    start_y = array[0]['y']
    end_x = array[0]['x']
    end_y = array[0]['y']

    for i in range(1, len(array)):
        x = array[i]['x']
        y = array[i]['y']

        start_x = x if (x < start_x) else start_x
        end_x = x if (x > end_x) else end_x
        start_y = y if (y < start_y) else start_y
        end_y = y if (y > end_y) else end_y
    
    results['startX'] = start_x
    results['endX'] = end_x
    results['startY'] = start_y
    results['endY'] = end_y

    # results = (start_x, start_y, end_x, end_y)
    return results


def create_mask(image, boundingBox):
    inp_mask = image.copy()

    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    (img_H, img_W) = image.shape[:2]

    # set the new width and height and then determine the ratio in change
    # for both the width and height: Should be multiple of 32
    (newW, newH) = (320, 320)

    rW = img_W / float(newW)
    rH = img_H / float(newH)

    # resize the image and grab the new image dimensions
    r_img = cv2.resize(image, (newW, newH))

    (H, W) = r_img.shape[:2]

    # change background color for mark image to black
    cv2.rectangle(inp_mask, (0, 0), (img_W, img_H), (255, 255, 255), -1)

    # loop over the bounding boxes
    # for (startX, startY, endX, endY) in boundingBox:
    # scale the bounding box coordinates based on the respective
    # ratios
    startX = boundingBox['startX']
    startY = boundingBox['startY']
    endX = boundingBox['endX']
    endY = boundingBox['endY']

    # draw the white bounding box on the mark image
    cv2.rectangle(inp_mask, (startX, startY), (endX, endY), (0, 0, 0), -1)

    # Converting image to 8-bit 1-channel image
    inp_mask = cv2.cvtColor(inp_mask, cv2.COLOR_BGR2GRAY)
    return inp_mask


fileName = "starbucks_01.jpg"
filePath = f"{fileName}"

# Reading an image in default mode
origin = cv2.imread(filePath)

# # Displaying the original image
# cv2.imshow('original image', image)
boundingBox = find_bouding_box(testArray)
print(find_bouding_box(testArray))

mask_img = create_mask(origin, boundingBox)

# cv2.imwrite("mask_{}".format(fileName), mask_img)
cv2.imshow('mask image', mask_img)

# masked_img = create_mask(origin, boundingBox)
# cv2.imshow('masked image', masked_img)
# cv2.imwrite("masked_{}".format(fileName), masked_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


