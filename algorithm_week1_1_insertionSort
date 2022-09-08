def insertionSort(A): #insertion sort 함수 정의
    for j in range(1, len(A)): 
        key=A[j] 
        i=j-1 #i는 key 전 요소
        while i>=0 and A[i]>key: 
            A[i+1]=A[i]
            i=i-1 #key(A[i+1])보다 A[i]가 크면 자리를 바꿈
        A[i+1]=key 


x = int(input()) #array 에 포함된 요소 갯수
num_list = [] #array
for i in range(x):
    num_list.append(int(input())) #반복문으로 array에 요소 추가

insertionSort(num_list) #위에 정의내린 insertion sort 함수로 num_list 정렬

for i in num_list:
    print(i) #한 요소 당 한 줄씩 출력



