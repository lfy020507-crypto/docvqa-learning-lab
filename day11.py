#把匹配到的答案框画到 10 张图片上
import day8
import day10
import json
from pathlib import Path
from PIL import Image, ImageDraw
lis = []
output_dir  = Path("output_day11") #在当前目录创建文件夹
output_dir.mkdir(parents=True, exist_ok=True) #parents=True：如果上级文件夹不存在，就自动创建。
#exist_ok=True：如果文件夹已经存在，就不报错。
ori_dir = Path("../Text recognition/数据集raw docvqa")
qa_path = ori_dir / "spdocvqa_qas" / "val_v1.0_withQT.json"
content = json.loads(qa_path.read_text(encoding="utf-8"))
data_set = content["data"]

saved_count = 0

for data in data_set:
    image_name = Path(data["image"]).name
    image_path = ori_dir / "spdocvqa_images" / image_name
    question_id = data.get("questionId")
    ocr_name = Path(image_name).with_suffix(".json")
    ocr_path = ori_dir / "spdocvqa_ocr" / ocr_name

    ocr = json.loads(ocr_path.read_text(encoding="utf-8"))
    lines = ocr["recognitionResults"][0]["lines"]

    matched = False
    for answer in data["answers"]:
        matched, boxes, matched_words = day8.match_consistent(answer, lines)
        if matched:
            break
    if matched:
        record = {
            "question_Id":question_id,
            "answer":answer,
            "image_path":str(image_path), #Path对象需要处理
            "matched":matched_words
            }
        if all(record.values()):
            image = Image.open(image_path).convert("RGB")
            draw = ImageDraw.Draw(image)

            for box in boxes:
                draw.rectangle(day10.trans_bbox(box), outline="red", width=3)

            output_path = output_dir / f'{data["questionId"]}_{Path(image_name).stem}_bbox.png'
            image.save(output_path)
            print("已保存：", output_path)


            lis.append(record)
            saved_count += 1
        if saved_count == 10:
            output_json_path = output_dir/"log.json"
            with output_json_path.open("w", encoding="utf-8") as f:
                json.dump(lis,f,ensure_ascii=False,indent=2)
            break

print("总共保存：", saved_count, "张")