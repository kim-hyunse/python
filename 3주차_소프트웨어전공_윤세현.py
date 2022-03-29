Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input('정수를 입력하세요:'))
정수를 입력하세요:5741
>>> i=a//1000
>>> j=a%1000
>>> k=j//100
>>> l=j%100
>>> m=l//10
>>> n=l%10
>>> sum=i+k+m+n
>>> print('자릿수의 합은 {}이다'.format(sum))
자릿수의 합은 17이다
>>> 
