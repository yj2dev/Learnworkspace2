# 사과나무 (다이아몬드)
import sys
sys.stdin=open("input.txt", "r")

def printArr(arr):
    for i in arr:
        print(*i)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

printArr(arr)