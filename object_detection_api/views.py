from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
from matplotlib import pyplot as plt
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import pickle
import pdfplumber
import re

img_file='C:\\Users\\chandan\\Desktop\\object_detection\\object_detection\\input'
img_file1='C:\\Users\\chandan\\Desktop\\object_detection\\object_detection\\pneumonia_Images'
model = tf.keras.models.load_model('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/next_words.h5')
tokenizer = pickle.load(open('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/token.pkl','rb'))
# Create your views here.
@csrf_exempt
def objectapi(request):
    response={}
    image_json=request.FILES['file']
    print('json_image--------->',image_json.name)
    fs=FileSystemStorage(location=img_file)
    img_name=fs.save(image_json.name,image_json)
    print('imgname------------->',img_name)
    imgurl='C:/Users/chandan/Desktop/object_detection/object_detection/input/'+img_name
    print('imgurl------------->',imgurl)
    model= tf.saved_model.load("object_detection/faster_rcnn_resnet50_v1_640x640_coco17_tpu-8/saved_model")
    json_file=open('object_detection/classes_names.json','r')
    json_model=json_file.read()
    class_names=json.loads(json_model)
    img=cv2.imread(imgurl)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
        response['status']=200
        response['object']=str(name_of_object)
        response['confidence']=str(class_percent)
        print('------------------->',response)
        return JsonResponse(json.dumps(response),safe=False)
    else:
        return JsonResponse(json.dumps(response),safe=False)


@csrf_exempt
def pneumonia_api(request):
    response={}
    image_json=request.FILES['file']
    print('json_image--------->',image_json.name)
    fs=FileSystemStorage(location=img_file1)
    img_name=fs.save(image_json.name,image_json)
    print('imgname------------->',img_name)
    type=request.POST.get('type')
    print('type------------->',type)
    imgurl='C:/Users/chandan/Desktop/object_detection/object_detection/pneumonia_Images/'+img_name
    print('imgurl------------->',imgurl)
    if type=='pneumonia':
        load_model = tf.keras.models.load_model('C:/Users/chandan/Desktop/object_detection/object_detection/pneumonia_model.h5')
        print('load_model------------->',load_model)
        img=image.load_img(imgurl,target_size=(256,256))
        img=image.img_to_array(img)/255
        img=np.array([img])
        print('-------------->',img.shape)
        predict = load_model.predict(img)
        print('predict--------------->',predict)
        response['accuracy_for_pneumonia--->']=float(str(predict[0][0]))
        print(response)
        return JsonResponse(json.dumps(response),safe=False)
    elif type=='tb':
        load_model = tf.keras.models.load_model('C:/Users/chandan/Desktop/object_detection/object_detection/tb_health.h5')
        print('load_model------------->',load_model)
        img=image.load_img(imgurl,target_size=(256,256))
        img=image.img_to_array(img)/255
        img=np.array([img])
        print('-------------->',img.shape)
        predict = load_model.predict(img)
        print('predict--------------->',predict)
        response['accuracy_for_tuberculosis--->']=str(np.format_float_positional(predict[0][0], trim="-"))
        print(response)
        return JsonResponse(json.dumps(response),safe=False)
    return JsonResponse(json.dumps(response),safe=False)  

@csrf_exempt
def smart_compose(request):
    return render(request,'smart_compose.html')


@csrf_exempt
def predict_next_words(model,tokenizer,text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ""
    for key,value in tokenizer.word_index.items():
        if value==preds:
            predicted_word = key
            break

    print('predicted_word_is--->',predicted_word)
    return predicted_word

@csrf_exempt
def text_from_textarea(request):
    response = {}
    if request.method =='POST':
        print('----you are in text_from_textarea function--------')
        print(request.body)
        text = request.POST.get('result')
        text = text.split(" ")
        print('text------->',text)
        if(text=='0'):
            print('executaion completed')
        else:
            text = text[-3:]
            print('text is ---->',text)

            output = predict_next_words(model,tokenizer,text)
            response['output']=output
            print(response)
            return JsonResponse(json.dumps(response),safe=False)

@csrf_exempt
def report_pdf(request):
    if request.method == 'POST':
        print('<>-------------you are inside report pdf---------<>')
        pdf_file =request.FILES['report pdf']
        print('pdf_file--------->',pdf_file.name)
        with pdfplumber.open(pdf_file) as pdf:
            pages=pdf.pages[0]
            text=pages.extract_text()
        print('text--------->',text)
        dict_res={}
        for i in text.split('\n'):
            keys=''
            # result=re.split(r'\d+\.\d+',i)
            result=re.split(r'(\d+\.\d+)',i)
            print('result before----------->',result)
            if len(result)>1:
                print('result----------->',result[0],result[1])
                if result[0][0].isdigit():
                    keys=result[0].split(' ',maxsplit=1)
                    keys=keys[1]
                    values=result[1]
                    print('keys----------->',keys)
                    print('values-------->',values)
                else:
                    keys=result[0]
                    values=result[1]
                    print('keys----------->',keys)
                    print('values----------->',values)
                dict_res[keys]=values      
        dict_res=json.dumps(dict_res)
        print('Dictionary values--------->',dict_res)  
        return JsonResponse(dict_res,safe=False)