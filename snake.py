import test101
from PIL import Image
import os
os.startfile("D:\PES\python\programs\snake.jpg")
import random
print(__name__)
s={1:38,4:14,8:30,21:42,28:76,32:10,36:6,48:26,50:67,62:18,71:92,80:99,88:24,95:56,97:78}
def fun1(n):
    d=dict()
    big=0
    for m in range(1,n+1):
        d[m]=0
    print(d)
    while big<100:
        for i in range(1,n+1):
            print("player number:",i)
            z=input("Press space to play the dice :")
            if z==" ":
                a=random.randrange(1,7)
                print("Dice value is: \t",a)
                f3(a)
                d[i]=d[i]+a
            else:
                print("Invalid input your chance has been skipped!!")
            for l in range(1,n+1):
                print("player",l,"is at ",d[l])
            print()
            if d[i] in s:
                d[i]=s[d[i]]
            if d[i]>big:
                big=d[i]
            if d[i]>=100:
                print("player",i,end=" ")
                break;
        test101.f1(d)
def f3(x):
    os.startfile("D:\PES\python\programs\gif.gif")        
    if x==1:
        img1=Image.open("D:\PES\python\programs\dice1.jpg")
    elif x==2:
        img1=Image.open("D:\PES\python\programs\dice2.jpg")
    elif x==3:
        img1=Image.open("D:\PES\python\programs\dice3.jpg")
    elif x==4:
        img1=Image.open("D:\PES\python\programs\dice4.jpg")
    elif x==5:
        img1=Image.open("D:\PES\python\programs\dice5.jpg")
    elif x==6:
        img1=Image.open("D:\PES\python\programs\dice6.jpg")
    img1.show()
map1={1:(20,430),2:(65,430),3:(109,430),4:(155,430),5:(200,430),6:(246,430),7:(291,430),8:(336,430),9:(382,430),10:(428,430),11:(20,383),12:(65,383),13:(109,383),14:(155,383),15:(200,383),16:(246,383),17:(291,383),18:(336,383),19:(382,383),20:(428,383),21:(20,338),22:(65,338),23:(109,338),24:(155,338),25:(200,338),26:(246,338),27:(291,338),28:(336,338),29:(382,338),30:(428,338),31:(20,292),32:(65,292),33:(109,292),34:(155,292),35:(200,292),36:(246,292),37:(291,292),38:(336,292),39:(382,292),40:(428,292),41:(20,247),42:(65,247),43:(109,247),44:(155,247),45:(200,247),46:(246,247),47:(291,247),48:(336,247),49:(382,247),50:(428,247),51:(20,201),52:(65,201),53:(109,201),54:(155,201),55:(200,201),56:(246,201),57:(291,201),58:(336,201),59:(382,201),60:(428,201),61:(20,156),62:(65,156),63:(109,156),64:(155,156),65:(200,156),66:(246,156),67:(291,156),68:(336,156),69:(382,156),70:(428,156),71:(20,110),72:(65,110),73:(109,100),74:(155,110),75:(200,110),76:(246,110),77:(291,110),78:(336,110),79:(382,110),80:(428,110),81:(20,65),82:(65,65),83:(109,65),84:(155,65),85:(200,65),86:(246,65),87:(291,65),88:(336,65),89:(382,65),90:(428,65),91:(20,21),92:(65,21),93:(109,21),94:(155,21),95:(200,21),96:(246,21),97:(291,21),98:(336,21),99:(382,21),100:(428,21),101:(428,21),102:(428,21),103:(428,21),104:(428,21),105:(428,21),106:(428,21)}
x=int(input("Enter number of players:"))
for i in range(1,x+1):
    if i==1:
        print("Player 1 is Green in color",end="\n")
    elif i==2:
        print("Player 2 is Red in color",end="\n")
    if i==3:
        print("Player 3 is Yellow in color",end="\n")
    if i==4:
        print("Player 4 is Blue in color",end="\n")
fun1(x)
print("is the winner \n")
