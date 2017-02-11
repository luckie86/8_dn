# -*- coding: utf-8 -*-
print "Pozdravljen uporabnik, sem Cortana in pretvarjam tekst z velikimi črkami v tekst z malimi črkami."
vnesi_string = raw_input("Prosim vnesite tekst: ")
if len(vnesi_string) > 0:
    odstrani_presledke = " ".join(vnesi_string.split())
    pretvorjen_string = odstrani_presledke.lower()
    print pretvorjen_string
else:
    print ("Niste vnesli teksta")