import sys
import platform
import re
import os
from os.path import abspath, join, dirname, basename, expanduser, exists
from os.path import isdir
import json
import shutil
from glob import glob
from datetime import datetime, timedelta

img_filetype = ['jpg', 'jpeg', 'bmp', 'png', 'JPG', 'JPEG', 'BMP', 'PNG']
img_dir_patterns = ['img', 'media']

def GuessImgDir(filepath):
    dir_path = dirname(filepath)
    child_dir = list(filter(isdir, os.listdir(dir_path)))












