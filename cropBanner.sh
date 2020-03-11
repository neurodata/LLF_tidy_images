#!/usr/bin/env bash

find ../datasets -regex ".*\(jpg\)" -execdir convert {} -gravity South -crop +0+20 +repage {} \;
