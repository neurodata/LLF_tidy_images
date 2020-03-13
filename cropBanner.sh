#!/usr/bin/env bash

find ../datasets/fgvc-aircraft-2013b -type f -regex ".*\(jpg\)" -execdir convert {} -gravity South -crop +0+20 +repage {} \;
