from scipy import special as sc

def getN(L, M):
    return L/M

def getPi_i(e, L, M):
    j = 0
    i = 0
    aux = 0.0
    pi = []

    while i < L:
        while j < M:
            aux += e[i]
            j += 1
            i += 1
        pi.append(aux/M)
        aux = 0.0
        j = 0

    return pi

def getSum(Pi, N):
    i = 0
    res = 0.0
    while i < N:
        res += (Pi[i] - 0.5)*(Pi[i] - 0.5)
        i += 1
    return res

def getX2_obs(Pi,M,N):
    return 4*M*getSum(Pi, N)

def Igamc(a,x):
    return sc.gammaincc(a, x)

def FrequencyBlockTest(e,L,M):
    N = getN(L,M)
    Pi = getPi_i(e, L, M)
    X2_obs = getX2_obs(Pi, M, N)
    P_value = Igamc(N/2, X2_obs/2)

    if P_value < 0.01:
        print "Reprovado"
    else:
        print "Aprovado"

    return P_value
