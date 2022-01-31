# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:25:07 2022

@author: ricky
"""
import cv2
import numpy as np

class ColorDetection:
    
    
    def __init__(self,color,file,formation):
        self.color=color
        self.file=file
        self.playerCoord=[]
        self.setPlayerCoord()
        self.formation=formation

    def Detection(self):
        l=0
        u=359
        if self.color =='purple':
            l=130
            u=200
        elif self.color == 'green':
            l=36
            u=86
        img = cv2.imread(self.file)
    
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
        lower_range = np.array([l,0,0])
        upper_range = np.array([u,255,255])
    
        mask = cv2.inRange(hsv,lower_range,upper_range)
        
        return(mask,img)
    
    
            
    def show(self):
        mask,img=self.Detection()
    
        contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.1* cv2.arcLength(contour, True), True)
            cv2.drawContours(img, [approx], 0, (0),4)    
        
        cv2.imshow("image",img)
        
    
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def setPlayerCoord(self):
        mask,img=self.Detection()
    
        contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
        playerCoord=[]
    
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.1* cv2.arcLength(contour, True), True)
            
            if len(approx)==4:
                x=0
                y=0
                for k in range(8):
                    if k%2==0:
                        x+=approx.ravel()[k]
                    else:
                        y+=approx.ravel()[k]
                playerCoord.append(x/4)
                playerCoord.append(y/4)
        self.playerCoord=playerCoord
    
    
    
    
    
    
    
    
    
    
    