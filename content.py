#!/usr/bin/env python

from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

args = parser.parse_args()

args.seq = args.seq.upper()  

lenght = len(args.seq)
g_content = seq.count('G') / lenght *100
c_content = seq.count("C") / lenght *100

print(f"The G content is {g_content}, the proportion of C is {c_content}")
