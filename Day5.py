import json
from pathlib import Path
data_dir = Path("../Text recognition/数据集raw docvqa")
qa_path = data_dir / "spdocvqa_qas" / "val_v1.0_withQT.json"
image_dir = data_dir / "spdocvqa_images"
ocr_dir = data_dir / "spdocvqa_ocr"

qa_content = json.loads(qa_path.read_text(encoding="utf-8"))
questions = qa_content["data"][:10]

missing_images = []
missing_ocr = []

for qa in questions:
    question_id = qa["questionId"]
    image_name = Path(qa["image"]).name

    image_path = image_dir / image_name
    ocr_path = ocr_dir / Path(image_name).with_suffix(".json")

    if not image_path.exists():
        missing_images.append(question_id)

    if not ocr_path.exists():
        missing_ocr.append(question_id)

print("检查题数：", len(questions))
print("缺图片题数：", len(missing_images))
print("缺图片的题号：", missing_images)
print("缺 OCR 题数：", len(missing_ocr))
print("缺 OCR 的题号：", missing_ocr)