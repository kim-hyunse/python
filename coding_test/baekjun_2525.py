time = input().split()
add = int(input())

hour = int(time[0])
minute = int(time[1])+add

if (minute>= 59):
    hour= hour + minute//60
    minute = minute % 60
    
if (hour>=23):
    hour = hour % 24

print(hour, minute)
