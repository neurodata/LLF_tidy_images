# Preprocessing steps per dataset

## FGVC_Aircraft

- http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft
- The bottom of each image has a banner 20 pixels high. This is to be cropped.

```
find ./ -regex ".*\(jpg\)" -execdir convert {} -gravity South -crop +0+20 +repage {} \;
```


# Padding 

The images need to be padded as they do not all have the same aspect
ratio. Using a helper [python script](./padding.py) we find the maximum of
(height,width) and pad the shorter side from both sides.
This can be done via the following:

```
find ../datasets -regex ".*\(jpg\)" -exec ./padding.py {} \;
```

# Resizing 

After padding to square we resize to match the smallest dimensions of
the datasets (CIFAR = 32x32) using `ImageMagick`.

```
sh resize.sh
```
