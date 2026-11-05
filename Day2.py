import day1 #只要调用必须import
'''加载并执行 day1.py 顶层的代码，然后你才能用 day1.data'''
from pathlib import Path
file_in_qa = day1.data[0]["image"]
print(f"{file_in_qa}") #documents/pybv0228_81.png
file_name = Path(file_in_qa).name #pybv0228_81.png 
'''写 .name，不加括号。
它从 Path 对象中返回一个新的字符串，不会把原来的 Path 对象改成字符串'''
print(f"{file_name}")
print(type(file_name))
image_dir = Path("../Text recognition/数据集raw docvqa/spdocvqa_images")
image_path = image_dir/file_name
print(image_path.exists())
from PIL import Image
with Image.open(image_path) as f:
    print(f.size)