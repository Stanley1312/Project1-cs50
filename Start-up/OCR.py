import cv2 as cv
import pytesseract
import numpy as np
from pylab import array, plot, show, axis, arange, figure, uint8 
from PIL import Image
from pytesseract import Output


img = cv.imread('E:\Start-up/unnamed.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys)
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 50:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# d = pytesseract.image_to_boxes(img)
# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv.imshow('img', img)
cv.waitKey(0)





# def thresholding(image):
#     return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
#     # return cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 2)
#     # th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#     # th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# def sharpend(image):
#     gaussian_image = cv.GaussianBlur(image,(5,5),0)
#     # mask = image - gaussian_image
#     # result = image +  mask
#     return gaussian_image
# def unsharp_mask(image, kernel_size=(5, 5), sigma=3.0, amount=1.0, threshold=0):
#     """Return a sharpened version of the image, using an unsharp mask."""
#     blurred = cv.GaussianBlur(image, kernel_size, sigma)
#     sharpened = float(amount + 1) * image - float(amount) * blurred
#     sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
#     sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
#     sharpened = sharpened.round().astype(np.uint8)
#     if threshold > 0:
#         low_contrast_mask = np.absolute(image - blurred) < threshold
#         np.copyto(sharpened, image, where=low_contrast_mask)
#     return sharpened

# def erode(image):
#     # kernel = np.matrix('0 1 0 ; 1 1 1 ;0 1 0',dtype=np.uint8)
#     kernel = np.ones((3,3),np.uint8)
#     # image = cv.dilate(image, kernel, iterations = 1)
#     # image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
#     image = cv.dilate(image, kernel, iterations = 1)
#     return image
# def contrast(image):
#     phi = 1
#     theta = 1
#     maxIntensity = 255.0
#     # Increase intensity such that
#     # dark pixels become much brighter, 
#     # bright pixels become slightly bright
#     newImage0 = (maxIntensity/phi)*(image/(maxIntensity/theta))**0.4
#     newImage0 = array(newImage0,dtype=uint8)
#     newImage0 = (maxIntensity/phi)*(image/(maxIntensity/theta))**2
#     newImage0 = array(newImage0,dtype=uint8)
#     return newImage0


# im = Image.open(r"E:\Start-up\unnamed1.jpg")
# im.save(r"E:\Start-up\unnamed1-300.jpg", dpi=(300,300))

# im1 = Image.open(r"E:\Start-up\unnamed2.jpg")
# im1.save(r"E:\Start-up\unnamed2-300.jpg", dpi=(300,300))



# image1 = cv.imread(r"E:\Start-up\unnamed1-300.jpg",0)
# image2 = cv.imread(r"E:\Start-up\unnamed2-300.jpg",0)

# image1 = unsharp_mask(image1)
# image2 = unsharp_mask(image2)

# image1 = sharpend(image1)
# image2 = sharpend(image2)

# image1 = contrast(image1)
# image2 = contrast(image2)



# image1 = thresholding(image1)
# image2 = thresholding(image2)

# # image1 = erode(image1)
# # image2 = erode(image2)




# custom_config = r'--oem 3 --psm 6'
# print(pytesseract.image_to_string(image1, config=custom_config))
# print(pytesseract.image_to_string(image2, config=custom_config))
# # print(image1)
# cv.imshow("image1",image1)
# cv.imshow("image2",image2)
# cv.waitKey(0)