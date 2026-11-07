from pathlib import Path
import json
import day8

org_path = Path("../Text recognition/数据集raw docvqa")
qa_path = org_path / "spdocvqa_qas" / "val_v1.0_withQT.json"
all_qa = json.loads(qa_path.read_text(encoding="utf-8"))

questions = all_qa["data"][:20]
failure_ids = []

for q in questions:
    ocr_name = Path(q["image"]).with_suffix(".json").name #注意处理方式
    ocr_path = org_path / "spdocvqa_ocr" / ocr_name
    ocr = json.loads(ocr_path.read_text(encoding="utf-8"))
    lines = ocr["recognitionResults"][0]["lines"]

    matched = False
    for answer in q["answers"]:
        if day8.match_consistent(answer, lines):
            matched = True
            break

    if not matched:
        failure_ids.append(q["questionId"])

coverage = (len(questions) - len(failure_ids)) / len(questions) * 100
print("覆盖率：", f"{coverage:.1f}%")
print("失败题号：", failure_ids)