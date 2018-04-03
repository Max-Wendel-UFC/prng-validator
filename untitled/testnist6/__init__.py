import math
import numpy.fft as np

def getX(e, L):
    i = 0
    X = []

    while i < L:
        if e[i] == 0:
            X.append(-1)
        else:
            X.append(1)
        i += 1

    return X

def DFT(X):
    return np.fft(X)

def S_line(S) :
    n = len(S)
    S_line = []
    i = 0

    while i < (n/2) :
        S_line.append(abs(S[i]))
        i += 1

    return S_line

def getT(n) :
    return math.sqrt(math.log(20.0, 2) * n)

def getPeaks(M,T):
    n = len(M)
    count = 0.0
    i = 0
    while i < n :
        if M[i] < T :
            count += 1.0
        i += 1

    return count

def DiscreteFourierTransform(e, n):
    X = getX(e, n)
    S = DFT(X)
    M = S_line(S)
    T = getT(n)
    N0 = 0.95 * (n/2)
    N1 = getPeaks(M,T)

    if N0 > N1:
        N = N0 - N1
    else :
        N = N1 - N0

    d = math.sqrt((N)/math.sqrt((n*0.95*0.05)/4))

    P_value = math.erfc(abs(d) / math.sqrt(2))

    if P_value < 0.01:
        print "Reprovado"
    else:
        print "Aprovado"

    return P_value