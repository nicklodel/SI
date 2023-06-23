# argparse1.py
# argparse simple example with positional arguments

import argparse
parser = argparse.ArgumentParser(description='Display a square of a given number')

#adding 1 positional argument
parser.add_argument("number", help="the number to square", type=int)

#adding 1 positional argument
parser.add_argument("name", help="your name", type=str)

args = parser.parse_args()
print(f"n. arguments = {len(vars(args))}")
print("args.number= ", args.number, "\n")
print("args.name= ", args.name, "\n")

print(args.number**2)

# Try:
# $python3 argparse1.py
# $python3 argparse1.py -h
# $python3 argparse1.py --help
# $python3 argparse1.py 4
# $python3 argparse1.py hola Juan
# $python3 argparse1.py 3 Juan


