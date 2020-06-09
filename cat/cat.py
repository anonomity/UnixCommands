import argparse


parser = argparse.ArgumentParser(description = "concatination of our nation")

parser.add_argument('files', metavar='F', type=argparse.FileType('r+'), nargs='+',
        help = "a file for the accumulator")

parser.add_argument('--S', action='store',type=argparse.FileType('w'), required=False,
        )
args = parser.parse_args()
for f in args.files:
    args.S.write(f.read())
