num1=int(input('첫번째정수를입력하세요:'))
num2=int(input('두번째정수를입력하세요:'))
num3=int(input('세번째정수를입력하세요:'))
max=num1
if num2>max:
    max=num2
    
if num3>max:
    max=num3
    
print('{} {} {} 중 가장 큰 수는 {}이다.'
      .format(num1, num2, num3, max))
