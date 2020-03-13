#!/usr/bin/env python
from PIL import Image
from PIL import ImageOps
from math import floor, sqrt
import argparse
import configparser
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

parser = argparse.ArgumentParser(description="Pad to square.")

parser.add_argument("image_path", metavar="P", type=str, nargs=1, 
                    help="The input file path.")

args = parser.parse_args()
inFile = args.image_path[0]


def main(inFile):
    
    img0 = tf.io.read_file(inFile)
    img1 = tf.io.decode_jpeg(img0, channels=3)

    img2 = tf.image.resize(img1, [32,32], method='bilinear', preserve_aspect_ratio=True)

    img3 = tf.image.convert_image_dtype(img2/255.0, dtype=tf.uint8)

    out = tf.io.encode_jpeg(img3, format='', quality=100)

    tf.io.write_file(inFile, out)


if __name__ == "__main__":

    main(inFile)

