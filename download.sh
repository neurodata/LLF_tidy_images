#!/usr/env bash

if false; then
# Setup
	WRKDIR="$PWD"
	mkdir ../compressed
	mkdir ../datasets_ORIGINAL
	mkdir ../datasets_cropped
	mkdir ../datasets_padded
	mkdir ../datasets_resized
	mkdir ../datasets_resized_wLabels


#Download
	cd ../compressed

## 101_ObjectCategories CalTech
	wget http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz

## Cars: http://host.robots.ox.ac.uk/pascal/VOC/voc2007/
	# train/val data
	wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
	
	# devkit with training labels
	wget http://ai.stanford.edu/~jkrause/cars/car_devkit.tgz
	#tar -xzf car_devkit.tgz

	# test labels
	wget http://imagenet.stanford.edu/internal/car196/cars_test_annos_withlabels.mat

## 102-Flowers
	mkdir 102Flowers; cd 102Flowers
	wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz
	wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat

fi

