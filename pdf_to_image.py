import datetime
import os
import fitz

def Pdf2Image(pdf_file_path, image_dir_path):
    # start_time = datetime.datetime.now()

    print("image_file_path=" + image_dir_path)

    pdf_doc = fitz.open(pdf_file_path)
    for pg in range(pdf_doc.pageCount):
        page = pdf_doc[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)
        pix.writePNG(image_dir_path + '/' + 'images_%s.png' % pg)

    # end_time = datetime.datetime.now()
    # print('pdf2img时间=', (end_time - start_time).seconds)


if __name__ == "__main__":
    # pdf_file_path = r'./tempFiles/udgra_02/udgra_02.pdf'
    # image_dir_path = './tempFiles/udgra_02/PageImages'
    
    # Pdf2Image(pdf_file_path, image_dir_path)
    exit(0)


