import os
import sys
import shutil

from copystatic import copy_files_recursive
from generate import generate_pages_recursive


dir_path_static = "static"
dir_path_public = "docs"
from_path = "content/index.md"
dest_path = "docs/index.html"
template_path = "template.html"
dir_path_content = "content"
dest_dir_path = "docs"


def main():
    try:
        basepath = sys.argv[1]
    except IndexError:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(f".{basepath}{dir_path_public}"):
        shutil.rmtree(f".{basepath}{dir_path_public}")

    print("Copying static files to public directory...")
    copy_files_recursive(
        f".{basepath}{dir_path_static}", f".{basepath}{dir_path_public}"
    )

    generate_pages_recursive(
        f".{basepath}{dir_path_content}",
        f".{basepath}{template_path}",
        f".{basepath}{dest_dir_path}",
        basepath,
    )


main()
