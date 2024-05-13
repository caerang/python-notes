import argparse

parser = argparse.ArgumentParser(description='Argparse Tutorial')
# argument는 원하는 만큼 추가한다.
parser.add_argument('--print-number', type=int, 
                    help='an integer for printing repeatably')
parser.add_argument('--foo1', action='store_true')
parser.add_argument('--foo2', action='store_true')
parser.add_argument('--foo3', action='store_false')
parser.add_argument('--foo4', action='store_false')
args = parser.parse_args()
print('args.foo1:', args.foo1)
print('args.foo2:', args.foo2)
print('args.foo3:', args.foo3)
print('args.foo4:', args.foo4)

# for i in range(args.print_number):
#     print('print number {}'.format(i+1))