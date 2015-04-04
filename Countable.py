'''
PROJECT WHIPLASH

3rd April, 2015
'''

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
I = 0
while True:
    ret,im = cap.read()
    im = cv2.flip(im,1)
    cv2.rectangle(im, (340,20), (620,300), (255,0,0))
    
    img = im[20:300,340:620]
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("CROPPED", img)
    ret,thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    while I<100:
        cv2.putText(thresh, "LOADING...", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
        cv2.putText(thresh, "Keep your hand to the right.", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
        cv2.line(thresh, (50,90),(250,90),127)
        cv2.line(thresh, (50,110),(250,110),127)

        cv2.line(thresh, (50,20), (50,200),127)
        cv2.line(thresh, (70,20), (70,200),127)
        
        cv2.line(thresh, (150,60),(150,70),255)
        cv2.circle(thresh, (45,65),5,255)
        for j in range(I):
            cv2.line(thresh, (50+j,60), (50+j,70), I+100)
        I+=1
        cv2.imshow("CHECK",thresh)
        if cv2.waitKey(10) == 27:
            I=100
            break   
        break
    if I<100:
        continue
    cv2.destroyWindow("CHECK")
    flag = 0
    ctr = -1
    for i in range(thresh.shape[1]):
        if thresh[100][i] == 0 and flag == 0:
            continue
        if thresh[100][i] == 255 and flag == 0:
            ctr+=1
            flag = 1
            continue
        if thresh[100][i] == 0 and flag == 1:
            flag = 0
            continue
        if ctr>4:
            ctr = 999
            break
    thumb_det = 0
    for i in range(20,200):
        if thresh[i][60] == 0 and flag==0:
            continue
        if thresh[i][60] == 255 and flag == 0:
            thumb_det = 1
            flag = 1
        if thresh[i][60] == 0 and flag==1:
            flag = 0
        if thumb_det>1:
            break
    if ctr+thumb_det<=5:
        fings =  ctr+thumb_det
        cv2.putText(thresh,str(fings),(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    else:
        cv2.putText(thresh, "XXX", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    
    cv2.imshow("BINARY",thresh)
    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()
        break
                        
cap.release()

