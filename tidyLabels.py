#!/usr/bin/env python
from PIL import Image
from PIL import ImageOps
from math import floor, sqrt
from scipy.io import loadmat
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
    
    labels = train_labels + test_labels

    subset = ['train'] * len(train_labels) + ['test'] * len(test_labels)

    dCars = {'filePath' : paths, 'baseName' : baseNames, 'label0' : labels, 'subset' : subset}

    return(dCars)

def Flowers():

    return(0)

def Pets():

    return(0)

def SUN397():

    return(0)

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

    return(0)




def main(directory):
    obj = Object101(directory)
    return(0)


    
if __name__ == "__main__":

    directory = "../datasets_resized_wLabels/"

    main(directory)
    






