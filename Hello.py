import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('names')
parser.add_argument('--repeat', type=int,default=1)
args = parser.parse_args()


for _ in range(args.repeat):
  print("Hello " + args.names + '!')