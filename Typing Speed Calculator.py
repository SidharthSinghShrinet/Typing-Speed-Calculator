from time import * 
import random as r
def mistake(partest,userinput):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=userinput[i]:
                error=error+1
        except :
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)

while True:
    ck=input("Whether you want to type or not please answer it in yes/no:")
    if ck=="yes":
        test=["My name is Sidharth Singh","Currently I am pursuing my B.Tech","My hobbies is playing online games"]
        test1=r.choice(test)
        print("                   *****************Typing Test********************")
        print(test1)
        print()
        print()
        time_1=time()
        testinput=input("Start Writing:")
        time_2=time()

        print("Speed:",speed_time(time_1,time_2,testinput),"w/sec")
        print("Error:",mistake(test1,testinput))
    elif ck=="no":
        print("Thank You! for visiting.")
        print("-----GAME OVER-----")
        break
    
    else:
        print("$--wrong input--$")
