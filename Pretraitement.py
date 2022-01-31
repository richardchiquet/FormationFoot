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
    path, dirs, files = next(os.walk("Formation"))
    
    for d in dirs:
        
        files = os.listdir("Formation/"+d)
        
        for file in files:
            
            img = cv2.imread("Formation/"+d+"/"+file)
            imgR = img[y1:y2,x1:x2]
            cv2.imwrite("FormationRogner/"+d+"/"+file,imgR)
            print("FormationRogner/"+d+"/"+file)
            
        
        

        
if __name__ =='__main__':    
        
    df = pd.DataFrame(columns = ['Formation','1x','1y','2x','2y','3x','3y','4x','4y','5x','5y','6x','6y','7x','7y','8x','8y','9x','9y','10x','10y','11x','11y'])      
    path, dirs, files = next(os.walk("FormationRogner"))
    
    
    for d in dirs:
    
        color,formation=d.split('-')[0],d.split('-')[1]        
        files = os.listdir("FormationRogner/"+d)
        
        for file in files:
            detection=ColorDetection.ColorDetection(color, "FormationRogner/"+d+"/"+file, formation)
            
            if len(detection.playerCoord)==22:
                
                df2= pd.DataFrame([[formation]+detection.playerCoord],columns=['Formation','1x','1y','2x','2y','3x','3y','4x','4y','5x','5y','6x','6y','7x','7y','8x','8y','9x','9y','10x','10y','11x','11y'])
                df=df.append(df2,ignore_index=True)
                print(formation,color,file)
        
    df.to_json("data.json",orient="columns")
    df.to_csv("data.csv")
    
        
    
    
    
            
        