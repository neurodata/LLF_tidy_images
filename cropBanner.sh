#!/usr/bin/env bash

find ../datasets_cropped/fgvc-aircraft-2013b -type f -regex ".*\(jpg\)" -execdir convert {} -gravity South -crop +0+20 +repage {} \;

convert ../datasets_cropped/birdsnap/download/images/Mourning_Dove/181010.jpg -gravity South -crop +0+20 +repage ../datasets_cropped/birdsnap/download/images/Mourning_Dove/181010.jpg
