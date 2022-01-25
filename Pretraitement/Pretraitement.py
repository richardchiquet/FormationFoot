import cv2
import numpy as np
from PIL import Image
import os
import ColorDetection
import json
import pandas as pd
import json


def show():
    
    img = cv2.imread("Formation/green-352/SC-5224.jpg")
    rows,cols,_ = img.shape
    print("Rows",rows)
    print("Cols",cols)
    y1=305
    y2=810
    x1=535
    x2=1380
    imgR = img[y1: y2,x1: x2]
    cv2.imshow("imageR",imgR)
    
    
    
    #Region of interest
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0))
     
     
    cv2.imshow("image",img)
    cv2.waitKey(0)

def crop():
    y1=305
    y2=810
    x1=535
    x2=1380
    
    df = pd.DataFrame(columns = ['Formation','1','2','3','4','5','6','7','8','9','10','11'])
    
    
    path, dirs, files = next(os.walk("Formation"))
    file_count = len(files)
    
    for d in dirs:

        color,formation=d.split('-')[0],d.split('-')[1]
        
        files = os.listdir("Formation/"+d)
        
        for file in files:
            img = cv2.imread("Formation/"+d+"/"+file)
            imgR = img[y1:y2,x1:x2]
            cv2.imwrite("FormationRogner/"+d+"/"+file,imgR)
            print("FormationRogner/"+d+"/"+file)
            
        
        

        
if __name__ =='__main__':
    
    
    
    df = pd.DataFrame(columns = ['Formation','1','2','3','4','5','6','7','8','9','10','11'])
    
    path ='Formation'
    
    path, dirs, files = next(os.walk("TestRognerGreen"))
    file_count = len(files)
    for k in range(file_count):
        fileName = "TestRogner/SCR-"+str(k)+".jpg"
        detectionPurple = ColorDetection.ColorDetection("purple", fileName)
        if len(detectionPurple.playerCoord)!=11:
            pass#os.remove(fileName)
        else:
            df2= pd.DataFrame([[1]+detectionPurple.playerCoord],columns = ['Formation','1','2','3','4','5','6','7','8','9','10','11'])
            df=df.append(df2, ignore_index=True)

            
            
    path, dirs, files = next(os.walk("TestRogner"))
    file_count = len(files)
    
    for k in range(file_count):
        fileName = "TestRogner/SCR-"+str(k)+".jpg"
        detectionGreen = ColorDetection.ColorDetection("green", fileName)
        if len(detectionGreen.playerCoord)!=11:
            pass#os.remove(fileName)
        else:
            df2= pd.DataFrame([[1]+detectionGreen.playerCoord],columns = ['Formation','1','2','3','4','5','6','7','8','9','10','11'])
            df=df.append(df2, ignore_index=True)


    
    
    
    
    
    
            
        