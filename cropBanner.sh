#!/usr/bin/env bash

find ../datasets_cropped/fgvc-aircraft-2013b -type f -regex ".*\(jpg\)" -execdir convert {} -gravity South -crop +0+20 +repage {} \;
