import re


# 清理文本
def get_only_chars(line):
    clean_line = ""

    line = line.lower()
    line = line.replace(" 's", " is")
    line = line.replace("-", " ")  # 用空格替换连字符
    line = line.replace('\t', " ")
    line = line.replace("\n", " ")
    line = line.replace("'", "")

    for char in line:
        if char in 'qwertyuiopasdfghjklzxcvbnm ':
            clean_line += char
        else:
            clean_line += ' '

    clean_line = re.sub(' +', ' ', clean_line)  # 删除多余空格

    if clean_line[0] == ' ':
        clean_line = clean_line[1:]

    return clean_line
