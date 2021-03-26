#-*- coding:utf-8 -*-
import turtle as t
import random
t.shape('turtle')
screenX, screenY = 1280, 720
t.getscreen().screensize(screenX*1.5, screenY*1.5)  # 화면 이동
t.speed(0); t.penup(); t.hideturtle(); y1=[]; y2=[]; ladder=[]; t.tracer(0,0); start=0
count= [0 for i in range(1,9)]
def rom():
    for i in range(12):                            #12개의 계단 생성
        x=random.randint(1,7)*100
        r1=random.randint(10,490)
        r2=random.randint(10,490)
        while r1 in y1 or r1 in y2:                   #중복 검사   
            r1=random.randint(10,490)
        while r2 in y2 or r2 in y1:
            r2=random.randint(10,490)
        y1.append(r1)
        y2.append(r2)
        ladder.append([x,r1,x+100,r2]) 
        t.penup()
        t.goto(x,r1)
        t.pendown()         
        t.goto(x+100,r2)
def br():
    for i in range(1,9):                             # 8개의 다리 생성
        t.goto(i*100,500)
        t.pendown()
        t.goto(i*100,0)
        t.penup() 

br()                   
rom()
t.rt(90)

for v in range(1000,9001):
    t.goto(start,500);t.penup(); t.showturtle()
    if v%1000==0: 
        start=v/10
        if v!=1000:
            print(int(start/100)-1)
            for j in range(1,9):                              #결과값
                print(f"{j}번:{count[j-1]} ", end="")
            print()                                     #1~8번을 1000번씩 반복함
            t.goto(start,500)
            count= [0 for i in range(1,9)]
            print('='*130)

    while t.ycor()!=0:                                #거북이 이동
        t.fd(1)
        for x,y,z,w in ladder:
            if (x,y) in [t.position()]: 
                t.goto(z,w)
                
            elif (z,w) in [t.position()]:
                t.goto(x,y)

    t.penup(); t.hideturtle()
    number=int(t.xcor()/100)
    count[number-1]+=1

    y1=y2=[]; ladder=[]
    t.clear()
    br()
    rom()
