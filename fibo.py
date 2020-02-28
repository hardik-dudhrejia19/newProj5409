import math
import time
#from matplotlib import pyplot as plt
#import numpy as np


def fibonacci(n):
    if(n == 0 or n == 1):
        return [0]
    else:
        ans_list = []
        a, b = 0, 1
        ans_list.append(a)
        ans_list.append(b)
        for i in range(2,n):
            c = a + b
            ans_list.append(c)
            a, b = b, c
        return ans_list

fp = open("input.txt","r")
lines = fp.readlines()
whole = "Request-ID\tTime\tN\tResult\n\n"
time_list = []
value_list = []
for i in lines:
    value_list.append(int(i))
    request = "Request_{}".format(int(i))

    tic = time.time()
    answer = fibonacci(int(i))
    toc  = time.time()
    time_list.append(toc - tic)

    answer_str = ""
    for i in range(len(answer)):
        if(i == len(answer) -1):
            answer_str += str(answer[i])
        else:
            answer_str+= str(answer[i]) + ","
    whole += request + "\t" + str(toc - tic) + "\t" + str(int(i)) + "\t" + answer_str + "\n"
out = open("fibonacciOutput.txt", "w")
out.write(whole)
fp.close()
out.close()
fibo = []
for i in range(len(time_list)):
    l = []
    l.append(value_list[i])
    l.append(time_list[i])
    fibo.append(l)
fibo.sort(key=lambda fibo : fibo[0])
list0 = []
list1 = []
for i in fibo:
    list0.append(i[0])
    list1.append(i[1])
#fibo_final = np.array(fibo)
#plt.title("Time v/s N graph for calculating fibonacci series")
#plt.xlabel("Number (N)")
#plt.ylabel("Time in seconds (s)")
#plt.plot(fibo_final[:,0],fibo_final[:,1],"r-")
#plt.savefig("fiboGraph.png")
