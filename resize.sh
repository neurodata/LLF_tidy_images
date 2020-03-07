#!/usr/env bash

## ImageMagick is required

## test
##find ./ -regex ".*\(jpg\)" -execdir file {}\;


## Resize all the jpg's to be 32x32 (forced)
#find ../big12/ -regex ".*\(jpg\)" -exec echo {} \; -execdir convert {} -resize 32x32! {} \;

echo "Done with resizing\n"
echo "Checking sizes\n"

## check
find ../big12/ -regex ".*\(jpg\)" -exec identify {} \; | awk '{print $1,$3}' > ../check_image_sizes.dat

find ../big12/ -regex ".*\(jpg\)" -print0 | xargs -P 12 -0 identify | awk '{print $1,$3}' | sed "s/ /,/" > ../check_image_sizes.csv

