#把 OCR 多边形转换成矩形框，画到 1 张原图上
from pathlib import Path
bbox = [622,
        138,
        1137,
        136,
        1138,
        167,
        622,
        168]
org_path = Path("../Text recognition/数据集raw docvqa")
picture_path = org_path/"spdocvqa_images/ffbf0023_4.png"
xs = bbox[0::2]
ys = bbox[1::2]
left, right = min(xs), max(xs)
top, bottom = min(ys), max(ys)
from PIL import Image, ImageDraw
image = Image.open(picture_path).convert("RGB")
draw = ImageDraw.Draw(image)
draw.rectangle((left, top, right, bottom), outline="red", width=3)
image.show()