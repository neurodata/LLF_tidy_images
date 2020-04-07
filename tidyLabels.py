#!/usr/bin/env python
from PIL import Image
from PIL import ImageOps
from math import floor, sqrt
from scipy.io import loadmat
import csv
import glob
import os
import argparse
import configparser
import pandas as pd


## The spec
## dictionary = {"dataset" : dataset = [{'filename':filename, 'label':label]}


def Object101(directory):
   
    ob101 = directory + "101_ObjectCategories/" 
    folders = os.listdir(ob101)
    classes = [i.lower() for i in folders]

    dOBJ101 = {'filePath' : [], 'baseName' : [], 'label0' : []}

    for fi in folders:
        ## Get paths and extract base names
        file_paths = glob.glob(ob101 + fi + '/*.jpg')
        base_names = [os.path.basename(i) for i in file_paths]

        # extend labels to match length of the path list
        lab = [fi for i in range(len(file_paths))]

        dOBJ101['filePath'].extend(file_paths)
        dOBJ101['baseName'].extend(base_names)
        dOBJ101['label0'].extend(lab)

    #dfOBJ101 = pd.DataFrame(dOBJ101)
    ## Not sure if a dict or a pd.DataFrame should be returned.
    return(dOBJ101)

def Cars(directory):
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

    dCars = {'filePath' : paths, 'baseName' : baseNames, 
             'label0' : labels0, 'labels1' : labels1, 'subset' : subset}

    return(dCars)

def Flowers(directory):
    
    return(0)

def Pets(directory):
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
    
    dPets = {'filePath' : paths, 'baseName' : baseNames, 'label0' :
            label0, 'lebel1' : label1, 'subset' : subset}

    return(dPets)
    ## END Pets

def SUN397(directory):

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


    dSUN = {'filePath' : paths, 'baseName' : baseNames, 'label0' : labels0}

    return(dSUN)
    ## END SUN397

def VOCdevkit():
    di = x + "/VOCdevkit/VOC2007/"
    labDir = di + "/ImageSets/Main/"

    for x in glob.glob(labDir + "/*_train.txt"):
        print(x)

    for x in glob.glob(labDir + "/*_val.txt"):
        print(x)

    return(0)

def birdsnap():

    return(0)

def dtd():

    return(0)

def fgvc():

    return(0)

def food101():
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
        

    dFood = {'filePath' : paths, 'baseName' : baseNames, 'label0' : labels0}

    return(dFood)


def mergeAll():

    return(0)

def main(directory):
    obj = Object101(directory)
    return(0)


    
if __name__ == "__main__":

    directory = "../datasets_resized_wLabels/"

    main(directory)
    






