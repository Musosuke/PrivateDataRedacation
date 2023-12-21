from _privacy_erase import privacy_erase
import os
from pathlib import Path


# main
if __name__ == '__main__':
    filepath = str(input("Please input the file path: "))

    # check if the file exists 並且是pdf檔 並且不是資料夾
    if Path(filepath).exists() and Path(filepath).suffix == '.pdf' and not Path(filepath).is_dir():
        privacy_erase(filepath)
    else:
        print("Please input the correct file path.")
        exit(1)