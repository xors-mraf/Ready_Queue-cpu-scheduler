import math
from time import sleep
import copy
def bubbles(lis):
    for i in range(len(lis)):
        for j in range(1,len(lis)):
               if(int(lis[j-1][1])>int(lis[j][1])):
                   temp=lis[j-1].copy()
                   lis[j-1]=lis[j].copy()
                   lis[j]=temp.copy()
    return

if __name__=='__main__':
     lis=list()
     n=int(input('hello please enter number of processes:'))
     for i in range(n):
         name=input('name of process:')
         enter_time=int(input('entering time:'))
         execute_time=int(input('execute time:'))
         lis.append([name,enter_time,execute_time])
     quantom=int(input('please enter your quantom:'))
     bubbles(lis)
     timer=0
     counter=0
     counter2=0
     ready_queue=[]
     queuelength=len(lis)
     count=0
     quantom_t=0
     sw=False
     idle=False
     while (True):


         if (counter < len(lis)):
             if (timer == lis[counter][1]):
                 ready_queue.append(copy.copy(lis[counter]))
                 counter += 1
                 if(idle==True):
                     quantom_t=quantom-2
                     idle=False
             elif (ready_queue==[]):
                 idle=True


         if (counter2 < len(ready_queue)):
           ready_queue[counter2][2] -= 1

         sleep(0.001)  # 1/QUANTOM TIME
         timer += 1

         if(counter2<len(ready_queue)):
          if (ready_queue[counter2][2] == 0):
             if(counter2==0):
                count=ready_queue[counter2][1]
             print(f'{ready_queue[counter2][0]}:({count},{timer})')
             quantom_t=quantom-1

             if (len(ready_queue) > counter2 + 1):
                 counter2 += 1
                 count = timer
             else:
                 break

          elif (quantom_t==quantom-1):
             if (counter2 == 0):
                  count = ready_queue[counter2][1]
             print(f'{ready_queue[counter2][0]}:({count},{timer})')
             ready_queue.append(copy.copy(ready_queue[counter2]))
             counter2 += 1
             count = timer


          quantom_t = (quantom_t + 1) % quantom
