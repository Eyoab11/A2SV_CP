#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.read
data = input().splitlines()
english = set(map(int, data[1].split()))
french = set(map(int, data[3].split()))
engFrench = english.union(french)
print(len(engFrench))
