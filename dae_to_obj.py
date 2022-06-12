import sys
import os
import glob
import pymeshlab

dae_files_dir = os.path.abspath(os.path.join(os.getcwd(), sys.argv[1])) 
print('Input .dae files dir: ', dae_files_dir)
dae_files = glob.glob(dae_files_dir+'/*.dae', recursive=True)
print('Input .dae files: ', dae_files)

for dae_file in dae_files:
    obj_file = dae_file.replace('dae', 'obj')
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(dae_file)
    ms.save_current_mesh(obj_file)
