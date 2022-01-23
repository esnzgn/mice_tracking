ام#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:23:28 2021

@author: chchinta
"""
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
#import seaborn as sns

def locate(img, img_bg,threshold):
    '''Locates the x,y positions of mouse in img while 
    background is img_bg, and at a given threshold'''
    diff = np.abs(img_bg-img)  
    # above is to turn negative values corresponding to mouse into positive
    bw = np.zeros_like(diff)  # create an empty image thas all black
    mouse_indx = np.where(diff>threshold)  # locate mouse using thresholding
    bw[mouse_indx] = 1
    mouse_y = mouse_indx[0].mean()  # imread inverts x,y
    mouse_x = mouse_indx[1].mean()
    return mouse_x, mouse_y

#f'{color[0]}/'
color = ['white','black']
time_spnt = np.empty((2,3))

for clr in color:
    if clr == color[0]:
        # Load background image
        img_01 = plt.imread(f'images-{color[0]}/img031.jpeg')[:, :, 0].astype(float)  # only take red values
        img_02 = plt.imread(f'images-{color[0]}/img021.jpeg')[:, :, 0].astype(float)  # only take red values
        
        yh = int(img_01.shape[0]/2)
        ye = int(img_02.shape[0])
        
        img_bg_ha = img_01[range(0,yh),:]
        #plt.imshow(img_bg_ha)
        
        img_bg_hb = img_02[range((yh),(ye)),:]
        #plt.imshow(img_bg_hb)
        
        img_bg = np.concatenate((img_bg_ha,img_bg_hb),0)
        #plt.imshow(img_bg)
    else:
        img_bg = plt.imread('black_background.jpeg') # Already in R
    
    img_bg = np.array(img_bg, dtype=float)  # Convert into floats or simply add .astype(float) to above line
    
    # Locate mice in the first frame
    if clr == color[0]:
        img = plt.imread(f'images-{color[0]}/img001.jpeg')[:, :, 0].astype(float)  # only take red values
    else:
        img = plt.imread(f'images-{color[1]}/img001.jpeg')[:, :, 0].astype(float)  # only take red values
    #  # Uncomment the next 4 lines to verify your thresholding of one such image
    # print('File number to test (1-600):')  # prompt user to enter a number
    # filenumber = int(input())  # convert the number into an integer
    # img = plt.imread(f'images-{color[0]}/img%03d.jpeg' %filenumber)[:, :, 0]  # only red values
    # img = np.array(img, dtype=float)
    
    
    plt.subplot(131)
    plt.imshow(img, cmap='gray')  # show orig in gray scale
    plt.subplot(132)
    plt.imshow(img-img_bg, cmap='gray')  # show the diff between background and image
    if clr == color[0]:
        threshold=10
        mouse_x, mouse_y = locate(img, img_bg, threshold)  # locate mouse
    else:
        threshold=40
        mouse_x, mouse_y = locate(img, img_bg, threshold)  # locate mouse
        
    plt.scatter(mouse_x, mouse_y, color='r', s=1)  # place a pointer at the centre of mouse
    
    # # How to guess the threshold (refer to class6)
    # diff = img - img_bg  # negative values is where mouse is at
    # plt.hist(diff.flatten(), 100)  # intensity values x-axis versus number of occurances y-axis
    # # above shows most values near zero but some values at -140, 20
    # abs_diff = np.abs(diff)  # instead convert into positive values
    # plt.hist(abs_diff.flatten(), 100)  # 
    # plt.ylim(0, 200)  # To figure out 
    # plt.show()
    
    # Locating mouse in all the 600 frames
    xs = []  # empty list to store x values
    ys = []  # empty list to store y values
    for ii in range(1, 601):
        if clr == color[0]:
            fname = f'images-{color[0]}/img%03d.jpeg' %(ii)
        else:
            fname = f'images-{color[1]}/img%03d.jpeg' %(ii)
            
        img = plt.imread(fname)[:, :, 0].astype(float)
        x, y = locate(img, img_bg,threshold)
        xs.append(x)
        ys.append(y)
    plt.subplot(133)
    plt.imshow(img_bg, cmap='gray')
     plt.plot(xs, ys, linewidth=0.5)
    plt.show()
    
    # time spent in each chamber
    count_left = 0
    count_right = 0
    count_middle = 0
    for x in xs:
        if x <= 270:  # Based on the image displayed
            count_left = count_left + 1
        elif x >= 460:
            count_right = count_right + 1 
        else:
            count_middle = count_middle + 1
    print('Time spent in left, middle, right chambers:')
    print(count_left, count_middle, count_right)
    if clr == color[0]:
        time_spnt[0,:] = [count_left, count_middle, count_right]
    else:
        time_spnt[1,:] = [count_left, count_middle, count_right]
    
# data set
x = ['chamber left', 'chamber central', 'chamber right']
y1 = time_spnt[0,:]
y2 = time_spnt[1,:]

# plot stacked bar chart 
plt.bar(x, y1, color='lightgrey',label='white mouse')
plt.bar(x, y2, bottom=y1, color='black',label='black mouse')
plt.legend(loc='upper right')
plt.show()