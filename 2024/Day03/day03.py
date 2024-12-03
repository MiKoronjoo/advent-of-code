import re
import sys

inp1 = sys.stdin.read()
inp2 = ''.join(x.split("don't()")[0] for x in inp1.split('do()'))
print(sum(int(n1) * int(n2) for n1, n2 in re.findall(r'mul\((\d+),(\d+)\)', inp1)))
print(sum(int(n1) * int(n2) for n1, n2 in re.findall(r'mul\((\d+),(\d+)\)', inp2)))
