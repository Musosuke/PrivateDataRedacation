import os
from paddleocr import PaddleOCR
import datetime
import json


def ImageOCR(filepath):
    if not os.path.exists(filepath):
        print('file not exist')
        return
    
    if not filepath.endswith('.png'):
        print('incorrect file format, only png is supported')
        return

    ocr = PaddleOCR(use_angle_cls=True, lang="ch") 

    # using paddleocr to detect text and save to txt in same name folder and same image name
    imagePath = filepath
    result = ocr.ocr(imagePath, cls=True)

    # save result to txt line by line
    # txtpath change to ../ScanJson/udgra_02/
    txtPath = filepath.replace('PageImages', 'ScanJson') #
    txtPath = txtPath.replace('.png', '.json') #

    with open(txtPath, 'w', encoding='utf-8') as f:
        # dump result to json file
        json.dump(result, f, ensure_ascii=False)



# call imageOCR for all png files in a directory
def directoryImageOCR(directoryPath):
    if not os.path.exists(directoryPath):
        print('directory not exist')
        return

    if not os.path.isdir(directoryPath):
        print('not a directory object')
        return

    for filename in os.listdir(directoryPath):
        if filename.endswith(".png"):
            print('processing file: ' + filename)
            imagePath = os.path.join(directoryPath, filename)
            ImageOCR(imagePath)
        else:
            continue


if __name__ == '__main__':
    image_dir_path = './tempFiles/udgra_02/PageImages'

    directoryImageOCR(image_dir_path)

    exit(0)




