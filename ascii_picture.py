from PIL import Image
import numpy as np
import random
import sys
import os

# Input (argv):  
# 1. path to image
# 2. sharpness (int between 1 and 255)
# 3. heigth (int 0<)
# 4. width (int 0<)
# Output: 
# Print ascii pic in terminal

default_height = 80
default_width = 160

def check_argv():
    global path, sharpness, height, width 
    try:
        path = sys.argv[1]
    except IndexError:
        print("Give an image path as first argument")
        sys.exit()
    if not os.path.exists(path):
        print("Give a valid image path as first argument")
        sys.exit()
    try:
        sharpness = int(sys.argv[2])
    except IndexError:
        print("Using default sharpness = ", sharpness)
    try:
        height = int(sys.argv[3])
    except IndexError:
        print("Using default height = ", height)
    if height<0:
        height = default_height
    try:
        width = int(sys.argv[4])
    except IndexError:
        print("Using default width = ", width)
    if width<0:
        width = default_width
    

if __name__=="__main__":
    sharpness = 180
    height = default_height
    width = default_width
    check_argv()
    
    im = Image.open(path)
    im_grey = im.convert('L')
    im_bw = im_grey.point(lambda x: 0 if x<sharpness else 255,'1')
    bw_ar = np.array(im_bw)
    im_dim = bw_ar.shape
    if height>im_dim[0]: 
        height = im_dim[0]
    elif width>im_dim[1]:
        width = im_dim[1]

    txt_im = ""
    height_stride = int(im_dim[0]/height)
    width_stride = int(im_dim[1]/width)
    ascii_set = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    #No padding 
    for h_ind in range(height):
        for w_ind in range(width):
            sub_im = bw_ar[height_stride*h_ind:height_stride*(h_ind+1),width_stride*w_ind:width_stride*(w_ind+1)]
            n_white = len(sub_im[sub_im==True])
            if n_white>height_stride*width_stride/2:
                txt_im += ' '
            else:
                txt_im += random.choice(ascii_set)
        txt_im += '\n'

    print(txt_im)