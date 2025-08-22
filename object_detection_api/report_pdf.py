import pdfplumber
import re
url='C:/Users/chandan/Desktop/aadhar output/HARISH_SHAIKH.pdf'
# url='C:/Users/chandan/Desktop/aadhar output/WC12.pdf'
with pdfplumber.open(url) as pdf:
    pages=pdf.pages[2]
    text=pages.extract_text()
print('text--------->',text)
# res_re=re.compile(r'd')
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
print('Dictionary values--------->',dict_res)           
        
            
                          

