#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Seq in upper letters

if re.search('^[ACGTU]+$', args.seq):
    if "U" in args.seq and "T" not in args.seq:
        print ('The sequence is RNA') #If  it has a U and not T, it is RNA
    elif "U" in args.seq and "T" in args.seq:
        print ('You have mixed DNA and RNA') #If it has  U and T it is a mix
    else:
        print ('The sequence is DNA') #If it has not U but ACGT, it is DNA
else:
    print ('The sequence is not DNA nor RNA!')
