from pathlib import Path
from pdf_to_image import Pdf2Image
from image_ocr import directoryImageOCR
from sensitive_scan import sensitive_scan
from blackout_image import blackout_image
from images_merge_to_pdf import merge_to_pdf

def privacy_erase(filepath):
    stem = Path(filepath).stem

    # images storage path: ./tempFiles/stem/PageImages
    image_dir_path = './tempFiles/' + stem + '/PageImages/'
    # json storage path: ./tempFiles/stem/ScanJson
    json_dir_path = './tempFiles/' + stem + '/ScanJson/'
    # scan text storage path: ./tempFiles/stem/ScanText
    text_dir_path = './tempFiles/' + stem + '/ScanText/'
    # blackout images storage path: ./tempFiles/stem/BlackoutImages
    blackout_dir_path = './tempFiles/' + stem + '/BlackoutImages/'
    # output pdf path: ./tempFiles/stem/stem_privacy_erased.pdf
    output_pdf = './tempFiles/' + stem + '/' + stem + '_privacy_erased.pdf'
    
    if not Path(image_dir_path).exists():
        Path(image_dir_path).mkdir(parents=True)

    if not Path(json_dir_path).exists():
        Path(json_dir_path).mkdir(parents=True)
    
    if not Path(text_dir_path).exists():
        Path(text_dir_path).mkdir(parents=True)

    if not Path(blackout_dir_path).exists():
        Path(blackout_dir_path).mkdir(parents=True)


    # 1. Convert pdf to image.
    Pdf2Image(filepath, image_dir_path)

    # 2. do OCR on images.
    directoryImageOCR(image_dir_path)

    # 3. scan sensitive words.
    # for each stem file, get the blackout list. and file name into a list., which {filename: blackout_list}
    total_blackout_list = []
    for image_json in Path(json_dir_path).glob('*.json'):
        # print(image_json)
        blackout_list = sensitive_scan(image_json)
        print(blackout_list)
        total_blackout_list.append({image_json.stem: blackout_list})

    # 4. blackout sensitive words.
    for item in total_blackout_list:
        for key, value in item.items():
            print(key, value)
            image_path = image_dir_path + key + '.png'
            blackout_image(image_path, value)

    # 5. merge images to pdf.
    merge_to_pdf(blackout_dir_path, output_pdf)


if __name__ == "__main__":
    # filepath = 'D:/_UserDocuments/Desktop/IEEE Xplore download/Associative_memory_based_fuzzy_inference.pdf'
    # filepath =  'D:/_UserDocuments/Desktop/PPPPPPP/file/udgra_02.pdf'
    # filepath = 'D:/_UserDocuments/Desktop/PPPPPPP/file/grb_02.pdf'
    filepath = "D:/_UserDocuments/Desktop/PPPPPPP/file/chen_p1.pdf"

    privacy_erase(filepath)
