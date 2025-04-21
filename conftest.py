import os
import sys

file = os.path.abspath(__file__)
dir = os.path.dirname(file)
src_dir_path = os.path.join(dir, 'src')
sys.path.append(src_dir_path)