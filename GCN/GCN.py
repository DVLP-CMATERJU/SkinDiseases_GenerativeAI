# -*- coding: utf-8 -*-

'''
---- Disclaimer ----
This is the official code release for the paper titled -

"Improvement of skin disease identification system using Generative AI"

Please cite our work if you find this useful.

Copyright 2019, Bisakh Mondal, Nibaran Das, K.C. Sontosh, Mita Nasipuri, All rights reserved.

---- Prerequisite Packages/ API ----
requirements.txt

---- Description ----
The purpose of this code is to  provide a ready to use functionality for Global contrast
Normalization, an algorithm which is used to prevent images from having varying amount of
contrast.

'''
# IMPORTS
import os
from PIL import Image
import numpy
import imageio
import cv2
import numpy as np

# Basic Parameters
root='< add source dir >' # the directory where images are stored

save_dir_GCN='<destination dir after GCN >' # Directory where images stored after GCN

save_dir_noise='<destination dir after GCN and Morph. trans.>'

images=os.listdir(root) # list of all images in source dir

imgs=[root+img  for img in images] # full path of source Images

NUM_ITER='int <Number of iterations for morphological transform>'

'''
This is the Utility Function which contains the implementation of Global
Contrast Normalization.

PARAMETERS:

'filename': The image file ('.png','.jpeg','.jpg','.bmp') on which GCN will
            be applied.
'lmda' :    Lambda value, a positive regularization term to bias the std
            deviation.
's'     :   A constant: default is generally 1.
'epsilon':  A term in denominator where denominator is constrained to be at
            least epsilon.
            default value 0.000000001

'''
def global_contrast_normalization(filename, s, lmda, epsilon = 0.000000001):
    X = numpy.array(Image.open(filename)) # load image and convert to Numpy array
    X_average = numpy.mean(X) # calculate mean
    X = X - X_average
    contrast = numpy.sqrt(lmda + numpy.mean(X**2))

    X = s * X / max(contrast, epsilon) # Normalization
    X.astype('uint8') # conversion to int type
    imageio.imwrite(os.path.join(save_dir_GCN,filename), X) # store image in destination dir.


'''
function_name: morph_transform
This is the Utility Function which contains the implementation of 2 popular morphological
transformation used in denoising.

'''
def morph_transform(itr):
    new_images=os.listdir(save_dir_GCN+root) # load the Normalised image
    imgs_gcn=[save_dir_GCN+root+img  for img in images] # list of GCN'ed images with full path.
    img_count=0
    for i in imgs_gcn:
        img=cv2.imread(i) #load image
        #removed noise
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=itr) # Dilation
        img = cv2.erode(img, kernel, iterations=itr) # Erosion

        cv2.imwrite(save_dir_noise+root+f'{img_count}.bmp',img)
        img_count+=1

if __name__=="__main__":
    for i in imgs:
        global_contrast_normalization(i, 1, 10)
    
    morph_transform(NUM_ITER)
