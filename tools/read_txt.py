def read_txt(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    # print(read_txt("login.txt"))
    print("-"*30)
    arrs=[]
    for data in read_txt("login.txt"):
        # 列表添加元组
        arrs.append(tuple(data.strip().split(",")))
    # 返回列表下标为1之外的所有元素
    print(arrs[1:])
