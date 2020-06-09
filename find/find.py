#Search for file
import glob
#see if path exists
import os
#execute unix commands
import subprocess
import argparse

# ! python3 find.py :
parser = argparse.ArgumentParser(description='Jackies Unix find command')

parser.add_argument('strings', metavar='F', type=str, nargs='+',
        help="a file for the accumulator")

parser.add_argument('--P', action='store', type=str, required=False)
args = parser.parse_args()

files = []
paths = []
for i in range(len(args.strings)):
    if(len(args.strings[i].split('.')) > 1):
        files.append(args.strings[i])
    if(len(args.strings[i].split('/')) > 1):
        if(os.path.lexists(args.strings[i])):
            paths.append(args.strings[i])

for j in range(len(files)):
    # prints if the file is there
    glob.glob(files[j])

print(args.P)
