x,y=map(int,input().split()) #동전 종류 가짓수 x와 거스를 돈 y를 입력

num_list=[]#동전 종류를 담을 리스트 생성
for i in range(x):
    s=int(input())
    num_list.append(s)#리스트에 어떤 동전들이 있는 지 x개만큼 입력

count=0

for i in reversed(range(x)):

    count=count+(y//num_list[i])
    y=y%num_list[i]

print(count)



