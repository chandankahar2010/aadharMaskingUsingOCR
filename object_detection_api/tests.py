import fitz  # pip install PyMuPDF and Pillow
import io
from PIL import Image
  
# STEP 2
# file path you want to extract images from
file = "C:/Users/chandan/Desktop/object_detection/object_detection/input/aadharPan.pdf"
  
# open the file
pdf_file = fitz.open(file)
img_list = pdf_file.get_page_images(0, full=True)
print('img_list----------->',img_list)
# STEP 3
# iterate over PDF pages
for page_index in range(len(pdf_file)):
  
    # get the page itself
    page = pdf_file[page_index]
    image_list = page.get_images()
  
    # printing number of images found in this page
    if image_list:
        print(
            f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.get_images(), start=1):
  
        # get the XREF of the image
        xref = img[0]
        print(xref)
  
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]

        imageSave = fitz.Pixmap(pdf_file,xref)
        print('imageSave---->',imageSave.n)
        if imageSave.n < 5:
            imageSave.save("C:/Users/chandan/Desktop/object_detection/object_detection/input/-%x.jpg" % xref)
  
        # get the image extension
        image_ext = base_image["ext"]
        print('image extension------->',image_ext)


for page in pdf_file:
    pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,
                          colorspace=fitz.csRGB, clip=None, alpha=False, annots=True)
    pix.save("C:/Users/chandan/Desktop/object_detection/object_detection/input/samplepdfimage-%i.jpg" % page.number)




# Linux System
import pytesseract

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Example usage
from PIL import Image

img = Image.open('/home/hexa/Downloads/7.png')
text = pytesseract.image_to_string(img)

print(text)


