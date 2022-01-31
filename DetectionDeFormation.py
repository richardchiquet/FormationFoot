import pyautogui as pag
import pandas as pd
import cv2
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample
import time
import numpy as np

import ColorDetection

start=time.time()
url = 'https://raw.githubusercontent.com/richardchiquet/FormationFoot/main/data-modified.csv'

df = pd.read_csv(url,index_col=0)
df1 = pd.read_csv(url,index_col=0)

df_majority1 = df[df['Formation']==433]
df_majority2 = df[df['Formation']==4231]
df_majority3 = df[df['Formation']==352]
df_majority4 = df[df['Formation']==442]

maj_class1 = resample(df_majority1, 
                                 replace=True,     
                                 n_samples=1324,    
                                 random_state=123) 
maj_class2 = resample(df_majority2, 
                                 replace=True,     
                                 n_samples=1324,    
                                 random_state=123) 
maj_class3 = resample(df_majority3, 
                                 replace=True,     
                                 n_samples=1324,    
                                 random_state=123) 
maj_class4 = resample(df_majority4, 
                                 replace=True,     
                                 n_samples=1324,    
                                 random_state=12)

df=pd.concat([maj_class1,maj_class2,maj_class3,maj_class4])

X = df.iloc[:,1:23].values
y = df.iloc[:,0].values




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)



sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)




classifier = RandomForestClassifier(n_estimators=65,random_state=0)
classifier.fit(X_train,y_train)
end=time.time()-start
print("L'entrainement est fini, l'entrainement a duré: "+str(end))

if __name__=="__main__":
    
    inp=input("Quel formation voulez-vous connaitre?(green/purple)\n")
    df = pd.DataFrame(columns = ['Formation','1x','1y','2x','2y','3x','3y','4x','4y','5x','5y','6x','6y','7x','7y','8x','8y','9x','9y','10x','10y','11x','11y'])
    
    if inp=='green' or inp=='purple':
        
        while(df.shape[0]<20):
            screen= pag.screenshot()
            screen.save("temp.jpg")
            y1=305
            y2=810
            x1=535
            x2=1380 
            img = cv2.imread("temp.jpg")
            imgR = img[y1:y2,x1:x2]
            cv2.imwrite("tempR.jpg",imgR)
            detection=ColorDetection.ColorDetection(inp, "tempR.jpg","0")
            if len(detection.playerCoord)==22:
                              df2= pd.DataFrame([[0]+detection.playerCoord],columns=['Formation','1x','1y','2x','2y','3x','3y','4x','4y','5x','5y','6x','6y','7x','7y','8x','8y','9x','9y','10x','10y','11x','11y'])
                              df=df.append(df2,ignore_index=True)
            time.sleep(0.5)
        Xd = df.iloc[:,1:23].values
        Xd = sc.fit_transform(Xd)
        yd=classifier.predict(Xd)
        counts = np.bincount(yd)
        print(np.argmax(counts))
        
                
        
            

            
            
            