import sys
import platform
import re
import os
from os.path import abspath, join, dirname, basename, expanduser, exists
from os.path import isdir, splitext
import json
import shutil
from glob import glob
from datetime import datetime, timedelta
from functools import partial
import vim

img_filetype = ['jpg', 'jpeg', 'bmp', 'png', 'JPG', 'JPEG', 'BMP', 'PNG']
img_dir_patterns = ['img', 'media']

def GuessImgDir(filepath):
    if not isdir(filepath):
        dir_path = dirname(filepath)
    else:
        dir_path = filepath

    child_dir = list(filter(isdir, os.listdir(dir_path)))

    def suspicious(bigstr):
        has = False
        for patt in img_dir_patterns:
            if has:
                break
            if patt.lower() in bigstr.lower():
                has = True
        return has

    candicate_dir = list(filter(suspicious, child_dir))
    candicate_dir.sort(key=ImgCount, reverse=True)

    if len(candicate_dir) == 0:
        ans = None
    else:
        ans = candicate_dir[0]

    return (ans, candicate_dir)   


def ImgCount(rscpath, filetype=1):
    '''
        filetype == 0 : file    
        filetype == 1 : folder   
    '''

    if filetype == 0:
        name, ext = splitext(basename(rscpath))
        ext = ext[1:]
        return 1 if ext in img_filetype else 0
    else:
        return sum(map(partial(ImgCount, filetype=0), os.listdir(rscpath)))

def MostSuspicious(filepath):
    ans = GuessImgDir(filepath)[0]

    if ans is not None:
        return ans
    else:
        return 'img'

def SetSelectedAs():
    current_buf = vim.current.buffer
    cur_buf_path = current_buf.name
    ans = basename(MostSuspicious(cur_buf_path))
    vim.command(r"let g:mdip_imgdir = '%s'" % ans)   
    vim.command(r"echohl Question | echo 'ImgDir switched to %s automatically!' | echohl None" % vim.eval("g:mdip_imgdir"))
    
#    print('ImgDir switched to %s automatically!' % ans)



