import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

template = cv2.imread('mushroom.jpg', 0)  #Small image (template)

def detectMushroom(inputImg):
    img_rgb = inputImg
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    # Calculate the metric for varying image sizes
    #pick the one that gives the best metric (e.g. Minimum Sq Diff.)

    best_match = None
    for scale in np.linspace(2.0, 2.5, 11):  #Pick scale based on your estimate of template to object in the image ratio
        print(scale)


    #Resize the input template image
        resized_template = imutils.resize(template, width = int(template.shape[1] * scale))

        res = cv2.matchTemplate(img_gray, resized_template, cv2.TM_SQDIFF)
        minval, maxLoc, minloc,  = cv2.minMaxLoc(res)  #Only care about minimum value and location as we are using TM_SQDIFF

        #Check if the min_val is the minimum compared to the value from other scales templates
        #If it is minimum then we got a better match compared to other scales
        #So save the value and location. 
        if best_match is None or min_val <= best_match[0]:
            ideal_scale=scale  #Save the ideal scale for printout. 
            h, w = resized_template.shape[::] #Get the size of the scaled template to draw the rectangle. 
            best_match = [min_val, min_loc, ideal_scale]
        
    return best_match[1]    # return location


    # print("Ideal template image size is : ", int(template.shape[0]ideal_scale), "x", int(template.shape[1]ideal_scale))

    #Save the image with a red box around the detected object in the large image. 
    # top_left = best_match[1]  #Change to max_loc for all except for TM_SQDIFF
    # bottom_right = (top_left[0] + w, top_left[1] + h)
    # cv2.rectangle(img_rgb, top_left, bottom_right, (0, 0,255), 2)  #Red rectangle with thickness 2. 
    # cv2.imwrite('matched_resized.jpg', img_rgb)