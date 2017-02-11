# -*- coding: utf-8 -*-
print "Pozdravljen, sem Cortana in pretvarjam kilometre v milje"
vnos = raw_input("Prosim vnesite število kilometrov: ")
if len(vnos)> 0 and vnos.isdigit():
    kilometri = int(vnos)
    kilometri_v_milje = kilometri * 0.621371192
    print kilometri_v_milje
    while True:
        n = raw_input("Bi želeli opraviti še eno pretvorbo?(da/ne): ")
        n = n.lower()
        if n == "da":
            vnos2 = raw_input("Prosim vnesite število kilometrov: ")
            if len(vnos2)> 0 and vnos2.isdigit():
                kilometri2 = int(vnos2)
                kilometri_v_milje2 = kilometri2 * 0.621371192
                print kilometri_v_milje2
            else:
                print ("Prosim vnesite samo številke")
        else:
            print ("Hvala, ker ste uporabljali naš pretvornik!")
            break
else:
    print ("Prosim vnesite samo številke")