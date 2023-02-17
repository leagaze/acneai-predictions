#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:45:58 2023

@author: Lea
"""

import cv2
import json
import matplotlib.pyplot as plt

images_path = 'acne04_dataset/Classification/JPEGImages/'
path_labels = "AcneAI_prediction_ACNE04_v1.json"
with open(path_labels, 'r') as f :
    labels_dict = json.load(f)
    for img_dict in labels_dict['images'] :
        img_id = img_dict['id']
        img = cv2.imread(images_path + img_dict['file_name'])
        
        annotations = [annotation_dict for annotation_dict in labels_dict['annotations'] if annotation_dict['image_id']==img_id]
        for annotation in annotations :
            cv2.circle(img, annotation['coordinates'], int(annotation['radius']),  (255,0,0), 1+int(max(img.shape[:2])/1000))
            cv2.putText(img,str(annotation['severity']), annotation['coordinates'],cv2.FONT_HERSHEY_SIMPLEX,img.shape[1]/1000,(0,0,255),thickness=1)
    
    
        plt.imshow(img[:,:,::-1])
        plt.show()
        cv2.imwrite(img_dict['file_name'], img)
