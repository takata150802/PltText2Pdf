#!/usr/bin/env python
# -*- coding: utf-8 -*-

def argsparse(args):
    assert len(args) >= 2,\
    "m(-_-)m This script takes one argument.\
    \n usage: $python ./PltText2Pdf.py hoge.csv"
    return args[1]

def is_equal_any(i,ls_):
    return reduce(lambda x,y: x or y ,[i == x for x in ls_])
def plot_grid(n_x, n_y, size_x, size_y):
    for i in range(n_x + 1):
        color_ = "red" if i % 5 == 0 else "gray"
        plt.plot([i * size_x, i * size_x], [0, n_y * size_y], color_)
    for i in range(n_y + 1):
        color_ =  "red" if is_equal_any(i,[0,5,10,15,20,22,27,32,37,42]) else "gray"
        plt.plot([0, n_x * size_x], [i * size_y, i* size_y], color_)
    for i in range(n_x + 1):
        for j in range(n_y + 1):
            plt.text(i * size_x, j * size_y, "(%d,%d)" % (i,j))
    range_x = [0, n_x * size_x]
    range_y = [0, n_y * size_y]
    return range_x, range_y

if __name__ == '__main__': 
    import sys
    args = sys.argv
    path = argsparse(sys.argv)

    import csv
    csv_ = []
    with open(path,"r") as fp:
        reader = csv.reader(fp, delimiter=",")
        for line in reader:
            csv_.append([line[0], int(line[1]), int(line[2])])
    print csv_

    import matplotlib.pyplot as plt
    plt.figure(figsize=(50,100))
    range_x, range_y = plot_grid(5,40,25, 250)
    plt.xlim(range_x)
    plt.ylim(range_y)
    for line in csv_:
        plt.text(line[1] * 10**-4,line[2] * 10**-4,line[0])
    plt.savefig("graph.pdf")
