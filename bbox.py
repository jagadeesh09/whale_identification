import os
import numpy as np
import cv2


bbox_file = 'cropping.txt'
img_folder = '../dataset/train'


def get_bounding_boxes(file_name):
    boxes  = []
    with open(bbox_file,'r') as f:
        f = f.readlines()  
    for box in f:
        bbox = {}
        box = box.strip()
        box = box.split(',')
        bbox['image'] = box[0]
        coords = box[1:]
        points = []
        for i in range(0,len(coords),2):
            x = float(coords[i])
            y = float(coords[i+1])
            points.append([x,y])
        points = np.asarray(points)
        print(points)
        [xmax,ymax] = np.amax(points,axis=0)
        [xmin,ymin] = np.amin(points,axis=0)
        bbox['coords'] = [xmin,ymin,xmax,ymax]
        boxes.append(bbox)

    return boxes  
    

def convert_to_yolo(root_folder='./',boxes):
    for box in boxes:
        img_name = box['image']
        img_path = os.join(root_folder,img_name)
        if not os.path.isfile(img_path):
            continue
        img = cv2.imread(img_path)
        height, width, channels = img.shape
        [xmin, ymin, xmax, ymax] = box['coords']

        x = xmin/float(width)
        y = ymin/float(height)
        w = (xmax-xmin)/float(width)
        h = (ymax-ymin)/float(height)

        

