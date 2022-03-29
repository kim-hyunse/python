from tkinter import*
window=Tk()
window.geometry('1500x1000')



check=0;
s1 = [0,0,0,0] #마름 중 클릭된 것이 몇번인지 체크하는 배열
s2 = [0,0,0,0] #보통 중 클릭된 것이 몇번인지 체크하는 배열
s3 = [0,0,0,0] #비만 중 클릭된 것이 몇번인지 체크하는 배열



def f1():
    a=float(e2.get())*0.01
    b=float(e3.get())
    c=round(b/(a*a))
    e4.insert(0,c)
    if(c<=18):
        e5.insert(0,'마름')
        b1.configure(image=img1_1,command=s1_1)
        l7.configure(text="운동명:벤치프레스\n횟수&반복:1\n소요시간:1\n칼로리소모:8")
        b2.configure(image=img1_2,command=s1_2)
        l8.configure(text="운동명:벤트오버로우\n횟수&반복:1\n소요시간:1\n칼로리소모:8")
        b3.configure(image=img1_3,command=s1_3)
        l9.configure(text="운동명:크런치\n횟수&반복:1\n소요시간:1\n칼로리소모:8")
        b4.configure(image=img1_4,command=s1_4)
        l10.configure(text="운동명:힙 브릿지\n횟수&반복:1\n소요시간:1\n칼로리소모:8")
        
    elif(18<c<=24):
        e5.insert(0,'보통')
        b1.configure(image=img2_1,command=s2_1)
        l7.configure(text="운동명:스쿼트\n횟수&반복:1\n소요시간:10\n칼로리소모:10")
        b2.configure(image=img2_2,command=s2_2)
        l8.configure(text="운동명:수영\n횟수&반복:1\n소요시간:10\n칼로리소모:10")
        b3.configure(image=img2_3,command=s2_3)
        l9.configure(text="운동명:줄넘기\n횟수&반복:1\n소요시간:10\n칼로리소모:10")
        b4.configure(image=img2_4,command=s2_4)
        l10.configure(text="운동명:플랭크잭\n횟수&반복:1\n소요시간:10\n칼로리소모:10")
    else:
        e5.insert(0,'비만')
        b1.configure(image=img3_1,command=s3_1)
        l7.configure(text="운동명:자전거\n횟수&반복:1\n소요시간:10\n칼로리소모:40")
        b2.configure(image=img3_2,command=s3_2)
        l8.configure(text="운동명:런닝머신\n횟수&반복:1\n소요시간:10\n칼로리소모:100")
        b3.configure(image=img3_3,command=s3_3)
        l9.configure(text="운동명:요가\n횟수&반복:1\n소요시간:10\n칼로리소모:50")
        b4.configure(image=img3_4,command=s3_4)
        l10.configure(text="운동명:등산\n횟수&반복:1\n소요시간:10\n칼로리소모:150")
        
def add6(): #선택된 운동법을 버튼 b6에 나타내는 함수
    if s1[0] == 1:
        b6.configure(image=img1_1)
        l12.configure(text="운동명:벤치프레스\n횟수&반복:1\n소요시간:20\n칼로리소모:80\n추천시간대:점심")
    elif s1[1] == 1:
        b6.configure(image=img1_2)
        l12.configure(text="운동명:벤트오버로우\n횟수&반복:1\n소요시간:20\n칼로리소모:150\n추천시간대:저녁")
    elif s1[2] == 1:
        b6.configure(image=img1_3)
        l12.configure(text="운동명:크런치\n횟수&반복:1\n소요시간:20\n칼로리소모:20\n추천시간대:아침")
    elif s1[3] == 1:
        b6.configure(image=img1_4)
        l12.configure(text="운동명:힙 브릿지\n횟수&반복:1\n소요시간:20\n칼로리소모:50\n추천시간대:점심")
    elif s2[0] == 1:
        b6.configure(image=img2_1)
        l12.configure(text="운동명:스쿼트\n횟수&반복:1\n소요시간:20\n칼로리소모:120\n추천시간대:저녁")
    elif s2[1] == 1:
        b6.configure(image=img2_2)
        l12.configure(text="운동명:수영\n횟수&반복:1\n소요시간:20\n칼로리소모:180\n추천시간대:저녁")
    elif s2[2] == 1:
        b6.configure(image=img2_3)
        l12.configure(text="운동명:줄넘기\n횟수&반복:1\n소요시간:20\n칼로리소모:150\n추천시간대:아침")
    elif s2[3] == 1:
        b6.configure(image=img2_4)
        l12.configure(text="운동명:플랭크잭\n횟수&반복:1\n소요시간:20\n칼로리소모:50\n추천시간대:점심")
    elif s3[0] == 1:
        b6.configure(image=img3_1)
        l12.configure(text="운동명:자전거\n횟수&반복:1\n소요시간:20\n칼로리소모:40\n추천시간대:아침")
    elif s3[1] == 1:
        b6.configure(image=img3_2)
        l12.configure(text="운동명:런닝머신\n횟수&반복:1\n소요시간:20\n칼로리소모:50\n추천시간대:점심")
    elif s3[2] == 1:
        b6.configure(image=img3_3)
        l12.configure(text="운동명:요가\n횟수&반복:1\n소요시간:20\n칼로리소모:100\n추천시간대:저녁")
    else:
        b6.configure(image=img3_4)
        l12.configure(text="운동명:등산\n횟수&반복:1\n소요시간:20\n칼로리소모:150\n추천시간대:점심")




def s1_1():
    s1[1]=s1[2]=s1[3]=0
    s1[0]=1 #1_1이미지 버튼 눌렀을 때
    global check
    check=1
    add5()

def s1_2():
    s1[0]=s1[2]=s1[3]=0
    global check
    s1[1]=1 #1_2이미지 버튼 눌렀을 때
    if(check!=1):
        add5()
        
        check=1
    else:
        add6()

def s1_3():
    s1[1]=s1[0]=s1[3]=0
    s1[2]=1 #1_3이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        
        check=1
    else:
        add6()


def s1_4():
    s1[1]=s1[2]=s1[0]=0
    s1[3]=1 #1_4이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()
   

def s2_1():
    s2[1]=s2[2]=s2[3]=0
    s2[0]=1 #2_1이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()


def s2_2():
    s2[0]=s2[2]=s2[3]=0
    s2[1]=1 #2_2이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()


def s2_3():
    s2[1]=s2[0]=s2[3]=0
    s2[2]=1 #2_3이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()


def s2_4():
    s2[1]=s2[2]=s2[0]=0
    s2[3]=1 #2_4이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()

    
def s3_1():
    s3[1]=s3[2]=s3[3]=0
    s3[0]=1 #3_1이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()


def s3_2():
    s3[0]=s3[2]=s3[3]=0
    s3[1]=1 #3_2이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()


def s3_3():
    s3[1]=s3[0]=s3[3]=0
    s3[2]=1 #3_3이미지 버튼 눌렀을 때
    global check
    if(check!=1):
        add5()
        check=1
    else:
        add6()


def s3_4():
    s3[1]=s3[2]=s3[0]=0
    s3[3]=1 #3_4이미지 버튼 눌렀을 때
    add6()
    
    


def add5(): #선택된 운동법을 버튼 b5에 나타내는 함수
    if s1[0] == 1:
        b5.configure(image=img1_1)
        l11.configure(text="운동명:벤치프레스\n횟수&반복:1\n소요시간:20\n칼로리소모:80\n추천시간대:점심")
    elif s1[1] == 1:
        b5.configure(image=img1_2)
        l11.configure(text="운동명:벤트오버로우\n횟수&반복:1\n소요시간:20\n칼로리소모:150\n추천시간대:저녁")
    elif s1[2] == 1:
        b5.configure(image=img1_3)
        l11.configure(text="운동명:크런치\n횟수&반복:1\n소요시간:20\n칼로리소모:20\n추천시간대:아침")
    elif s1[3] == 1:
        b5.configure(image=img1_4)
        l11.configure(text="운동명:힙 브릿지\n횟수&반복:1\n소요시간:20\n칼로리소모:50\n추천시간대:점심")
    elif s2[0] == 1:
        b5.configure(image=img2_1)
        l11.configure(text="운동명:스쿼트\n횟수&반복:1\n소요시간:20\n칼로리소모:120\n추천시간대:저녁")
    elif s2[1] == 1:
        b5.configure(image=img2_2)
        l11.configure(text="운동명:수영\n횟수&반복:1\n소요시간:20\n칼로리소모:180\n추천시간대:저녁")
    elif s2[2] == 1:
        b5.configure(image=img2_3)
        l11.configure(text="운동명:줄넘기\n횟수&반복:1\n소요시간:20\n칼로리소모:150\n추천시간대:아침")
    elif s2[3] == 1:
        b5.configure(image=img2_4)
        l11.configure(text="운동명:플랭크잭\n횟수&반복:1\n소요시간:20\n칼로리소모:50\n추천시간대:점심")
    elif s3[0] == 1:
        b5.configure(image=img3_1)
        l11.configure(text="운동명:자전거\n횟수&반복:1\n소요시간:20\n칼로리소모:40\n추천시간대:아침")
    elif s3[1] == 1:
        b5.configure(image=img3_2)
        l11.configure(text="운동명:런닝머신\n횟수&반복:1\n소요시간:20\n칼로리소모:50\n추천시간대:점심")
    elif s3[2] == 1:
        b5.configure(image=img3_3)
        l11.configure(text="운동명:요가\n횟수&반복:1\n소요시간:20\n칼로리소모:100\n추천시간대:저녁")
    else:
        b5.configure(image=img3_4)
        l11.configure(text="운동명:등산\n횟수&반복:1\n소요시간:20\n칼로리소모:150\n추천시간대:점심")

def p1():
    f = int(e13.get())
    s = int(e14.get())
    e15.insert(0, 20*f+20*s)


#사용하실 사진 여기에 경로 저장해주세요 png만 가능하니 변환프로그램 사용, 크기200x200으로 통일했습니다\
    
img1=PhotoImage(file="default.png")

img1_1=PhotoImage(file="1_1.png")
img1_2=PhotoImage(file="1_2.png")
img1_3=PhotoImage(file="1_3.png")  
img1_4=PhotoImage(file="1_4.png")

img2_1=PhotoImage(file="2_1.png")
img2_2=PhotoImage(file="2_2.png")
img2_3=PhotoImage(file="2_3.png")  
img2_4=PhotoImage(file="2_4.png")

img3_1=PhotoImage(file="3_1.PNG")
img3_2=PhotoImage(file="3_2.PNG")
img3_3=PhotoImage(file="3_3.PNG")  
img3_4=PhotoImage(file="3_4.PNG")

l1=Label(window,text='이름:')
l1.grid(column=0, row=0)
e1=Entry(window,width=10)
e1.grid(column=1, row=0)

l2=Label(window,text='키(cm):')
l2.grid(column=2, row=0)
e2=Entry(window,width=10)
e2.grid(column=3, row=0)

l3=Label(window,text='몸무게:')
l3.grid(column=4, row=0)
e3=Entry(window,width=10)
e3.grid(column=5, row=0)

b1=Button(window,text='입력',width=7,command=f1)
b1.grid(column=6, row=0)

l4=Label(window,text='     BMI:')
l4.grid(column=7, row=0)
e4=Entry(window,width=5)
e4.grid(column=8, row=0)

l5=Label(window,text='  체형:')
l5.grid(column=9, row=0)
e5=Entry(window,width=5)
e5.grid(column=10, row=0)

b1=Button(window,image=img1)
b1.grid(column=1,row=5,columnspan=4,rowspan=3)
l7=Label(window,text="운동명:\n횟수&반복:\n소요시간:\n칼로리소모:")
l7.grid(column=1,row=8)

b2=Button(window,image=img1)
b2.grid(column=6,row=5,columnspan=4,rowspan=3)
l8=Label(window,text="운동명:\n횟수&반복:\n소요시간:\n칼로리소모:")
l8.grid(column=6,row=8)

b3=Button(window,image=img1)
b3.grid(column=1,row=12,columnspan=4,rowspan=3)
l9=Label(window,text="운동명:\n횟수&반복:\n소요시간:\n칼로리소모:")
l9.grid(column=1,row=15)

b4=Button(window,image=img1)
b4.grid(column=6,row=12,columnspan=4,rowspan=3)
l10=Label(window,text="운동명:\n횟수&반복:\n소요시간:\n칼로리소모:")
l10.grid(column=6,row=15)

l6=Label(window,text=" 원하는 운동 2개를 골라주세요",font=(0,20))
l6.grid(column=15,row=4)

b5=Button(window,image=img1)
b5.grid(column=12,row=5,columnspan=4,rowspan=3)
l11=Label(window,text="운동명:\n횟수&반복:\n소요시간:\n칼로리소모:")
l11.grid(column=15,row=8)

b6=Button(window,image=img1)
b6.grid(column=16,row=5,columnspan=4,rowspan=3)
l12=Label(window,text="운동명:\n횟수&반복:\n소요시간:\n칼로리소모:")
l12.grid(column=16,row=8)

l6=Label(window,text=" 원하는 운동 2개를 골라주세요",font=(0,20))
l6.grid(column=15,row=4)

l13 = Label(window, text='첫번째 운동 횟수', width=15)
l14= Label(window, text='두번째 운동 횟수', width=15)
l15 = Label(window, text='소요시간', width=15)
e13 = Entry(window)
e14 = Entry(window)
e15 = Entry(window)
l13.grid(row=15, column=15)
e13.grid(row=15, column=16)
l14.grid(row=16, column=15)
e14.grid(row=16, column=16)
l15.grid(row=17, column=15)
e15.grid(row=17, column=16)
b13 = Button(window, text='더하기', command=p1,width=10)
b13.grid(row=18, column=15, columnspan=2)


window.mainloop()
