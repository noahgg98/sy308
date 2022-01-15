import random

import sys

def workhorse(bott, top, mod):

    #save nums
    modde = list()

    for i in range(0, 1001):
        #get random val
        num = random.randint(bott, top)

        modde.append(num%mod)

    probs = {item: modde.count(item)/10000 for item in modde}



    return probs


if __name__=='__main__':

    if len(sys.argv) == 4:
        probs = workhorse(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))


        print("Probabilities: ")
        print(probs)

