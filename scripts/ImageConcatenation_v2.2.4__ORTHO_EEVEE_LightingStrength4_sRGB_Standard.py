# -*- coding: utf-8 -*-
"""
Author:     Tobias Ried, 2021
"""

import os
from PIL import Image

print('START')

#################################################################################
# initial settings
#################################################################################
# file paths
rendered_normal_images = r'D:/data/rendered_images/ORTHO/Normals_CYCLES_None_XYZ/'
rendered_texture_images = r'D:/data/rendered_images/ORTHO/Textures_EEVEE_LightingStrength4_sRGB_Standard/'
merged_images = r'D:/data/merged_images/ORTHO_EEVEE_LightingStrength4_sRGB_Standard/'



#################################################################################
# load image files from directory and create two lists (texture/normal)
#################################################################################
files_normal = os.listdir(rendered_normal_images)
files_texture = os.listdir(rendered_texture_images)

zipped_t_n = zip(files_texture, files_normal)
zipped_t_n_list = list(zipped_t_n)



#################################################################################
# concatenate the texture/normal images
#################################################################################
# read the images
for t, n in zipped_t_n_list:
    left_image = Image.open(rendered_texture_images + str(t))
    right_image = Image.open(rendered_normal_images + str(n))

    # concatenate images
    left_image_size = left_image.size
    right_image_size = right_image.size
    new_image = Image.new('RGBA',(2*left_image_size[0], left_image_size[1]), (250,250,250))
    new_image.paste(left_image,(0,0))
    new_image.paste(right_image,(left_image_size[0],0))
    new_image.save(merged_images + 'merged_' + str(n), 'PNG', compress_level=0)    # default: compress_level=6

print('FINISHED')