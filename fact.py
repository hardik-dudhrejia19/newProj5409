import math
import time
#from matplotlib import pyplot as plt
#import numpy as np


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        prod = 1
        for i in range(n, 0, -1):
            prod = prod * i
        return prod


fp = open("input.txt", "r")
lines = fp.readlines()
time_list = []
value_list = []
whole = "Request-ID\tTime\tN\tResult\n\n"
for i in lines:
    value_list.append(int(i))
    request = "Request_{}".format(int(i))

    tic = time.time()
    ans = factorial(int(i))
    toc = time.time()

    time_list.append(toc - tic)

    whole += request + "\t" + str(toc - tic) + "\t" + str(int(i)) + "\t" + str(ans) + "\n"
out = open("factorialOutput.txt", "w")
out.write(whole)
fp.close()
out.close()
fact_final = []
for i in range(len(time_list)):
    l = []
    l.append(value_list[i])
    l.append(time_list[i])
    fact_final.append(l)
fact_final.sort(key=lambda fact_final: fact_final[0])
list0 = []
list1 = []
for i in fact_final:
    list0.append(i[0])
    list1.append(i[1])
#plt.title("Time v/s N graph for calculating factorial")
#plt.xlabel("Number (N)")
#plt.ylabel("Time in seconds (s)")
#plt.plot(list0, list1, "b-")
#plt.show()
#plt.savefig("factGraph.png")
