#   Tower of Hanoi with graphic using Turtle

from hmac import trans_36
from turtle import *

class Disc(Turtle):
    def __init__(self,n):
        Turtle.__init__(self,shape='square',visible=False)
        self.pu()
        self.shapesize(1.5,n*1.5,2)
        self.fillcolor(n/6,0,1-n/6.0)
        self.st()

class Tower(list):
    def __init__(self,x):
        self.x=x

    def push(self,d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
        
    def pop(self):
        d=list.pop(self)
        d.sety(150)
        return d
    
def hanoi(n,from_, with_, to_):
        if n>0:
            hanoi(n-1,from_,to_,with_)
            to_.push(from_.pop())
            hanoi(n-1,with_,from_,to_)

def play():
        onkey(None,'space')
        clear()
        try:
            hanoi(noofdisc,t1,t2,t3)
        except Terminator:
            pass

def main():
        global t1,t2,t3
        global noofdisc
        noofdisc = int(input('Enter total no. of disc : ')) 

        ht();
        penup();
        goto(0,-225)
        t1=Tower(-250)
        t2=Tower(0)
        t3=Tower(250)

        for i in range(noofdisc,0,-1):
            t1.push(Disc(i))
        write('Press Spacebar to start the game :',align='center',font=('Courier',16,'bold'))
        onkey(play,'space')
        listen()

if __name__=='__main__':
        msg=main()
        mainloop()
    