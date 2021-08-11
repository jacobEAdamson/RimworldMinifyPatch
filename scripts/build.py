#!/usr/bin/env python

import shutil
import os

current_path = os.getcwd()
dist_path = os.path.join(current_path, 'dist')

if os.path.exists(dist_path):
  shutil.rmtree(dist_path)
os.mkdir(dist_path)

shutil.copytree(os.path.join(current_path, "About"), os.path.join(dist_path, "About"))
shutil.copytree(os.path.join(current_path, "Defs"), os.path.join(dist_path, "Defs"))
shutil.copytree(os.path.join(current_path, "Patches"), os.path.join(dist_path, "Patches"))
print(f'Built at {dist_path}')
