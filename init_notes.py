import os
from shutil import copyfile
import argparse

# Some constants and defaults
HOME_FOLDER = os.path.expanduser('~')
DEFAULT_BASE_FOLDER = os.path.join(HOME_FOLDER, 'Documents', 'TexNotes') 
TEMPLATE_FILE_NAME = 'template.tex'

parser = argparse.ArgumentParser(description="Latex Notes projects initializer")

parser.add_argument("projName", help="The name of the project to create the files and folders for it")
parser.add_argument("--d", help="Base directory where to create the folder structure")
parser.add_argument("--i", help="Intermediate directories to create after the base folder")

args = parser.parse_args()

if args.d:
    base_folder = args.d
else:
    base_folder = DEFAULT_BASE_FOLDER

print(base_folder)

if args.i:
    base_folder = os.path.join(base_folder, args.i)

# Creating folder structure
base_path = os.path.join(base_folder, args.projName)
print(base_path)

if not os.path.exists(base_path):
    os.mkdir(base_path)

# Creating additional directories
img_path = os.path.join(base_path, 'img')
if not os.path.exists(img_path):
    os.mkdir(img_path)

# Copying Latex initial template
tex_fname = args.projName.replace(' ', '_') + '.tex'
tex_filepath = os.path.join(base_path, tex_fname)
if not os.path.exists(tex_filepath):
    copyfile(TEMPLATE_FILE_NAME, tex_filepath)

