from pikepdf import Pdf, PdfImage, Name  # pip install pikepdf 
import zlib,os
from PIL import Image
import time

example = Pdf.open('C:/Users/chandan/Desktop/object_detection/object_detection/input/aadharPan.pdf')
page1 = example.pages[0]
print(list(page1.images.keys()))
rawimage = page1.images['/IM10']
pdfimage = PdfImage(rawimage)
print('pdfimage--------->',type(pdfimage))
print('pdfIMagecolor-------->',pdfimage.obj) # obj gives us detailed object Image width,height
ImageView = pdfimage.extract_to(fileprefix='image')
print('ImageView------>',ImageView)


rawimage = pdfimage.obj
print('rawimage-------->',rawimage)
pillowimage = pdfimage.as_pil_image()
pillowimage.show()

im = Image.open("C:/Users/chandan/Desktop/object_detection/object_detection/input/ac8.jpg")
im = im.resize((pillowimage.width, pillowimage.height))
im.show()

# grayscale = pillowimage.convert('L')
# grayscale = grayscale.resize((735, 735))
# rawimage.write(zlib.compress(grayscale.tobytes()),filter=Name("/FlateDecode"))

rawimage.write(zlib.compress(im.tobytes()),filter=Name("/FlateDecode"))
rawimage.ColorSpace = Name("/DeviceRGB")
rawimage.Width, rawimage.Height = pillowimage.width, pillowimage.height
example.save('C:/Users/chandan/Desktop/object_detection/object_detection/input/NewaadharPan.pdf')

# OBJECT_ID = "/IM10"

# def replace_image(filepath, new_image):
#     f = open(filepath, "rb")
#     contents = str(f.read())
#     for i in contents:
#         print(i,sep=" ")
#         time.sleep(0.2)
#     f.close()

#     image = Image.open(new_image)
#     width, height = image.size
#     NewImagelength = os.path.getsize(new_image)
#     print('size-------->',width,height,NewImagelength)

#     start = contents.find(OBJECT_ID)
#     stream = contents.find("stream", start)
#     image_beginning = stream + 7
#     print('--------->',start,stream,image_beginning)
#     meta = contents[start: image_beginning]
#     print('--------->',meta)
#     meta = meta.split("\n")
#     new_meta = []
#     for item in meta:
#         if "/Width" in item:
#             new_meta.append("/Width {0}".format(width))
#         elif "/Height" in item:
#             new_meta.append("/Height {0}".format(height))
#         elif "/Length" in item:
#             new_meta.append("/Length {0}".format(NewImagelength))
#         else:
#             new_meta.append(item)

#     new_meta = "\n".join(new_meta)
#     new_meta = bytes(new_meta,'utf-8')
#     # Find the end location
#     image_end = contents.find("endstream", stream) - 1

#     # read the image
#     f = open(new_image, "rb")
#     new_image_data = f.read()
#     print('new_image_data---.',type(new_image_data))
#     f.close()

#     # recreate the PDF file with the new_sign
#     with open(filepath, "wb") as f:
#         f.write(bytes(contents[:start],'utf-8'))
#         f.write(new_meta)
#         f.write(new_image_data)
#         f.write(bytes(contents[image_end:],'utf-8'))

# replace_image("C:/Users/chandan/Desktop/object_detection/object_detection/input/aadharPan.pdf", "C:/Users/chandan/Desktop/object_detection/object_detection/input/a.jpg")