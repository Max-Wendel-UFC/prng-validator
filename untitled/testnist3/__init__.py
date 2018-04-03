import math

def getPi(e, L):
    i = 0
    aux = 0.0

    while i < L:
        aux += e[i]
        i += 1

    return aux/L

def get_t(Pi, L):
    return 2 / math.sqrt(L)

def get_P_variance(Pi):
    return abs(Pi - 0.5)

def getVn_obs(e,L):
    j = 0
    Vn = 0

    while j < L-1:
        if e[j] == e[j+1]:
            Vn += 0
        else:
            Vn += 1
        j += 1

    return Vn

def getP_value(Vn_obs, L, Pi):
    return math.erfc((abs(Vn_obs - 2*L*Pi*(1-Pi))) / (2 * math.sqrt(2 * L * Pi * (1 - Pi))))

def run(e, L):
    Pi = getPi(e, L)
    P_variance = get_P_variance(Pi)
    t = get_t(Pi, L)

    if P_variance > t:
        print "ERRO! Try test1 again."
        print Pi
        print P_variance
        print t
        return

    Vn_obs = getVn_obs(e, L)
    P_value = getP_value(Vn_obs, L, Pi)

    if P_value < 0.01:
        print "Reprovado"
    else:
        print "Aprovado"

    return  P_value