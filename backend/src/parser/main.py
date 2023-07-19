import os
from pathlib import Path

import mutagen

if __name__ == "__main__":
    root_path = Path("/data")

    l = list(root_path.glob("**/*"))
    filelist = [file for file in l if file.is_file() and mutagen.File(file) is not None]

    print(filelist)
