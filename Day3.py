from pathlib import Path
import Day2
import json
init_path = Path("../Text recognition/数据集raw docvqa/spdocvqa_ocr")
ocr_path = init_path/Path(Day2.file_name).with_suffix(".json")
'''.with_suffix()它会返回一个新的 Path 对象'''
print()
content = json.loads(ocr_path.read_text(encoding="utf-8"))
data = content["recognitionResults"][0]["lines"]
words_num = 0
i = 0
while i < len(data) and words_num < 20:
    word = data[i]["words"]
    for j in range(len(word)):
        print(word[j]["text"],end=" ")
        words_num += 1
        if words_num == 20:
            break

    i += 1