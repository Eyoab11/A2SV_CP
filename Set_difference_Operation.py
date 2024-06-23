#Hackerrank Set .difference() Operation
import sys
input = sys.stdin.read
data = input().splitlines()
english = set(map(int, data[1].split()))
french = set(map(int, data[3].split()))
eng = english.difference(french)
print(len(eng))
