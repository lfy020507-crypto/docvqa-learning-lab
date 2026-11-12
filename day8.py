import Day6
def match_consistent(answer: str, lines:list):
    length = len(answer.split())

    result = False

    for line in lines:
        words_ls = []
        for word in line["words"]:
            words_ls.append(word["text"])

        if length > len(words_ls):
            continue
        else:
            i = 0
            while i + length <= len(words_ls):
                selected = line["words"][i:i + length]
                combine = " ".join(word["text"] for word in selected)

                if Day6.normalize(combine) == Day6.normalize(answer):
                    result = True
                    print("匹配文字：", combine)
                    boxes = [word["boundingBox"] for word in selected]
                    print("原始坐标：", boxes)
                    return True, boxes, combine

                i += 1

    print("no matching results")
    return False, [], []