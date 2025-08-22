import cv2,os
from PIL import Image,ImageFilter
import pytesseract
from pytesseract import Output
import re,math
import numpy as np
from scipy import ndimage
KYC_directory='C:/Users/chandan/Desktop/KYC - Copy - Copy'
folders_list=os.listdir(KYC_directory)
print('list of folders------>',folders_list)
for i in range(len(folders_list)):
    folders_dir=KYC_directory+'/'+folders_list[i]
    print('folders_dir------->',folders_dir)
    folder=os.chdir(folders_dir)
    files=os.listdir(folder)
    print('files------->',files)
    for j in range(len(files)):
        img=folders_dir+'/'+files[j]
        print('----->',img)
        img=cv2.imread(img)
        cv2.imshow('img',img)
        k=cv2.waitKey(0)
        pytesseract.pytesseract.tesseract_cmd=r'C:/Users/chandan/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
        d=pytesseract.image_to_string(img)
        aadhaar_number=''
        words=""
        for word in d.split('\n'):
            print('i before split ------>',word)
            word=word.split()
            print('i after split ------>',word)
            for i in range(len(word)):
                if len(word[i])==4 and word[i].isdigit():
                    words +=word[i]+' '
            print('words------>',words)
            word=words
            print('j------>',len(word))
            if len(word)<16:
                aadhaar_number = word
                aadhaar_number = aadhaar_number.split()
            print('aadhar number---->',aadhaar_number)
            if aadhaar_number != [] and len(aadhaar_number) ==3:
                d=pytesseract.image_to_data(img,output_type=Output.DICT)
                print('------->',d)
                n_boxes = len(d['level'])
                for k in range(n_boxes):
                    temp = d['text'][k]
                    if temp.isdigit():
                        # print('data------------>',d['conf'][i])
                        if (temp==aadhaar_number[0] or temp==aadhaar_number[1] or temp==aadhaar_number[2]):
                            (x, y, w, h) = (d['left'][k], d['top'][k], d['width'][k], d['height'][k])
                            cv2.rectangle(img, (x, y), (x + w + 2, y + h + 2), (54, 69, 79), -1)
                cv2.imshow('img',img)
                cv2.waitKey(0)
                cv2.destroyWindow('img')
                break










# h,w,c=img.shape
# print('H,W,C----->',h,w,c)
# remember full path of tesserract exe file
# Image details changes using PIL(python image library OR PILLOW) H-height,W-width,C-channel
# with Image.open(aadhar_img) as img:
#     img.load()
#     img.show() 
#     print(img.size)
#     # print('text------->',text')
print('-=========<><><><><><>==========-')
#     # crop_img = img.crop((100,900,300,1800))
#     # crop_img.show()
#     # print('crop_img------->',crop_img.size)
#     converted_img = img.transpose(Image.ROTATE_90)
#     converted_img.show()
#     gray_img = img.convert("L")
#     gray_img.show()
#     print('------------>',gray_img.getbands())
#     edges = gray_img.filter(ImageFilter.FIND_EDGES)
#     edges.show()
#     edges = gray_img.filter(ImageFilter.EMBOSS)
#     edges.show()

# Image creation using numpy
# arr = np.zeros((600,600))
# arr[200:400,200:400]=255
# print('arr------>',arr)
# img=Image.fromarray(arr)
# img.show()
# red_arr = np.zeros((600,600))
# green_arr = np.zeros((600,600))
# blue_arr = np.zeros((600,600))
# red_arr[150:350,150:350]=255
# green_arr[200:400,200:400]=255
# blue_arr[250:450,250:450]=255
# red_img=Image.fromarray(red_arr).convert("L")
# green_img=Image.fromarray(green_arr).convert("L")
# blue_img=Image.fromarray(blue_arr).convert("L")
# Main_img=Image.merge("RGB",(red_img,green_img,blue_img))
# print('------>',Main_img)
# Main_img.show()
