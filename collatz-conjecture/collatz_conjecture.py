
def getCollatzConjecture(curr:int, maxiter:int=200)->int:
    count = 0
    while count<maxiter:
        next = 0 
        if (curr % 2) != 0: #odds
            next = (curr*3)+1
        else:
            next = curr//2

        if next == 1:
            return next
        else:        
            yield next

        curr = next
        count+=1

def getCollatzConjectureList(n:int, maxitr:int)->list:
    path = []
    for j in getCollatzConjecture(n, maxitr):
        path += [j]
    path+=[1]
    return path


if __name__ == "__main__":
    import sys

    if len(sys.argv)<2:
        print("Usage: python3 collatz_conjecture.py <start_seed> <end_seed> <interval> <maaxiter>")
        print(" plots the paths of collatz conjectures of seeds starting from 'start_seed'(default=1)\n till 'end_seed'(default=10) incrementing seed by `increment`(default=1)")
        print(" 'maxiter'(default = 200) sets iteration limit of path calculation.\n ALL ARGUMENTS ARE OPTIONAL!")
        print("\nUsing default values...\n")

    # defaults
    start_seed = 1
    end_seed = 10
    increment = 1
    maxitr = 200

    if len(sys.argv) >= 2:
        start_seed = int(sys.argv[1])
    if len(sys.argv) >= 3:
        end_seed = int(sys.argv[2])
    if len(sys.argv) >= 4:
        increment = int(sys.argv[3])
    if len(sys.argv) >= 5:
        maxitr = int(sys.argv[4])

    # importing the required module
    import matplotlib.pyplot as plt
    import numpy as np
    plt.style.use('classic')

    print(sys.argv)
    
    print('start_seed: '+str(start_seed))
    print('end_seed  : '+str(end_seed))
    print('increment : '+str(increment))


    print('-'*50)
    print('| seed\t|')
    print('-'*50)
    for seed in range(start_seed, end_seed, increment):
        
        print(seed, end='\t| ')
        seed_path = getCollatzConjectureList(seed, maxitr)
        print(seed_path)
        
        x = list(range(len(seed_path)))
        plt.plot(x, seed_path, '*-', label=str(seed))
        plt.legend(loc="upper right")
    print('-'*50)
    plt.show()