# -*- coding: utf-8 -*-
"""
Author:     Tobias Ried, 2021
"""

import os
import glob
import re
from PIL import Image

print('START')

#################################################################################
# initial settings
#################################################################################
# file paths
rendered_images = r'd:/data/rendered_images/'
merged_images = r'd:/data/merged_images/'



#################################################################################
# load image files from directory and create two lists (texture/normal)
#################################################################################
files = os.listdir(rendered_images)

files_texture = []
files_normal = []

for filename in files:
    # regular expression filtering
    pattern_texture = r'^[0-9]{12}[_][t]'
    pattern_normal = r'^[0-9]{12}[_][n]'
    if re.match(pattern_texture, filename):
        match_texture = re.match(pattern_texture, filename)
        files_texture.append(filename)

    if re.match(pattern_normal, filename):
        match_normal = re.match(pattern_normal, filename)    
        files_normal.append(filename)

zipped_t_n = zip(files_texture, files_normal)
zipped_t_n_list = list(zipped_t_n)



#################################################################################
# concatenate the texture/normal images
#################################################################################
# read the images
for t, n in zipped_t_n_list:
    left_image = Image.open(r'D:/data/rendered_images/' + str(t))
    right_image = Image.open(r'D:/data/rendered_images/' + str(n))

    # concatenate images
    left_image_size = left_image.size
    right_image_size = right_image.size
    new_image = Image.new('RGBA',(2*left_image_size[0], left_image_size[1]), (250,250,250))
    new_image.paste(left_image,(0,0))
    new_image.paste(right_image,(left_image_size[0],0))
    new_image.save(r'D:/data/merged_images/merged_' + str(t), 'PNG', compress_level=0)    # default: compress_level=6

print('FINISHED')