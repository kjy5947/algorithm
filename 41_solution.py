
def DFS(n):
    if n > 0:
        DFS(n//2)
        print(n % 2, end='')
    else: return
num=int(input())

DFS(num)
