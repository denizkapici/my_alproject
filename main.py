import random
import argparse

parser = argparse.ArgumentParser(description='Random number generator')
parser.add_argument('--min', type=int, default=1, help='Minimum value')
parser.add_argument('--max', type=int, default=100, help='Maximum value')
args = parser.parse_args()

random_number = random.randint(args.min, args.max)
print(f'Random number: {random_number}')
