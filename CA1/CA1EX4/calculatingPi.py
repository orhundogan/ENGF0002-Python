# Orhun Dogan
# October 6th 2020
# This program computes an approximation of π

import random
import math

def radius(x,y):
    return math.sqrt(abs(x-0.5)**2 + abs(y-0.5)**2)

def check_precision(precision,pi_list):
    alpha=10000
    if len(pi_list)<alpha:
        return False
    else:
        for i in range(len(pi_list)-1,len(pi_list)-alpha,-1):
            a = int(pi_list[i]*10**precision)
            b = int(pi_list[i-1]*10**precision)
            if a!=b:
                return False
            
        return True

def estimate_pi(precision):
    
    nhits=0
    ntotal=0
    pi_list=[]

    while True :
        x = random.random()
        y = random.random()
        if radius(x,y)<=0.5:
            nhits+=1            
        ntotal+=1
        
        pi_calculated = 4* nhits/ntotal
        pi_list.append(pi_calculated)
        
        if check_precision(precision,pi_list)==True:
            return pi_calculated
    



print(estimate_pi(3))
print("c")
