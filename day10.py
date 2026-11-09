#把 OCR 多边形转换成矩形框，画到 1 张原图上
from pathlib import Path
from PIL import Image, ImageDraw
org_path = Path("../Text recognition/数据集raw docvqa")
picture_path = org_path/"spdocvqa_images"
sp_path = picture_path/"ffbf0023_4.png"
def trans_bbox(bbox:list):

    xs = bbox[0::2]
    ys = bbox[1::2]
    left, right = min(xs), max(xs)
    top, bottom = min(ys), max(ys)
    return left, top, right, bottom
'''
image = Image.open(sp_path).convert("RGB")
draw = ImageDraw.Draw(image)
draw.rectangle((trans_bbox([622, 138, 1137, 136, 1138, 167, 622, 168])), outline="red", width=3)
image.show() 
'''
'''也可以把画图过程放进函数，但是为了加深记忆，day11再写一遍'''