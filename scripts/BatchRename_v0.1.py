# -*- coding: utf-8 -*-
"""
Author:     Tobias Ried, 2021
"""

import os
import glob
import re

print('START')

#################################################################################
# initial settings
#################################################################################
# file paths
rename_input_directory = r'D:/data/rendered_images/PERSP/Textures_EEVEE_LightingStrength4_None_XYZ/'
rename_output_directory = r'D:/data/rendered_images/PERSP/Textures_EEVEE_LightingStrength4_None_XYZ/'



#################################################################################
# batch renaming
#################################################################################
files = os.listdir(rename_input_directory)

for filename in files:
    filename_crop = filename[:-22] + '.png'
    os.rename(rename_input_directory + filename, rename_output_directory + filename_crop)

print('FINISHED')