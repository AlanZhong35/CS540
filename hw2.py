import sys
import math
import string


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict.fromkeys(string.ascii_uppercase, 0)
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        message = f.read()
        message = message.upper().replace(" ","").replace("\n","");
        message = message.strip(); 
        for punctuation in string.punctuation:
            message = message.replace(punctuation,"") #remove punctuation
        #print(message)
        for letter in message:
            if letter in string.ascii_uppercase:
                X[letter]=X[letter]+1
        print("Q1")
        for key, value in X.items():
            print(key,value)  

    
    with open ("e.txt",encoding='utf-8') as f:
        E=dict.fromkeys(string.ascii_uppercase, 0)
        for key in E:
            E[key] = f.readline().split(" ")[1]
    with open ("s.txt",encoding='utf-8') as f:
        S=dict.fromkeys(string.ascii_uppercase, 0)
        for key in S:
            S[key] = f.readline().split(" ")[1]
    
    print("Q2")
    logAEng= X["A"]*math.log(float(E["A"]))
    logASpa=X["A"]*math.log(float(S["A"]))
    print(f"{logAEng:.4f}")
    print(f"{logASpa:.4f}")

    pEng = 0.6
    pSpa = 0.4
    eTotal = 0
    sTotal = 0
    for key,value in X.items():
        eTotal += X[key]*math.log(float(E[key]))
        sTotal += X[key]*math.log(float(S[key]))
    bigfEng = math.log(pEng)+eTotal
    bigfSpa = math.log(pSpa)+sTotal
    print("Q3")
    print(f"{bigfEng:.4f}")
    print(f"{bigfSpa:.4f}")
    if bigfSpa-bigfEng>=100:
        condEngGivenX = 0
    elif bigfSpa-bigfEng<=-100:
        condEngGivenX = 1
    else:
        condEngGivenX = 1/(1+pow(math.e,float(bigfSpa-bigfEng)))
    print("Q4")
    print(f"{condEngGivenX:.4f}")
     

    return X



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
def Q4Alternate(filename):
    pEng = 0.6
    pSpa = 0.4
    with open ("e.txt",encoding='utf-8') as f:
        E=dict.fromkeys(string.ascii_uppercase, 0)
        for key in E:
            E[key] = f.readline().split(" ")[1]
    with open ("s.txt",encoding='utf-8') as f:
        S=dict.fromkeys(string.ascii_uppercase, 0)
        for key in S:
            S[key] = f.readline().split(" ")[1]
    X = shred(filename)
    total = 0
    denom = 1
    eTimes = 1
    sTimes = 1
    for key,value in X.items():
        total += X[key]
        denom *= math.factorial(X[key])
    multinomCo = math.factorial(total)/denom
    for key, value in E.items():
        eTimes *= pow(float(value),X[key])
    for key, value in S.items():
        sTimes *= pow(float(value),X[key])
    condXGivenEng=multinomCo * eTimes
    condXGivenSpa=multinomCo * sTimes
    condEngGivenX = (condXGivenEng*pEng)/(condXGivenEng*pEng+condXGivenSpa*pSpa)
    condSpaGivenX = (condXGivenSpa*pSpa)/(condXGivenEng*pEng+condXGivenSpa*pSpa)
    print("Q2")
    print(condEngGivenX)
    print(condSpaGivenX)
def main():
     #shred("samples/letter0.txt")
     shred("letter.txt")

if __name__ == "__main__":
        main()