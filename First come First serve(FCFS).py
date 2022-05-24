
########## mahdiyar eftekharinia###########

import math
from time import sleep
def bubbles(lis):
    for i in range(len(lis)):
        for j in range(1,len(lis)):
               if(int(lis[j-1][1])>int(lis[j][1])):
                   temp=lis[j-1].copy()
                   lis[j-1]=lis[j].copy()
                   lis[j]=temp.copy()
    return lis

if __name__=='__main__':
     lis=list()
     n=int(input('hello please enter number of processes:'))
     for i in range(n):
         name=input('name of process:')
         enter_time=int(input('entering time:'))
         execute_time=int(input('execute time:'))
         lis.append([name,enter_time,execute_time])
     res=bubbles(lis)
     timer=0
     start=0
     while (True):
      if(lis[0][2]==0):
          print(f'process {lis[0][0]} excuted for:({start},{timer})')
          lis.pop(0)
          start=timer
      else:
          lis[0][2]-=1
      if not lis:
          break
      sleep(0.001) # (1/Quantom) time slice this can millisseconds or seconds
      timer+=1

