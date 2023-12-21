from PIL import Image, ImageDraw
from pathlib import Path


def blackout_image(imagePath, blackout_list:list):
    """
    Blackout the image with a given color
    :param img: image to blackout
    :param blackout: color to blackout with
    :return: blacked out image
    """
    image = Image.open(imagePath).convert('RGB')#開啟原圖片來塗黑
    draw = ImageDraw.Draw(image) #建立一個畫布

    for box in blackout_list:
        # box是一个包含四个坐标的列表，格式为 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
        # 转换坐标为整数类型
        box = [(int(x), int(y)) for x, y in box]
        
        # 绘制矩形框并将其塗黑
        draw.polygon(box, fill=0)  # 使用黑色填充框

    # store in ./tempFiles/stem/BlackoutImages/
    path = imagePath.split('PageImages')[0] + 'BlackoutImages/'
    imagestem = Path(imagePath).stem
    image.save(path + imagestem + '_blackout.png')
