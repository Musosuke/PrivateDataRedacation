from reportlab.pdfgen import canvas
from PIL import Image
import os


# function merge_to_pdf, input: filename_list and output_file_name, output: .pdf file
# implement: merge files in list
def merge_to_pdf(image_folder, output_pdf):
    # 列出文件夾中的所有圖片文件
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # 創建一個PDF文件
    c = canvas.Canvas(output_pdf)
    
    for image_file in image_files:
        # 合併圖片到PDF中
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        
        # 取得圖片的寬度和高度
        width, height = img.size
        
        # 添加一頁到PDF
        c.setPageSize((width, height))
        c.drawInlineImage(image_path, 0, 0, width, height)
        c.showPage()
    
    # 保存PDF文件
    c.save()



if __name__ == "__main__":
    image_folder = "/path/to/your/image/folder"
    output_pdf = "/path/to/your/output/file.pdf"

    convert_images_to_pdf(image_folder, output_pdf)