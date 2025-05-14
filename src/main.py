import os
import sys
import shutil

from copystatic import copy_files_recursive
from generate import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
from_path = "content/index.md"
dest_path = "docs/index.html"
template_path = "./template.html"
dir_path_content = "./content"
dest_dir_path = "./docs"


def main():
    try:
        basepath = sys.argv[1]
    except IndexError:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath,
    )


main()
