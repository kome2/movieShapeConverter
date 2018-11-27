#!/usr/bin/env python
#! -*- coding: utf-8

import cv2
import numpy as np
import sys
from PIL import Image
from argparse import ArgumentParser
import os
import configparser as config
from tqdm import tqdm

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('input', type=str, help='path to input movie')
    argparser.add_argument('resolution', type=str, help='resolution of converted movie')
    argparser.add_argument('config', type=str, help='path to config file')
    argparser.add_argument('-o', '--output', type=str, help='filename of output movie')
    args = argparser.parse_args()
    return args

def homoPool(conf):
    lst = config.ConfigParser()
    lst.read(configFile)
    
    pts1 = np.empty((0, 2))
    pts2 = np.empty((0, 2))
    for i in range(1, 5):
        src = 'src' + str(i)
        dst = 'dest' + str(i)
        srcAr = [int(x) for x in lst['number'][src].split()]
        dstAr = [int(x) for x in lst['number'][dst].split()]
        pts1 = np.append(pts1, np.array([srcAr]), axis=0)
        pts2 = np.append(pts2, np.array([dstAr]), axis=0)
    
    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)

    M = cv2.getPerspectiveTransform(pts1, pts2)
    
    return M

def trackSwimmerImgs(M, inputFile, resolution, op):
    if not os.path.exists(inputFile):
        print("error", inputFile, "does noe exist", file=sys.stderr)
        exit()
    fName = str(os.path.splitext(os.path.basename(inputFile))[0])+ "_converted.mp4"
    outputFile = op or fName

    cap = cv2.VideoCapture(inputFile)
    totalFrame = int(cap.get(7))
    frameRate = round(cap.get(5))
    
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(outputFile, fourcc, frameRate, (resolution[0], resolution[1]))

    print("Source File:", inputFile)
    print("Output File:", outputFile)

    print("convertion started")
    with tqdm(total=totalFrame) as pbar:
        while(cap.isOpened()):
            pbar.update(1)
            ret, frame = cap.read()
            try:
                res = cv2.warpPerspective(frame, M, (resolution[0], resolution[1]))
            except cv2.error:
                break
            video.write(res)

    print("convertion completed")
    video.release()

if __name__ == '__main__':
    args = get_option()

    inputFile = args.input
    resolution = [int(x) for x in args.resolution.split('x')]
    configFile = args.config
    outputFile = args.output

    M = homoPool(configFile)
    trackSwimmerImgs(M, inputFile, resolution, outputFile)
