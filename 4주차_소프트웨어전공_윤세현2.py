user_id="lovePython!"
user_pw="p12345"
ID=input('아이디를 입력하세요:')


if ID==user_id:
    password=input('비밀번호를 입력하세요:')

    if password==user_pw:
     print('lovePython!님 환영합니다~!!')
    else:
      print('비밀번호가 틀립니다.')
    
else:
    print('아이디를 찾을 수 없습니다')
    

