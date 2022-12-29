import sys
import math
import random


def isPrimeNum(ispnum):
    print("isPrimeNum")
    multiples = []

    for x in range(1, ispnum+1):
        for y in range(ispnum, 0, -1):
            if x > y:
                break
            if x*y == ispnum:
                if (x not in multiples) and (y not in multiples):
                    multiples.append(x)
                    multiples.append(y)
                    # print("numbers: %d, %d" %(x,y))
    if len(multiples) == 2:
        return True
    else:
        return False


def isCoprime(num1, num2):
    print("isCoprime")
    num1Factors = FindAllFactors(num1)
    num2Factors = FindAllFactors(num2)

    for x in range(len(num1Factors)):
        if num1Factors[x] in num2Factors:
            return False
    return True


def hasPrimeFactors(facList):
    print("hasPrimeFactors")
    for x in range(len(facList)):
        if not isPrimeNum(facList[x]):
            return False
    return True


def FindFactors(num):
    print("FindFactors")
    multiples = []

    for x in range(2, num):
        for y in range(num, 1, -1):
            if x * y == num:
                if (x not in multiples) and (y not in multiples):
                    multiples.append(x)
                    multiples.append(y)

    multiples.sort()
    return multiples


def FindAllFactors(num):
    print("FindAllFactors")
    multiples = []

    for x in range(2, num):
        for y in range(num, 1, -1):
            if x * y == num:
                if (x not in multiples) and (y not in multiples):
                    if not isPrimeNum(x):
                        newFactors = FindFactors(x)
                        for z in range(len(newFactors)):
                            if not newFactors[z] in multiples:
                                multiples.append(x)
                    else:
                        multiples.append(x)
                    if not isPrimeNum(y):
                        newFactors = FindFactors(y)
                        for z in range(len(newFactors)):
                            if not newFactors[z] in multiples:
                                multiples.append(y)
                    else:
                        multiples.append(y)
    multiples.sort()
    return multiples


def hasEvens(numList):
    print("hasEvens")
    for x in numList:
        if x % 2 == 0:
            print("EVENS HERE: %d" %x)
            return True
    return False


def FindCandidate(candi, N, r):
    print("FindCandidate")
    # Randomly pick candidate and check its multiples for 1 < e < r and co prime with N and r
    # Find e and d
    while True:
        pick = random.choice(candi)
        print(pick)
        pickFactors = FindAllFactors(pick)
        # Remove Prime Candidates
        if isPrimeNum(pick):
            # print("Is Prime Num")
            # print(pick)
            candi.remove(pick)
            continue
        # check if single factor
        elif len(pickFactors) > 2:
            candi.remove(pick)
            continue
        # check for 1 < e < r
        elif not (1 < pickFactors[0] < r or 1 < pickFactors[1] < r):
            candi.remove(pick)
            continue
        # check if co prime with N and r
        elif not (isCoprime(pick, N) and isCoprime(pick, r)):
            candi.remove(pick)
            continue
        # print(pick)
        break

    return pick


def KeyGen(p,q):
    print("KeyGen")
    # Get N and R for later
    n = p * q
    r = (p - 1) * (q - 1)
    candidates = []
    # Retrieve candidates for (1 mod r)
    for a in range(1, 11):
        candidates.append((a * r) + 1)

    print(candidates)
    choice = FindCandidate(candidates, n, r)
    choiceFactors = FindFactors(choice)
    # print(choiceFactors)

    return [choiceFactors[0], n], [choiceFactors[1], n]


if __name__ == '__main__':
    # print(FindFactors(1161))
    print(FindAllFactors(55))

    # Ask for first prime number and check if prime
    while True:
        firstPrimeNum = int(input("Enter First Prime Number: "))
        if isPrimeNum(firstPrimeNum):
            break
        else:
            print("This is not a prime number, please enter a prime number")
    # Ask for second prime number and check if prime
    while True:
        secondPrimeNum = int(input("Enter Second Prime Number: "))
        if isPrimeNum(secondPrimeNum):
            break
        else:
            print("This is not a prime number, please enter a prime number")

    print("Prime numbers are: %d, %d" % (firstPrimeNum, secondPrimeNum))

    #print(FindFactors(12))
    # Generate Key Pairs
    PubKey, PrivKey = KeyGen(firstPrimeNum, secondPrimeNum)
    print("Public Key is:", PubKey)
    print("Private Key is:", PrivKey)
