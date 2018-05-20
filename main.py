#!/usr/bin/env python
# -*- coding: utf-8 -*-

def argsparse(args):
    assert len(args) >= 2,\
    "m(-_-)m This script takes one argument.\
    \n usage: $python ./PltText2Pdf.py hoge.csv"
    return args[1]

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
    plt.figure(figsize=(30,100))
    plt.xlim([0,500000])
    plt.ylim([0,100000000])
    for line in csv_:
        plt.text(line[1],line[2],line[0])
    plt.savefig("graph.pdf")
