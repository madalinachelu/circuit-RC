import math
from matplotlib import pyplot as plt

    # R = 20 * pow(10, -1)  # rezistenta
    # C = 72 * pow(10, -4)  # condensatorul

def calculeazaVout(R,C,suf):
    E = 5 # tensiunea E este de 5 volti
    T = 1000 #TIMP
    # R = 7 * pow(10, -1)  # rezistenta
    # C = 692 * pow(10, -4)  # condensatorul
    tau = R * C
    print("3*tau = ",3*tau)
    print("T = ",T)
    #print(tau * 1000)
    v = [0] * 1000 #vector cu 1000 de elemente de 0
    t = [0] * 1000
    #print(v)

    for i in range(0,1000):
        t[i] = (i + 1 )/1000.0

    for j in range(0,1000):
        u = (j + 1) % 300 + 1
        #
        if u > 150:
            v[j] = E * math.exp(-t[u] / tau)
        else:
            v[j] = E - E * math.exp(-t[u] / tau)

    print(str(len(t)) + " " + str(len(v)))
    plt.plot(t,v)
    plt.xlabel("Timp")
    plt.ylabel("Tensiune")
    plt.title('Circuit RC')
    plt.show()
    fisier_v = "fisier_v" + "_" + suf
    fisier_t = "fisier_t" + "_" + suf
    scriere(v,fisier_v)
    scriere(t,fisier_t)

def scriere(vector, fisier):
    file = open(fisier, "w")
    for element in vector:
        file.write(str(element) + " ")
    file.close()


def main(param):
    #
    if param == 1:
        print("Cazul 1 3*tau<T")
        R = 7 * pow(10, -1)  # rezistenta
        C = 692 * pow(10, -4)  # condensatorul
        calculeazaVout(R,C,"caz_1")
    else:
        print("Cazul 1 3*tau>T")
        R = 60 * pow(10,3)  # rezistenta
        C = 8 * pow(10, -6)  # condensatorul

    #    R = 9 * pow(1,-1)  # rezistenta
    #    C = 6 * pow(2, +1)  # condensatorul

        calculeazaVout(R,C,"caz_2")

#--------------------------------------------------------------------------
#Pentru a plota primul caz se lasa decomentata doar linia main1
#Pentru a plota primul caz se lasa decomentata doar linia main2
# Caz 1
main(1)
# Caz 2
main(2)
