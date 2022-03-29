quiz = ['1.중국의 수도를 선택하세요./1)칭따오/2)상하이/3)베이징']

for i in quiz :
    quizSplit = i.split('/')           # ['1.중국의 수도를 선택하세요.', '1)칭따오', '2)상하이', '3)베이징']
    print(quizSplit[0])                # 출력 
    print(quizSplit[1])
    print(quizSplit[2])
    print(quizSplit[3])
