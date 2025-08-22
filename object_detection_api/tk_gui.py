# import tkinter as tk
# from tkinter import *
# window=tk.Tk()
# window.title('AADHAR MASKING GUI')
# window.geometry("900x400")
# def mask_program():
#     print('hello welcome to process!!!')
# my_button=Button(text='Start process',command=mask_program,width=20)
# my_button.grid(row=0,column=2,pady=10,padx=10)
# mask_font=('Times',75,'bold')
# mask_label=tk.Label(window,text="Masked Count")
# mask_label.grid(row=1,column=0)
# mask_count=tk.Label(window,bg='green',width=5,font=mask_font)
# mask_count.grid(row=1,column=1)
# # mask_label.grid(row=2,column=2,padx=50,pady=30)
# unmask_font=('Times',75,'bold')
# unmask_label=tk.Label(window,text="Unmasked Count")
# unmask_label.grid(row=1,column=2)
# unmask_count=tk.Label(window,bg='red',width=5,font=unmask_font)
# unmask_count.grid(row=1,column=3)
# window.mainloop()
# print('----------------------------------------------------------------------')
import tkinter  as tk 
my_w = tk.Tk()
my_w.geometry("350x170")  # width and height of the window

counter=11 # Initital value of counter
def my_time():
    global counter
    counter=counter-1 # decrease value by 1 
    if counter < 0:
        return
    
    l1.config(text=str(counter)) # Update the label text using string
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',76,'bold') # display size and style
l1=tk.Label(my_w,font=my_font,bg='yellow',width=2)
l1.grid(row=1,column=1,padx=50,pady=30)

my_time() # call the function 
my_w.mainloop()    
# print('----------------------------------------------------------------------')
# def validate(aadhaarNum):
#         print(aadhaarNum)
#         mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
#             [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
#             [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
#             [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
#         perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
#             [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
#             [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]
#         try:
#             i = len(aadhaarNum)
#             j = 0
#             x = 0
#             while i > 0:
#                 i -= 1
#                 x = mult[x][perm[(j % 8)][int(aadhaarNum[i])]]
#                 j += 1
#             if x == 0:
#                 return 1 
#             else:
#                 return 0 

#         except ValueError:
#             return 0 
#         except IndexError:
#             return 0 
# aadhaarNum=str(879202155228)
# result=validate(aadhaarNum)
# print('aadhar is valid or not------>',result)