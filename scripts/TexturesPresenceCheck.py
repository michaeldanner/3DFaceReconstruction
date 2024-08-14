# -*- coding: utf-8 -*-
"""
Author:     Tobias Ried, 2021
"""

import os
import glob
import shutil

print('START')

folder_loc = r'D:/data/headspaceOnline/subjects/'
target_loc = r'D:/data/headspaceOnline/subjects_excluded/no_textures/'

for folder in os.listdir(folder_loc):
    if not glob.glob(os.path.join(folder_loc + folder + r'/*.bmp')):
        shutil.move(folder_loc + folder, target_loc + folder)

print('FINISHED')