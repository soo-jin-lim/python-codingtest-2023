#  백준 1516- 게임개발
from collections import deque

N = int(input())
A = [[] for _ in range(N+1)] # 0번 인덱스는 안씀
indegree = [0] * (N + 1) # 자기건물 빌드시간
selfBulild = [0] * (N + 1) # 진입차수

for i in range(1, N+1):
    inputList = list(map(int, input().split()))
    selfBulild[i] = inputList[0] # 건물 빌드시간
    index = 1
    while True: # 인접리스트
        preTemp = inputList[index]
        index += 1
        if preTemp == -1: break # while문 탈출  

        A[preTemp].append(i)
        indegree[i] += 1 # 진입차수 증가

q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i) # 1부터 시작

result = [0] * (N+1)

while q: # 위상정렬 수행
    now = q.popleft()
    for next in A[now]: # 1--> 2,3,4
        indegree[next] -= 1 # 방문했으니깐 -1 감소
        #시간업데이트
        result[next] = max(result[next], result[now] + selfBulild[now])
        if indegree[next] == 0:
            q.append(next)

for i in range(1, N+1):
    print(result[i] + selfBulild[i])
