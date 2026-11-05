#写文字规范化函数，处理大小写、首尾空格和连续空格
def normalize(line:str) -> str:
    words = line.lower().split()
    '''split() 不传参数时，Python 会按空白字符拆分，并跳过连续空白；空格、制表符和换行都能处理。
    `split(" ")` 则指定“每遇到一个普通空格就切一次”'''
    return " ".join(words)
a = "Clai     sbcvsdfjoi   "
print(normalize(a))