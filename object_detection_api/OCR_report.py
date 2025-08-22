import cv2,re
import pytesseract
from pytesseract import Output
# filename = 'C:/Users/chandan/Desktop/aadhar output/Laboratory-Blood-Test-Results.png'
report_Dict=[]
pytesseract.pytesseract.tesseract_cmd=r'C:/Users/chandan/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
img = cv2.imread('C:/Users/chandan/Desktop/aadhar output/Blood-Test-Results-on-Admission.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# adaptive_threshold = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,85,11)
cv2.imshow('image',gray_img)
cv2.waitKey(0)
config="--psm 1"
data = pytesseract.image_to_string(gray_img,config=config)
print('String data------------>',data)
final_dict={}
dict=[]
result=[]
keys=""
for i in data:
    keys += i
dict.append(keys)
# print('dictionary----->',dict)
for j in dict:
    key=j.split("\n")
    result.append(key)
# print('result----->',result[0])
for i in result[0]:
    # print('hhhhhhhh===>',i)
    # res_re=re.compile(r'd*')
    res=re.split('(\d+.*$)',i)
    # print(res)
    if len(res)>1:
        keys=res[0]
        # print('---->',keys)
        values=res[1]
        # print('----->',values)
        final_dict[keys]=values
print('final dictionary------>',final_dict)
# d = pytesseract.image_to_data(img, output_type='data.frame')
# print('data------------>',d)
# for text bounding box
# config="--psm 3"
# d = pytesseract.image_to_data(adaptive_threshold, output_type=Output.DICT,config=config)
# print('data------------>',d)
# # result = d['text']
# dict_keys=[]
# dict_values=[]
# print('result------------>',result)
# for i in result:
#     i=i.strip()
#     if len(i)>0:
#         if i.isalpha() and i !='to':
#             keys=i
#             dict_keys.append(keys)
#             continue
#         elif i.isnumeric():
#             values=i
#             dict_values.append(values)
#             continue
#         else:
#             values=i
#             dict_values.append(values)
# print('dictionary reslut------->',dict_keys)
# print('dictionary reslut------->',dict_values)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     if d['conf'][i] > 80:
#         # print('data------------>',d['conf'][i])
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# print('report_Dict result ------>',report_Dict)
# cv2.imshow('img', img)
# cv2.waitKey(0)