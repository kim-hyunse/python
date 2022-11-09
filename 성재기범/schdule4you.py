import schedule
import time

now = time
print("현재 :",now.strftime('%Y-%m-%d %H:%M:%S'))

def job_monday():
    print("공전응 들을 시간")
    schedule.every().monday.at("8:50").do(job_monday)
    
def job_tuesday():
    print("College English 들을 시간")
    schedule.every().tuesday.at("10:50").do(job_tuesday)
    
def job_wednesday():
    print("과학기술글쓰기 들을 시간")
    schedule.every().wednesday.at("8:50").do(job_wednesday)
    
def job_wednesday2():
    print("물리학및실험2 들을 시간")
    schedule.every().wednesday.at("12:50").do(job_wednesday2)
    
def job_thursday():
    print("수학2 들을 시간")
    schedule.every().thursday.at("8:50").do(job_thursday)
    
def job_thursday2():
    print("화학및실험1 들을 시간")
    schedule.every().thursday.at("12:50").do(job_thursday2)

def job_friday():
    print("미래형자동차및디자인 들을 시간")
    schedule.every().friday.at("8:50").do(job_friday)

def job_monday2():
    print("수학2 영상 볼 시간")
    schedule.every().monday.at("00:01").do(job_monday2)

def job_thursday3():
    print("화학및및실험1 영상 볼 시간")
    schedule.every().thursday.at("17:00").do(job_thursday3)
    
def job_friday2():
    print("응용프로그래밍 영상 볼 시간")
    schedule.every().friday.at("00:01").do(job_friday2)
