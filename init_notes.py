import os
import argparse
from string import Template

# Some constants and defaults
HOME_FOLDER = os.path.expanduser('~')
DEFAULT_BASE_FOLDER = os.path.join(HOME_FOLDER, 'Dropbox', 'TexNotes') 
TEMPLATE_FILE_NAME = 'template.tex'

def read_template(path):
    with open(path, 'r') as f:
        template = f.read()
    return Template(template)

parser = argparse.ArgumentParser(description="Latex Notes projects initializer")

parser.add_argument("projName", help="The name of the project to create the files and folders for it")
parser.add_argument("--d", help="Base directory where to create the folder structure")
parser.add_argument("--i", nargs='+', help="Intermediate directories to create after the base folder")

args = parser.parse_args()

if args.d:
    base_folder = args.d
else:
    base_folder = DEFAULT_BASE_FOLDER

if args.i:
    dirs = args.i
    if type(args.i) != list:
        dirs = [args.i]
    for d in dirs:
        base_folder = os.path.join(base_folder, d)
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

# Creating folder structure
base_path = os.path.join(base_folder, args.projName)

if not os.path.exists(base_path):
    os.mkdir(base_path)

# Creating additional directories
img_path = os.path.join(base_path, 'img')
if not os.path.exists(img_path):
    os.mkdir(img_path)

# Copying Latex initial template
tex_fname = args.projName.replace(' ', '_').lower() + '.tex'
tex_filepath = os.path.join(base_path, tex_fname)
if not os.path.exists(tex_filepath):
    template = read_template(TEMPLATE_FILE_NAME)
    print(template)
    print(template.substitute(TITLE=args.projName))
    with open(tex_filepath, 'w') as f:
        f.write(template.substitute(TITLE=args.projName))

