#!/usr/bin/env python
from PIL import Image
from PIL import ImageOps
from math import floor, sqrt
import argparse
import configparser

parser = argparse.ArgumentParser(description="Pad to square.")

parser.add_argument("image_path", metavar="P", type=str, nargs=1, 
                    help="The input file path.")

args = parser.parse_args()
inFile = args.image_path[0]


def main(inFile):
    im = Image.open(inFile)
    
    w = im.size[0]
    h = im.size[1]
    
    M = max(h,w)
    
    out = ImageOps.pad(im, (M,M))

    out.save(inFile, 'jpeg')


if __name__ == "__main__":

    main(inFile)
    
    




