#!/usr/bin/env bash

find ../datasets -type f -regex ".*\(jpg\)" | xargs -P 12 -L 1 ./padding.py
