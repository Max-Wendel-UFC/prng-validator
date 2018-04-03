from scipy import special as sc

def getM(L):
    if (L < 128) :
        print "Tamanho muito pequeno"
        return 0
    elif (L < 6272) :
        return 8
    elif (L < 750000) :
        return 128
    else :
        return 10000

def getK(M) :
    if (M == 8) :
        return 3
    elif (M == 128) :
        return 5
    elif (M == 10000) :
        return 6

def getN(M) :
    if (M == 8) :
        return 16
    elif (M == 128) :
        return 49
    elif (M == 10000) :
        return 75

def getV(L):
    V = []
    if (L < 6272) :
        V.append(1)
        V.append(2)
        V.append(3)
        V.append(4)

    elif (L < 750000) :
        V.append(4)
        V.append(5)
        V.append(6)
        V.append(7)
        V.append(8)
        V.append(9)

    else :
        V.append(10)
        V.append(11)
        V.append(12)
        V.append(13)
        V.append(14)
        V.append(15)
        V.append(16)

    return V

def getPi(K, M) :
    Pi = []

    if (K == 3 and M < 9) :
        Pi.append(0.2148)
        Pi.append(0.3672)
        Pi.append(0.2305)
        Pi.append(0.1875)
        return Pi

    elif (K == 5 and M < 129) :
        Pi.append(0.1174)
        Pi.append(0.2430)
        Pi.append(0.2493)
        Pi.append(0.1752)
        Pi.append(0.1027)
        Pi.append(0.1124)
        return Pi

    elif (K == 5 and M < 513):
        Pi.append(0.1170)
        Pi.append(0.2460)
        Pi.append(0.2523)
        Pi.append(0.1755)
        Pi.append(0.1027)
        Pi.append(0.1124)
        return Pi

    elif (K == 5 and M < 10001):
        Pi.append(0.1307)
        Pi.append(0.2437)
        Pi.append(0.2452)
        Pi.append(0.1714)
        Pi.append(0.1002)
        Pi.append(0.1088)
        return Pi

    elif (K == 6 and M < 10001) :
        Pi.append(0.0882)
        Pi.append(0.2092)
        Pi.append(0.2483)
        Pi.append(0.1933)
        Pi.append(0.1208)
        Pi.append(0.0675)
        Pi.append(0.0727)
        return Pi

def getVi(e,M,N,K,V) :
    i = 0
    j = 0

    nu = []
    nu.append(0)
    nu.append(0)
    nu.append(0)
    nu.append(0)
    nu.append(0)
    nu.append(0)
    nu.append(0)


    while i < N :
        V_n_obs = 0
        run = 0

        while j < M:
            if e[i*M+j] == 1:
                run += 1
                if run > V_n_obs :
                    V_n_obs = run
                else :
                    run = 0
            j += 1

        if V_n_obs < V[0] :
            nu[0] += 1

        j = 0
        while j < K :
            if V_n_obs == V[j] :
                nu[j] += 1
            j += 1

        if V_n_obs > V[K] :
            nu[K] += 1

        i += 1
        j = 0

    return nu

def getX_obs(K, N, Pi, Vi) :
    i = 0
    X_obs = 0.0

    while i < K+1 :
        X_obs += ( (Vi[i] - N*Pi[i])**2 ) / N*Pi[i]
        i +=1

    return X_obs

def Igamc(a,x):
    return sc.gammaincc(a, x)

def LongestRunOfOnes(e, L) :
    M = getM(L)

    if M == 0 :
        return 0

    K = getK(M)
    N = getN(M)
    Pi = getPi(K, M)
    V = getV(L)
    Vi = getVi(e, M, N, K, V)
    X_obs = getX_obs(K, N, Pi, Vi)
    P_value = Igamc(K/2, X_obs/2)

    if P_value < 0.01:
        print "Reprovado"
    else:
        print "Aprovado"

    return P_value
