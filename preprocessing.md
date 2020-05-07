# Preprocessing steps per dataset

Some of the preprocessing requires
[ImageMagick](https://imagemagick.org/index.php) and python including tensorFlow (non GPU is ok).

## FGVC_Aircraft

- http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft
- The bottom of each image has a banner 20 pixels high. This is to be cropped.

## [cropBanner.sh](./cropBanner.sh)

```
sh cropBanner.sh
```


# Padding 
## [padding.py](./padding.py) 

The images need to be padded as they do not all have the same aspect
ratio. We find the maximum of (height,width) and pad the shorter side
from both sides.  This can be done via the following:

```
sh pad.sh
```


# Resizing
## [resize.sh](./resize.sh)

After padding to square we resize to match the smallest dimensions of
the datasets (CIFAR = 32x32) using `tensorflow.image.resize` which
defaults to `bilinear` interpolation.

```
sh resize.sh
```


---

