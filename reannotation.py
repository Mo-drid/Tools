import xml.etree.ElementTree as ET
import os
import glob
import math
import numpy as np

w_img = 1920
h_img= 1080
def scale(x):
    xmin=float(x.find('xmin').text)
    ymin=float(x.find('ymin').text)
    xmax=float(x.find('xmax').text)
    ymax=float(x.find('ymax').text)

    w=xmax-xmin
    h=ymax-ymin

    xcenter = (xmin + w/2) / w_img
    ycenter = (ymin + h/2) / h_img
    w = w / w_img
    h = h / h_img
    return [round(xcenter,3),round(ycenter,3),round(w,3),round(h,3)]

Dataset_names = ['person','sports ball']
def ParseXML(img_folder):
    for xml_file in glob.glob(img_folder+'/*.xml'):
        # print(img_folder)
        tree=ET.parse(open(xml_file))
        root = tree.getroot()
        image_name = root.find('filename').text
        img_path = img_folder+'/'+image_name
        f = open("{}.txt".format(image_name[:-4]), "w")
        for i, obj in enumerate(root.iter('object')):
            # difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls == 'person':#['player', 'referee', 'other']:
                # cls =  'person'
                label=0
                print(cls)

            else:
                cls = 'sports ball'
                label=1
            # if cls not in Dataset_names:
            #     Dataset_names.append(cls)
            
            # cls_id = Dataset_names.index(cls)
            xmlbox = obj.find('bndbox')
            lst = scale(xmlbox)
            OBJECT = (str(label)+' '
                      + str(lst[0])+' '
                      +str(lst[1])+' '
                      +str(lst[2])+' '
                      +str(lst[3])
                      )
            
            # print(img_path)
            f.write(OBJECT+'\n')
            
        f.close()

ParseXML(r"E:\New folder\1000_img_annot\train\xml")

