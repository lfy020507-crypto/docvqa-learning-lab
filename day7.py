import Day6
#1. 从 QA 记录取出一个答案，从对应的 OCR 文件取出 lines。
#2. 遍历每一行的 words，比较答案和 word["text"]。比较前可以用 Day 6 的 normalize() 处理大小写和多余空格。
#3. 找到后输出 word["text"] 和 word["boundingBox"]；找不到就明确输出“未匹配”。
def match(words:str, answer:str) -> bool:
    if (Day6.normalize(words) == Day6.normalize(answer)):
        return True
    return False


ans = ...
lines = ...

found = False
for line in lines:
    for word in line["words"]:
        if match(word["text"], ans):
            text = word["text"]
            bbox = word["boundingBox"]
            found = True
            break
    if found:
        break


if found:
    print(text, bbox)
else:
    print("no matching results")