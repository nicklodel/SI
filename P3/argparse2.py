# argparse2.py
# argparse simple example with optional arguments

import argparse

parser = argparse.ArgumentParser(description='cracks an encrypted ZIP file')

# Adding 2 optional arguments
parser.add_argument('-f', dest = "zname", type=str,	metavar='ZIPFILE',
                    help='specify zip file')
parser.add_argument('-d', dest = "dname", type=str,	metavar='DICTFILE', 
                    help='specify dictionary file')

# Adding 1 positional argument
parser.add_argument("number", help="the number to square", type=int)

args = parser.parse_args()
print(f"n. arguments = {len(vars(args))}")

# checking presence of optional arguments
if (args.zname == None) or (args.dname == None):
    print("Problems...")
else:
    print(f"{args.number= }")
    print(f"{args.zname= }")
    print(f"{args.dname= }")

# Try:
# $python3 argparse2.py 
# $python3 argparse2.py -h
# $python3 argparse2.py --help
# $python3 argparse2.py -f locked.zip -d dictionary.txt 4
# $python3 argparse2.py -f locked.zip 4 -d dictionary.txt
# $python3 argparse2.py 4 -f locked.zip -d dictionary.txt
# $python3 argparse2.py hola
