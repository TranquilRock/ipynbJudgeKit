def Q1_Draw_an_arrow(treeSize):
    if(treeSize < 2):
        print("Too small!!!")
        return
    a = '_'
    b = '*'
    for i in range(treeSize + 1):
        print(a * (treeSize - i) + b * (2 * i + 1) + a * (treeSize - i))
    for _ in range(treeSize + 1):
        print(a * (treeSize - treeSize // 2) + b * (2 * (treeSize//2) + 1) + a * (treeSize - treeSize // 2))

import random
count = -1
arr = [i for i in range(1,100)]
def gen_data():
    global count
    '''return an array of test data'''
    count = count + 1
    return [arr[count]]
