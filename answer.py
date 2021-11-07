def nothing():
    '''Student's hw should be "mv" into "anwser.py" '''
    pass


def Q1_Draw_an_arrow(treeSize):
    if(treeSize < 2):
        print("Too small!!!")
        return
    a = '_'
    b = '*'
    for i in range(treeSize + 1):
        print(a * (treeSize - i) + b * (2 * i + 1) + a * (treeSize - i))
    for _ in range(treeSize + 1):
        print(a * (treeSize - treeSize // 2) + b *
              (2 * (treeSize//2) + 1) + a * (treeSize - treeSize // 2))
