import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

print(*sorted(arrA+arrB))