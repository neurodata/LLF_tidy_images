#!/usr/env bash

## ImageMagick is required along with tensorflow

## Resize all the jpg's to be 32x32
find ../datasets -type f -regex ".*\(jpg\)" | xargs -P 12 -L 1 ./resize.py

echo "Done with resizing.\n"
echo "Checking sizes...\n"

## check
find ../datasets_tmp -type f -regex ".*\(jpg\)" -exec identify {} \; | awk '{print $1,$3}' > ../check_image_sizes.dat
