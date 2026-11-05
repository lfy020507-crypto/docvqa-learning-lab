'''把一道题的 QA、图片、OCR 合并成一个自己设计的简单数据对象.打印题号、答案、图片尺寸、OCR 词数'''
import json
from PIL import Image
from pathlib import Path
init_path = Path("../Text recognition/数据集raw docvqa")
qas = init_path/Path("spdocvqa_qas/val_v1.0_withQT.json")
qa_content = json.loads(qas.read_text(encoding="utf-8"))
dataset = qa_content["data"][0]
q,a = dataset["question"], dataset["answers"]
image_init_path = dataset["image"]
#################################
image_path = Path(image_init_path).name
print(type(image_path))
toge_image_path = init_path/"spdocvqa_images"/image_path
print(type(toge_image_path))
with Image.open(toge_image_path) as f:
    size = f.size
    print(size)
#################################
ocr_name = Path(image_path).with_suffix(".json")
ocr_path = init_path/"spdocvqa_ocr/"/ocr_name
ocr = json.loads(ocr_path.read_text(encoding="utf-8"))
ocr_lines = ocr['recognitionResults'][0]["lines"]
################################
item = {
    "Question":q,
    "Answers":a,
    "Image":image_path,
    "OCR":ocr_lines
}
for key,value in item.items():
    print(key,value,sep="---->")