import testnist1 as t1
import testnist3 as t3
import testnist2 as t2
import testnist4 as t4
import testnist6 as t6

ref_arq = open("/home/max/Artigo/Amostra_1/data.e","r")
L = 1000
i = 0
e = []
while i < L:
    aux = ref_arq.read(1)
    if aux == '0':
        e.append(0)
    else:
        e.append(1)

    i=i+1

print "Resultado do teste 1: "
print t1.run(e,100)
#print "Resultado do teste 2: "
#print t2.FrequencyBlockTest(e,100,20)
#print "Resultado do teste 3: "
#print t3.run(e,100)
#print "Resultado do teste 4: "
#print  t4.LongestRunOfOnes(e,128)
#print "Resultado do teste 6: "
#print t6.DiscreteFourierTransform(e,1101)

