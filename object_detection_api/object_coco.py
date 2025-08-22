import numpy as np
import tensorflow as tf
import cv2,json
from matplotlib import pyplot as plt
# load model from path
model= tf.saved_model.load("faster_rcnn_resnet50_v1_640x640_coco17_tpu-8/saved_model")
# read image and preprocess
json_file=open('classes_names.json','r')
json_model=json_file.read()
class_names=json.loads(json_model)
img = cv2.imread('input/chair.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(1,1,1)
plt.imshow(img)
plt.show()
# get height and width of image
h, w, _ = img.shape
input_tensor = np.expand_dims(img, 0)
# predict from model
resp = model(input_tensor)
class_arr_id=resp['detection_classes'].numpy()
class_id=class_arr_id[0][0]
class_arr_percent=resp['detection_scores'].numpy()
class_percent=class_arr_percent[0][0]
if class_percent > 0.8:
    name_of_object=class_names[str(int(class_id))]
    print('object is----->',name_of_object)
    print('confidence is------>',class_percent)


#iterate over boxes, class_index and score list
# for boxes, classes, scores in zip(resp['detection_boxes'].numpy(), resp['detection_classes'], resp['detection_scores'].numpy()):
#     for box, cls, score in zip(boxes, classes, scores): # iterate over sub values in list
#         if score > 0.8: # we are using only detection with confidence of over 0.8
#             ymin = int(box[0] * h)
#             xmin = int(box[1] * w)
#             ymax = int(box[2] * h)
#             xmax = int(box[3] * w)
#             # write classname for bounding box
#             # cv2.putText(img, class_names[cls], (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
#             # draw on image
#             cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (128, 0, 128), 4)
#             plt.subplot(1,1,1)
#             plt.imshow(img)
#             plt.show()

# convert back to bgr and save image
# cv2.imwrite("output/newchair.jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
