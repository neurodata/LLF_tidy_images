#!/usr/env bash

WORKDIR="$PWD"
if true; then
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


if true; then
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

  ## PASCAL VOC
  cd $OG;
  mkdir VOC2007; cd VOC2007; VOC=$PWD
  mkdir VOCtest;

  ## trainval data
  wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
  tar -xf VOCtrainval_06-Nov-2007.tar

  ## annotated test data
  wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
  tar -xf VOCtest_06-Nov-2007.tar -C VOCtest


  ## DTD
  cd $OG; #mkdir DTD; cd DTD; DTD=$PWD
  wget http://www.robots.ox.ac.uk/~vgg/data/dtd/download/dtd-r1.0.1.tar.gz
  tar -xzf dtd-r1.0.1.tar.gz


  ## PETS
  cd $OG; mkdir Pets; cd Pets; PETS=$PWD
  wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
  wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz

  ## Food-101
  cd $OG; 
  wget http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz
  tar -xzf food-101.tar.gz

  ## CIFAR-10
  cd $OG;
  wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
  tar -xzf cifar-10-python.tar.gz

  ## CIFAR-100
  cd $OG;
  wget https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz
  tar -xzf cifar-100-python.tar.gz

  ## Birdsnap
  cd $OG
  wget http://thomasberg.org/datasets/birdsnap/1.1/birdsnap.tgz
  tar -xzf birdsnap.tgz
  cd birdsnap;
  ## Should be python2
  python get_birdsnap.py

  fi 

## CLEANING
if true; then
  find $OG -regex ".*\(tgz\|tar.gz\|tar\)" -exec mv {} ../compressed/ ;
fi











