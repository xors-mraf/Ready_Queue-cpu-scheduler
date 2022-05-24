###########Mahdiyar Eftekharinia###############
import math
import copy

def bubbles(lis):
    for i in range(len(lis)):
        for j in range(1,len(lis)):
               if(int(lis[j-1][1])>int(lis[j][1])):
                   temp=lis[j-1].copy()
                   lis[j-1]=lis[j].copy()
                   lis[j]=temp.copy()


def min(ready_queue):
    min=ready_queue[0]
    if(len(ready_queue)==1):
        return min
    for i in range(1,len(ready_queue)):
        if(min[2]>ready_queue[i][2]):
            min=copy.copy(ready_queue[i])
    return min

if __name__=='__main__':
    lis = list()
    n = int(input('hello please enter number of processes:'))
    for i in range(n):
        name = input('name of process:')
        enter_time = int(input('entering time:'))
        execute_time = int(input('execute time:'))
        lis.append([name, enter_time, execute_time])
    bubbles(lis)
    print(lis)
    timer=0
    counter=0
    ready_queue=[]
    while(True):
        if(counter<len(lis)):
          if(lis[counter][1]==timer):
            for i in lis[counter:]:
             if(i[1]==timer):
                ready_queue.append(i)
                counter+=1
          elif(lis[counter][1]<timer):
              for i in lis[counter:]:
                  if (i[1]<timer):
                      ready_queue.append(i)
                      counter += 1

        if not ready_queue:
            print(f'idle time for:({timer},{timer+1})')
        else:
            mini=min(ready_queue)
            print(f'process {mini[0]} excuted for:({timer},{timer+mini[2]})')
            timer+=mini[2]-1
            ready_queue.remove(mini)
        if(counter==len(lis) and ready_queue==[]):
            break
        timer+=1


