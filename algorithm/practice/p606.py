# 중복순열 구하기(DFS)  
import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

def dfs(L):
    if L == m:
        pass
    else:
        for i in range(1, n + 1):
            res[L] = i
            dfs(L + 1)



if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)