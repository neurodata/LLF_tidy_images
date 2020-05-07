# LLF_tidy_images

We assume that the below datasets have been downloaded to `../datasets/` relative
to the root of this git repository and stored in individual folders
appropriately named.

## Datasets


| Dataset Name | Source | Classes |
|:-------------|:-------|:--------|
| Food-101 | [Link](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/) | 101 |
| CIFAR-10     | [Link](https://www.cs.toronto.edu/~kriz/cifar.html) | 10 | 
| CIFAR-100    | [Link](https://www.cs.toronto.edu/~kriz/cifar.html) | 100 |
| BirdSnap     | [Link](http://thomasberg.org)  | 500 | 
| SUN397 | [Link](https://vision.princeton.edu/projects/2010/SUN/) | 397 | 
| Stanford Cars| [Link](http://ai.stanford.edu/~jkrause/cars/car_dataset.html) | 196 |
| FGVC Aircraft| [Link](https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/) | 100 |
| PASCAL VOC 2007 | [Link](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/) | 20 |
| DTD | [Link](http://www.robots.ox.ac.uk/~vgg/data/dtd/) | 47 | 
| Pets | [Link](http://www.robots.ox.ac.uk/~vgg/data/pets/) | 37 |
| Caltech-101 | [Link](http://www.vision.caltech.edu/Image_Datasets/Caltech101/Caltech101.html) | 101
| Flowers | [Link](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html) | 102 |



The total number of images should be 312,252


| Dataset Name  | train|  test| classes| Labels |
|:--------------|-----:|-----:|-------:|-------:|
|birdsnap       | 47386|  2443| 500    | All    |
|cifar10        | 50000| 10000| 10     | All    |
|cifar100       | 50000| 10000| 100    | All    |
|DTD            |  3760|  1880| 47     | All    |
|FGVC_Aircraft  |  6667|  3333| 100    | All    |
|flowers        |  2040|  6149| 102    | All    |
|stanford-cars  |  8144|  8041| 196    | All    |
|Oxford_Pets    |  3680|  3369| 37     | All    |
|food-101       | 75750| 25250| 101    | All    |
|PASCAL_VOC2007 |  5011|  4952| 20     | All    |
|Caltech-101    |  3060|  6084| 102    | All    |
|SUN397         | 19850| 19850| 397    | ALL    |


# Downloading

The links to all of the datasets are save in the `download.sh` script
which sets up the proper folders and downloads and unpacks the datasets.

Run with `sh download.sh`


# Image Pre-processing

See [preprocessing.md](./preprocessing.md)


# Output labels

Then to create the csv file that holds all of the file paths and labels
for all of the images across all of the datasets run

```
python3 tidyLabels.py
```




---
