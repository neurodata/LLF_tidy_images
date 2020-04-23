#!/usr/bin/env python
from PIL import Image
from PIL import ImageOps
from math import floor, sqrt
from scipy.io import loadmat
from collections import deque
import csv
import glob
import os
import numpy as np
import argparse
import configparser
import pandas as pd


## The spec
## dictionary = {"dataset" : dataset = [{'filename':filename, 'label':label]}


def get_Object101(directory):
   
    ob101 = directory + "101_ObjectCategories/" 
    folders = os.listdir(ob101)
    classes = [i.lower() for i in folders]

    dOBJ101 = {'dataset' : [], 'filePath' : [], 'baseName' : [], 'label0' : []}

    for fi in folders:
        ## Get paths and extract base names
        file_paths = glob.glob(ob101 + fi + '/*.jpg')
        base_names = [os.path.basename(i) for i in file_paths]

        # extend labels to match length of the path list
        lab = [fi for i in range(len(file_paths))]

        dOBJ101['filePath'].extend(file_paths)
        dOBJ101['baseName'].extend(base_names)
        dOBJ101['label0'].extend(lab)

    dOBJ101['dataset'] = ['101_ObjectCategoreis'] * len(dOBJ101['filePath'])
    #dfOBJ101 = pd.DataFrame(dOBJ101)
    ## Not sure if a dict or a pd.DataFrame should be returned.

    return(dOBJ101)

def get_Cars(directory):
    cars = directory + "Cars/" 
    train_dir = cars + "cars_train/"
    test_dir = cars + "cars_train/"
    devkit_dir = cars + "devkit/"

    meta = loadmat(devkit_dir + "cars_meta.mat")
    class_sup_names = [meta['class_names'][0][i][0] for i in range(len(meta['class_names'][0]))]

    ##
    ## Here we could parse the class names into a hierarchy ....
    ##

    test_annotations = loadmat(cars + "cars_test_annos_withLabels.mat")
    train_annotations = loadmat(devkit_dir + "cars_train_annos.mat")

    testAnno = test_annotations['annotations'][0]
    trainAnno = train_annotations['annotations'][0]

    class_test = [testAnno[i][4][0][0] for i in range(len(testAnno))]
    class_train = [trainAnno[i][4][0][0] for i in range(len(trainAnno))]


    test_path = [test_dir + testAnno[i][5][0] for i in range(len(testAnno))]
    train_path = [train_dir + trainAnno[i][5][0] for i in range(len(trainAnno))]

    paths = train_path + test_path

    baseNames = [p.split('/')[-1] for p in paths]

    test_labels = [class_sup_names[i - 1] for i in class_test]
    train_labels = [class_sup_names[i - 1] for i in class_train]
    
    labels1 = train_labels + test_labels
    labels0 = [i.split(' ')[0] for i in labels1]

    subset = ['train'] * len(train_labels) + ['test'] * len(test_labels)

    dCars = {'dataset' : ['Cars'] * len(paths), 'filePath' : paths, 
            'baseName' : baseNames, 'label0' : labels0, 
            'label1' : labels1, 'subset' : subset}

    return(dCars)

def get_Flowers(directory):
   
    flower_dir = directory + '102Flowers/'
    
    paths = glob.glob(flower_dir + 'jpg/*.jpg')
    paths.sort()

    baseNames = [p.split('/')[-1] for p in paths]

    meta = loadmat(flower_dir + 'imagelabels.mat')
    splits = loadmat(flower_dir + 'setid.mat')

    labels = list(meta['labels'][0])

    name_dict = {}

    with open('102Flower_labels.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            name_dict[int(row[0])] = row[1]

    labels0 = [name_dict[i] for i in labels] 

    dFlowers = {'dataset' : ['102Flowers'] * len(paths), 'filePath' : paths, 
            'baseName' : baseNames, 'label0' : labels0}

    return(dFlowers)

def get_Pets(directory):
    pets_dir = directory + "Pets/" 
    anno_dir = pets_dir + "annotations/"

    train_anno = [] 
    test_anno = [] 

    with open(anno_dir + "trainval.txt", newline="") as f:
        reader = csv.reader(f, delimiter = " ")
        for row in reader:
            train_anno.append(row)

    with open(anno_dir + "test.txt", newline="") as f:
        reader = csv.reader(f, delimiter = " ")
        for row in reader:
            test_anno.append(row)

    test_base = [i[0] + ".jpg" for i in test_anno]
    train_base = [i[0] + ".jpg" for i in train_anno]
    
    baseNames = train_base + test_base

    test_paths = [pets_dir + "images/" + i[0] + ".jpg" for i in test_anno]
    train_paths = [pets_dir + "images/" + i[0] + ".jpg" for i in train_anno]

    paths = train_paths + test_paths

    spec = lambda y: 0 if y == 1 else 1

    test_label0 = [['cat', 'dog'][spec(y[2])] for y in test_anno]
    train_label0 = [['cat', 'dog'][spec(y[2])] for y in train_anno]

    label0 = train_label0 + test_label0

    ## Breed
    test_label1 = [i[3] for i in test_anno]
    train_label1 = [i[3] for i in train_anno]

    label1 = train_label1 + test_label1

    subset = ['train'] * len(train_anno) + ['test'] * len(test_anno)
    
    dPets = {'dataset' : ['Pets'] * len(paths), 'filePath' : paths, 'baseName' : baseNames, 'label0' :
            label0, 'lebel1' : label1, 'subset' : subset}

    return(dPets)
    ## END Pets

def get_SUN397(directory):

    sun397_dir = directory + 'SUN397/'

    paths = []
    baseNames = []
    labels0 = []

    pathList = []

    with open(sun397_dir + 'ClassName.txt') as f:
        for l in f.readlines():
            pathList.append(l.strip()[1::])

    for p in [sun397_dir + pa for pa in pathList]:
        tmp = glob.glob(p + '/*.jpg')
        lab = '_'.join(p.split('/')[4::])

        baseNames.extend([ti.split('/')[-1] for ti in tmp])
        paths.extend(tmp)
        labels0.extend([lab] * len(tmp))


    dSUN = {'dataset' : ['SUN397'] * len(paths), 'filePath' : paths, 'baseName' : baseNames, 'label0' : labels0}

    return(dSUN)
    ## END SUN397

def get_VOCdevkit(directory):
    di = directory + '/VOCdevkit/VOC2007/'

    labDir = di + '/ImageSets/Main/'
    jpgDir = di + '/JPEGImages/'

    paths = glob.glob(jpgDir + '*.jpg')
    baseNames = [p.split('/')[-1] for p in paths]
    keyNames = [b.split('.')[0] for b in baseNames]

    file_dict = {ki: {'dataset' : 'VOC', 'filePath' : p, 'baseName' :
        bi, 'labelL' : deque()} for ki,bi,p in
        zip(keyNames,baseNames,paths)}

    ## Get Training/Validation data
    trainValList = sorted(glob.glob(labDir + "/*_trainval.txt"))

    for x in trainValList:
        with open(x, 'r') as f:
            trainVal_rows = pd.read_csv(f,header=None)
            label = x.split('/')[-1].split('_trainval')[0]
            for index, row in trainVal_rows.iterrows():
                tmpKi = row[0].split(' ')[0] 
                tmp = row[0].split(' ')[-1]
                if tmp == '1': 
                    file_dict[tmpKi]['labelL'].appendleft(label)
                if tmp == '0':
                    file_dict[tmpKi]['labelL'].append(label)

    ## Add Testing data
    di = directory + '/VOCdevkit/VOC2007test/VOC2007'

    labDir = di + '/ImageSets/Main/'
    jpgDir = di + '/JPEGImages/'

    paths = glob.glob(jpgDir + '*.jpg')
    baseNames = [p.split('/')[-1] for p in paths]
    keyNames = [b.split('.')[0] for b in baseNames]


    ## Get Testin data
    for ki,bi,p in zip(keyNames, baseNames, paths):
        file_dict[ki] = {'filePath' : p, 'baseName' : bi, 'labelL' : deque()}


    testList = sorted(glob.glob(labDir + "/*_test.txt"))

    for x in testList:
        with open(x, 'r') as f:
            test_rows = pd.read_csv(f,header=None)
            label = x.split('/')[-1].split('_test')[0]
            for index, row in test_rows.iterrows():
                tmpKi = row[0].split(' ')[0] 
                tmp = row[0].split(' ')[-1]
                if tmp == '1': 
                    file_dict[tmpKi]['labelL'].appendleft(label)
                if tmp == '0':
                    file_dict[tmpKi]['labelL'].append(label)


    
### -1:
### Negative: The image contains no objects of the class of interest. A classifier should give a `negative' output.
### 1:
### Positive: The image contains at least one object of the class of interest. A classifier should give a `positive' output.
### 0:
### ``Difficult'': The image contains only objects of the class of interest marked as `difficult'. The output of the classifier for this image does not affect its evaluation.


    #Labels

    vocDat = pd.DataFrame(file_dict).transpose()

    labs = {ki : {'label0' : 'NaN', 'label1' : 'NaN', 'label2' : 'NaN',
        'label3' : 'NaN', 'label4' : 'NaN', 'label5' : 'NaN', 'label6' :
        'NaN'} for ki in file_dict.keys()}
    
    Xl = lambda x: ['label0','label1','label2','label3','label4','label5',
            'label6'][x]

    for index, row in vocDat.iterrows():
        l0 = vocDat.loc[row.name]['labelL']

        for i in range(len(l0)):
            labs[row.name][Xl(i)] = vocDat.loc[row.name]['labelL'][i]


    lpd = pd.DataFrame(labs).transpose()
    out = pd.concat([vocDat, lpd], axis = 1)

    pdVOC = out.drop(['labelL'], axis = 1)
    pdVOC['dataset'] = ["VOC"] * pdVOC.shape[0]

    dVOC = pdVOC.to_dict()

    return(dVOC)

def get_birdsnap(directory):
    bird_dir = directory + 'birdsnap/download/images/' 

    classes = os.listdir(bird_dir)
    classes.sort()
    classes

    paths = []
    baseNames = []
    labels0 = []
    

    for ci in classes:
        tmp = glob.glob(bird_dir + ci + "/*.jpg")
        paths.extend(tmp)
        baseNames.extend([b.split('/')[5] for b in tmp])
        labels0.extend([ci] * len(tmp))
        
    dBird = {'dataset' : ['birdsnap'] * len(paths), 'filePath' : paths, 'baseName' : baseNames, 'label0' : labels0}

    return(dBird)

def get_dtd(directory):
    dtd_dir = directory + "dtd/" 

    paths = []
    baseNames = []
    labels0 = []
    labels1 = []
    labels2 = []
    labels3 = []

    with open(dtd_dir + "labels/labels_joint_anno.txt") as f:
        for line in f:
            row = line.strip().split(' ')

            paths.append(dtd_dir + row[0])
            baseNames.append(row[0].split('/')[-1])
            labels0.append(row[1])
            if len(row) > 2:
                labels1.append(row[1])
            else: 
                labels1.append("NaN")

            if len(row) > 3:
                labels2.append(row[2])
            else: 
                labels2.append("NaN")

            if len(row) > 4:
                labels3.append(row[3])
            else: 
                labels3.append("NaN")

    dDTD = {'dataset' : ['dtd'] * len(paths), 'filePath' : paths, 
            'baseName' : baseNames, 'label0' : labels0, 
            'label1' : labels1, 'label2' : labels2, 'label3' : labels3}

    return(dDTD)

def get_fgvc(directory):
    fgvc_dir = directory + 'FGVC/fgvc-aircraft-2013b/'
    data_dir = fgvc_dir + 'data/'
    image_dir = fgvc_dir + 'data/images/'

    image_dict = {i.split('.')[0] : {'baseName' : i} for i in os.listdir(image_dir)}

    train_list = ['images_variant_train.txt', 'images_family_train.txt', 'images_manufacturer_train.txt']

    test_list = ['images_variant_test.txt', 'images_family_test.txt', 'images_manufacturer_test.txt']

    with open(data_dir + 'images_variant_train.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['variant'] = row[1]
        
    with open(data_dir + 'images_variant_test.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['variant'] = row[1]

    with open(data_dir + 'images_variant_trainval.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['variant'] = row[1]
        
    with open(data_dir + 'images_variant_val.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['variant'] = row[1]
        
    with open(data_dir + 'images_family_train.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['family'] = row[1]
        
    with open(data_dir + 'images_family_test.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['family'] = row[1]

    with open(data_dir + 'images_family_trainval.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['family'] = row[1]
        
    with open(data_dir + 'images_family_val.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['family'] = row[1]
        
    with open(data_dir + 'images_manufacturer_train.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['manufacturer'] = row[1]
        
    with open(data_dir + 'images_manufacturer_test.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['manufacturer'] = row[1]

    with open(data_dir + 'images_manufacturer_trainval.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['manufacturer'] = row[1]
        
    with open(data_dir + 'images_manufacturer_val.txt') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            image_dict[row[0]]['manufacturer'] = row[1]

    paths = []
    baseNames = []
    labels0 = []
    labels1 = []
    labels2 = []

    for key in image_dict:
       paths.append(image_dir + image_dict[key]['baseName'])
       baseNames.append(image_dict[key]['baseName'])
       labels0.append(image_dict[key]['variant'])
       labels1.append(image_dict[key]['family'])
       labels2.append(image_dict[key]['manufacturer'])


    dFGVC = {'dataset' : ['fgvc'] * len(paths), 'filePath' : paths, 
            'baseName' : baseNames, 'label0' : labels0, 
            'label1' : labels1, 'label2' : labels2}

    return(dFGVC)

def get_food101(directory):
    food_dir = directory + "food-101/images/" 
    classes = os.listdir(food_dir)
    classes.sort()

    paths = []
    baseNames = []
    labels0 = []
    

    for ci in classes:
        tmp = glob.glob(food_dir + ci + "/*.jpg")
        paths.extend(tmp)
        baseNames.extend([b.split('/')[5] for b in tmp])
        labels0.extend([ci] * len(tmp))
        
    dFood = {'dataset' : ['food101'] * len(paths), 'filePath' : paths, 'baseName' : baseNames, 'label0' : labels0}

    return(dFood)


def mergeAll():

    return(0)

def main(directory):

    datasets = [
            pd.DataFrame(get_Object101(directory)),
            pd.DataFrame(get_fgvc(directory)),
            pd.DataFrame(get_food101(directory)),
            pd.DataFrame(get_Cars(directory)),
            pd.DataFrame(get_SUN397(directory)),
            pd.DataFrame(get_dtd(directory)),
            pd.DataFrame(get_Flowers(directory)),
            pd.DataFrame(get_birdsnap(directory)),
            pd.DataFrame(get_VOCdevkit(directory)),
            ]
    
    return(datasets)


    
if __name__ == "__main__":

    wd = os.getcwd()
    directory = "../datasets_resized_wLabels/"
    #datasets = main(directory)

    #A = pd.concat(datasets)
    A = pd.DataFrame(get_birdsnap(directory))
    B = pd.DataFrame(get_VOCdevkit(directory))

    




