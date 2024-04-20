
import numpy as np
from scipy import ndimage


import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def main(unused_argv):

    """In the code here before, numpy has been used to work on the image. The .imread() func - 
    tion will find the picture at the given location and convert the image into a numpy array 
    which is the representation of the image in vectors. 
    Then, the for loop will iterate from 0 to 360, with 360 excluded, and rotate the loaded pic- 
    ture by rearranging the vectors through the .rotate() function. After that step, the .imsave() 
    function save the pictures to the given path. 
    27  
    All those steps are repeated 360 times in order to create my data. Being a proof of con- 
    cept, I wanted to demonstrate that it was possible to detect those shapes and convert  
    them to code. That dataset has been used to aim to train the prototype of AI I present."""


    picture = ndimage.imread("picture.png", flatten=True)
    paragraph = ndimage.imread("paragraph.png", flatten=True)
    picture_rot_array = [] 
    picture_array_labels = [] 
    paragraph_rot_array = [] 
    paragraph_array_labels = []

    for x in range(0, 360):
        picture_rot = ndimage.rotate( 
            picture, x, reshape=False, mode='constant',cval=100)
        picture_rot_array.append(picture_rot)
        picture_array_labels.append("picture")
        mpimg.imsave("picture_rot" + str(x) + ".png", picture_rot, cmap=plt.cm.gray)

        paragraph_rot = ndimage.rotate( 
            paragraph, x, reshape=False, mode='constant',cval=100)
        
        paragraph_rot_array.append(paragraph_rot)
        paragraph_array_labels.append("paragraph")
        mpimg.imsave("paragraph_rot" + str(x) + ".png", paragraph_rot,cmap=plt.cm.gray)

    print("Done")

