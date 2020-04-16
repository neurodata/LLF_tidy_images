#!/usr/env bash

WORKDIR="$PWD"
if false; then
# Setup
	#mkdir ../compressed
	mkdir ../datasets_ORIGINAL
	mkdir ../datasets_cropped
	mkdir ../datasets_padded
	mkdir ../datasets_resized
	mkdir ../datasets_resized_wLabels

fi

#Download
	cd ../datasets_ORIGINAL
	OG="$PWD"


## Cars: http://host.robots.ox.ac.uk/pascal/VOC/voc2007/

  if false; then
## 101_ObjectCategories CalTech
  cd $OG
  wget http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz

  tar -xzf 101_ObjectCategories.tar.gz

  cd $OG
	mkdir Cars; cd Cars; CARS="$PWD"
	# train/val data
  wget http://imagenet.stanford.edu/internal/car196/cars_train.tgz
  # test data
  wget http://imagenet.stanford.edu/internal/car196/cars_test.tgz

	tar -xzf cars_train.tgz
	tar -xzf cars_test.tgz
	
	# devkit with training labels
	wget http://ai.stanford.edu/~jkrause/cars/car_devkit.tgz
	tar -xzf car_devkit.tgz

	# test labels
	wget http://imagenet.stanford.edu/internal/car196/cars_test_annos_withlabels.mat

  
## 102-Flowers
  cd $OG
	mkdir 102Flowers; cd 102Flowers
  FLOWERS=$PWD
	wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz
	wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat
  wget http://www.robots.ox.ac.uk/~vgg/data/flowers/102/setid.mat
  cp $WORKDIR/102Flower_labels.csv $FLOWERS/

  tar -xzf 102flowers.tgz

## SUN397
  cd $OG
	mkdir SUN397; cd SUN397;
	wget http://vision.princeton.edu/projects/2010/SUN/SUN397.tar.gz
	wget https://vision.princeton.edu/projects/2010/SUN/download/Partitions.zip 

  tar -xzf SUN397.tar.gz
  mkdir Partitions
  unzip Partitions.zip -d Partitions

## FGVC (Aircraft)
  cd $OG
  mkdir FGVC; cd FGCV;
  wget https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/archives/fgvc-aircraft-2013b.tar.gz

  tar -xzf fgvc-aircraft-2013b.tar.gz

  fi 






## CLEANING
#if false; then
#  #  find $OG -regex ".*\(tgz\|tar.gz\)" -exec mv {} ../compressed/ ;
#fi











