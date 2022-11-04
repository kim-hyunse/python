a, b, c = map(int, input().split()) #입력값 Ax+By=C 를 만족하는 A,B,C 입력
def gcd(a, b): #최대 공약수를 구하는 GCD 구현
  if b == 0:
    return a 
  else:
    return gcd(b, a % b) #recursive function

def extended_euclid(a, b): #extended euclid 구현
  ret = [0] * 2 
  if b == 0: #b가 0이 될 때 
    ret[0] = 1  
    ret[1] = 0
    return ret #x값 1 y값 0으로 return

  q = a // b #a를 b로 나눈 몫
  V = extended_euclid(b, a % b) 
  ret[0] = V[1] 
  ret[1] = V[0] - V[1] * q #x = y', y = x'-y'-q 구현
  return ret #계산된 x, y return

mgcd = gcd(a, b) #최대공약수

if c % mgcd != 0: #c가 최대 공약수의 배수가 아닌 경우
  print(-1) #-1 return 
else: 
  share = int(c/ mgcd) #b 0될 때까지 extended_euclid 호출
  ret = extended_euclid(a, b) 
  print(ret[0] * share, end=' ' ) 
  print(ret[1] * share)
