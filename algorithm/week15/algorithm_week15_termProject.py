import sys
from collections import deque

f, s, g, u, d = map(int, input().split())
#f:건물의 총 층수
#s:지금 있는 층
#g:목적지의 층수
#u:위로 u층만큼 가기
#d:아래로 d층만큼 가기

visited = [0 for i in range(f+1)] #방문 여부
count = [0 for i in range(f+1)] #몇번 만에 갔는 지

def bfs(v): #너비우선탐색
    
    q = deque([v]) #현재 층을 큐에 넣기
    visited[v] = 1 #방문했다고 체크
    
    while q:
        v = q.popleft() #머문 층을 q에서 빼주기
        
        if v == g: #목적지 층이 현재 목적지와 같으면
            return count[g] 
        
        for i in (v+u, v-d): #u만큼 위로/d만큼 아래로
            if 0 < i <= f and not visited[i]:
            #i가 범위 안에 속하고 visited[i]가 방문하지 않은 층이면
                visited[i] = 1 #방문했다고 체크
                count[i] = count[v] + 1 #방문 횟수 +1
                q.append(i) 
                
    if count[g] == 0: #엘리베이터로 g층에 못 가는 경우
        return 'use the stairs' #계단 이용


print(bfs(s))
