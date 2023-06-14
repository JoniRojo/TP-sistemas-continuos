import math
import argparse
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
    parser = argparse.ArgumentParser()
    r=3                       #tasa de crecimiento de presas en ausencia de depredadores
    a=2                       #coeficiente de depredacion
    b=1                       #tasa de crecimiento del numero de depredadores
    m=2                       #tasa de mortalidad de depredadores
    intervalInit=0  
    intervalEnd=50
    intialValueP=2
    intialValueD=2
    h=0.01
    parser.add_argument("-i", "--interval", type=float, help="Interval max. Default = 50. The sistem will also stop when the amount of preys or depredators reach less than 0.005")
    parser.add_argument("-s", "--step", type=float, help="Size of the step. Default = 0.01")
    parser.add_argument("-d", "--depredator", type=int, help="Starting amount of depredators. Default = 2")
    parser.add_argument("-p", "--prey", type=int, help="Starting amount of preys. Default 2 = 2")
    parser.add_argument("-r", type=float, help="Growth rate of prey in the absence of predators. Default = 3")
    parser.add_argument("-a", type=float, help="Predation coefficient. Default = 2")
    parser.add_argument("-b", type=float, help="Growth rate of the number of predators. Default = 1")
    parser.add_argument("-m", type=float, help="Predator mortality rate. Default = 2")

    args = parser.parse_args()

    if args.interval:
        intervalEnd=args.interval
    if args.step:
        h=args.step
    if args.depredator:
        intialValueD=args.depredator
    if args.prey:
        intialValueP=args.prey
    if args.r:
        r=args.r
    if args.a:
        a=args.a
    if args.b:
        b=args.b
    if args.m:
        m=args.m
    
    hashmapP = {intervalInit:intialValueP}
    hashmapD = {intervalInit:intialValueD}

    eulerAlgorithm(h,r,a,b,m,intervalEnd,hashmapP,hashmapD,p,d)
    # Print values
    for clave in hashmapP:
        valor= hashmapP[clave]
        print(str(clave)+" : "+str(valor))
    for clave in hashmapD:
        valor= hashmapD[clave]
        print(str(clave)+" : "+str(valor))


    fig ,(ax1, ax2) = plt.subplots(1,2)
    # 1
    ax1.plot(list(hashmapP.values()),'-',color='g', label='Preys')
    ax1.plot(list(hashmapD.values()), '-', color= 'r', label='Depredators')
    ax1.set_title('Population through time')
    ax1.set_xlabel('Simulation time')
    ax1.set_ylabel('Population')
    ax1.legend()    


    # 2
    x=hashmapP.values()
    y=hashmapD.values()
    ax2.set_title('Interaction of the number of prey and predators')
    ax2.set_xlabel('Population of depredators')
    ax2.set_ylabel('Population of preys')
    ax2.plot(x,y)
    ax2.legend() 
    fig.tight_layout()
    plt.subplot(1,2,2)
    plt.show()

if __name__ == "__main__":
    main()
