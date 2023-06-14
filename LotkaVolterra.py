import math

import matplotlib.pyplot as plt
import numpy as np


def eulerCalculus (h,func,hashmap,t):
    return round((hashmap[round((t),5)]+h*func),5)

def eulerAlgorithm(h,r,a,b,m,intervalEnd,hashmapP,hashmapD,funcp,funcd):
    i=h
    while (i <=intervalEnd and (hashmapP[round((i-h),5)]> 0.005 or hashmapD[round((i-h),5)]> 0.005)):
        hashmapP[i] = eulerCalculus(h,funcp(r,a,(i-h),hashmapP,hashmapD),hashmapP,(i-h))
        hashmapD[i] = eulerCalculus(h,funcd(b,m,(i-h),hashmapP,hashmapD),hashmapD,(i-h))
        i=round((i+h),5)
    return


def p(r,a,t,hashmapP,hashmapD):
    return round((r*hashmapP[round(t,5)]-a*hashmapP[round((t),5)]*hashmapD[round((t),5)]),5)

def d(b,m,t,hashmapP,hashmapD):
    return round((b*hashmapP[round((t),5)]*hashmapD[round((t),5)]-m*hashmapD[round((t),5)]),5)

def main():
    r=3                       #tasa de crecimiento de presas en ausencia de depredadores
    a=2                       #coeficiente de depredacion
    b=1                       #tasa de cercimiento del numero de depredadores
    m=2                       #tasa de mortalidad de depredadores
    intervalInit=0  
    intervalEnd=50
    intialValueP=2
    intialValueD=2
    hashmapP = {intervalInit:intialValueP}
    hashmapD = {intervalInit:intialValueD}
    h=0.01
    eulerAlgorithm(h,r,a,b,m,intervalEnd,hashmapP,hashmapD,p,d)
    
    # Print values
    for clave in hashmapP:
        valor= hashmapP[clave]
        print(str(clave)+" : "+str(valor))
    for clave in hashmapD:
        valor= hashmapD[clave]
        print(str(clave)+" : "+str(valor))

    # 1
    plt.plot(list(hashmapP.values()),'-',color='g', label='Preys')
    plt.plot(list(hashmapD.values()), '-', color= 'r', label='Depredators')
    plt.title('Population through time')
    plt.xlabel('Simulation time')
    plt.ylabel('Population')
    plt.legend()    
    plt.show()

    # 2
    # x=hashmapP.values()
    # y=hashmapD.values()
    # plt.title('Interaction of the number of prey and predators')
    # plt.xlabel('Population of depredators')
    # plt.ylabel('Population of preys')
    # plt.plot(x,y)
    # plt.legend() 
    # plt.show()


if __name__ == "__main__":
    main()
