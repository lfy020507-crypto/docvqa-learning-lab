from pathlib import Path
import json
path = Path("../Text recognition/数据集raw docvqa/spdocvqa_qas/val_v1.0_withQT.json")
print(path.resolve())  # 看看实际指向哪里
print(path.exists())   # 应该输出 True
content = json.loads(path.read_text(encoding="utf-8"))
data = content["data"]
print(data[0])
'''
for i in range(5):
    det = data[i]
    print(f"{det["question"]}")
    print(f"{det["answers"]}")
    print(f"{det["answers"][0]}")
'''
if __name__ == "__main__":
    for det in data[:5]:
        print(f"{det["question"]}")
        print(f"{det["answers"]}")
        print(f"{det["answers"][0]}")