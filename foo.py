primeNum = "2357111317192329313741434753596167717379838997101103107109113127131137139149151157163167173179181191193197199211223227229233239241251257263269271277281283293307311313317331337347349353359367373379383389397401409419421431433439443449457461463467479487491499503509521523541547557563569571577587593599601607613617619631641643647653659661673677683691701709719727733739743751757761769773787797809811821823827829839853857859863877881883887907911919929937941947953967971977983991997"


def isPrimeNum(ispnum):
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


def GetAllPrime():
    PrimeNumbers = ""
    x = 2
    while len(PrimeNumbers) < 10000:
        if isPrimeNum(x):
            PrimeNumbers = PrimeNumbers + str(x)
            # print(PrimeNumbers)
        x = 1 + x
    print(PrimeNumbers)


def solution(i):
    # Your code here
    num = ""
    for x in range(5):
        num = num + primeNum[i+x]
    return num

if __name__ == '__main__':
    GetAllPrime()
    print(len(primeNum))
    print(solution(55))