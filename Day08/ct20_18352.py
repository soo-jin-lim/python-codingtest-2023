# 백준 18352 -  특정 도시찾기
import sys
from collections import deque
input = sys.stdin.readline

M,K,N,X = map(int,input().split())
A = [[ ]for _ in range(N+1)]
anwer = [] 
visited = [-1] * (N+1) #방문리스트 초기화

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] += 1
    while q:
        now =  q.popleft()
        for i in A[now]:
            if visited[i] == -1: # 미방문이면
                visited[i] = visited[now] + 1
                q.append(i)

# 두번째 줄부터 엣지 입력
for _  in range(M):
    s,e = map(int,input().split())
    A[s].append(e)

BFS(X) #시작점 부터 BFS시작

for i in range(N+1):
    if visited[i] == K:
        anwer.append(i)

if len(anwer) == 0:
    print(-1)
else:
    anwer.sort()
    for i in anwer:
        print(i)


    
