import cv2,re,os
import xlsxwriter
import pytesseract
from pytesseract import Output
import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title('AADHAR MASKING GUI')
window.geometry("550x250")
def aadhar_masking():
    KYC_directory='C:/Users/chandan/Desktop/KYC/'
    Copy_file_directory='C:/Users/chandan/Desktop/Copy KYC Folder'
    folders_list=os.listdir(KYC_directory)
    print('list of folders------>',folders_list)
    masked_count=0
    unmasked_count=0
    mask_book=xlsxwriter.Workbook('C:/Users/chandan/Desktop/masked aadhar.xlsx')
    unmask_book=xlsxwriter.Workbook('C:/Users/chandan/Desktop/unmasked aadhar.xlsx')
    mask_sheet = mask_book.add_worksheet()
    unmask_sheet = unmask_book.add_worksheet()       
    mask_row=0
    mask_column=0
    unmask_row=0
    unmask_column=0
    my_button["state"]=DISABLED
    for i in range(len(folders_list)):
        folders_dir=KYC_directory+folders_list[i]
        print('folders_dir------->',folders_dir)
        folder=os.chdir(folders_dir)
        files=os.listdir(folder)
        print('files------->',files)
        for j in range(len(files)):
            img=folders_dir+'/'+files[j]
            print('----->',img)
            img=cv2.imread(img)
            print('image---------->',img)
            # directory='C:/Users/chandan/Desktop/aadhar output'
            # gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            pytesseract.pytesseract.tesseract_cmd=r'C:/Users/chandan/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
            # cv2.imshow('img',img)
            # cv2.waitKey(0)
            d=pytesseract.image_to_string(img)
            aadhaar_number=''
            new_aadhaar_number=[]
            print('new_aadhaar_number-------->',new_aadhaar_number)
            for word in d.split('\n'):
                print('i------>',word.strip())
                print('j------>',len(word.strip()))
                if len(word)==14:
                    aadhaar_number = word
                    aadhaar_number = aadhaar_number.split()
                    count = len(aadhaar_number)
                    for digit in range(count):
                        temp=aadhaar_number[digit]
                        if temp.isdigit():
                            new_aadhaar_number.append(temp)
                    print('aadhar number---->',aadhaar_number)
                    print('new_aadhar number---->',new_aadhaar_number)
            if new_aadhaar_number != []:
                file_copy=files[j]
                path=os.path.join(Copy_file_directory,folders_list[i]+'Copy')
                print('path=------<>',path)
                os.mkdir(path)
                os.chdir(path)
                new_file_copy=file_copy.split('.')
                file_copy=new_file_copy[0]+'_Copy.'+new_file_copy[1]
                cv2.imwrite(file_copy,img)
                d=pytesseract.image_to_data(img,output_type=Output.DICT)
                print('------->',d)
                n_boxes = len(d['level'])
                for k in range(n_boxes):
                    temp = d['text'][k]
                    if temp.isdigit():
                        # print('data------------>',d['conf'][i])
                        if temp==new_aadhaar_number[0] or temp==new_aadhaar_number[1] or temp==new_aadhaar_number[2]:
                            (x, y, w, h) = (d['left'][k], d['top'][k], d['width'][k], d['height'][k])
                            cv2.rectangle(img, (x, y), (x + w, y + h), (54, 69, 79), -1)
                masked_img=folders_dir+'/'+files[j]
                print('masked_img-------->',masked_img)
                masked_count=masked_count+1
                mask_count.config(text=str(masked_count))
                window.update()
                # mask_label(1000,aadhar_masking)
                print('masked count inside loop------------<>',masked_count)
                mask_sheet.write(mask_row, mask_column, masked_img) 
                mask_row += 1 
                os.chdir(folders_dir)
                cv2.imwrite(files[j], img)
                # cv2.imshow('img',img)
                # cv2.waitKey(0)
            else:
                unmasked_count=unmasked_count+1
                unmask_count.config(text=str(unmasked_count))
                window.update()
                # unmask_label(1000,aadhar_masking)
                print('unmasked count inside loop------------<>',unmasked_count)
                unmasked_img=folders_dir+'/'+files[j]
                print('unmasked image----------->',unmasked_img)
                unmask_sheet.write(unmask_row, unmask_column, unmasked_img)
                unmask_row += 1 
                continue
        print('i is ---------------->',i)
        print('folders_list is ---------------->',len(folders_list))
        if i==(len(folders_list)-1):
            task_complete.config(text='Aadhar masking is completed.')
    mask_book.close()
    unmask_book.close()
    print('masked count------------<>',masked_count)
    print('---------<><><><><><>---------------')
    print('unmasked count------------<>',unmasked_count)
my_button=Button(text='Start process',command=aadhar_masking)
my_button.grid(row=0,column=2,pady=10,padx=10)
mask_font=('Times',75,'bold')
mask_label=tk.Label(window,text="Masked Count")
mask_label.grid(row=1,column=0)
mask_count=tk.Label(window,bg='green',width=2,font=mask_font)
mask_count.grid(row=1,column=1)
# mask_label.grid(row=2,column=2,padx=50,pady=30)
unmask_font=('Times',75,'bold')
unmask_label=tk.Label(window,text="Unmasked Count")
unmask_label.grid(row=1,column=2)
unmask_count=tk.Label(window,bg='red',width=2,font=unmask_font)
unmask_count.grid(row=1,column=3)
task_font=('Times',12,'bold')
task_complete=tk.Label(window,font=task_font)
task_complete.grid(row=2,column=2,pady=5)
window.mainloop()