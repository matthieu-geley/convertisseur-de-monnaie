def Conv():

    dollar = 1.08
    livre = 0.89
    i = 1
    j = 0
    valeur = 50

    if i == j:
        print("erreur: conversion inutile, la même devise est sélectionnée en entrée et en sortie.")
    if i == 0:
        if j == 1:
            print(float(valeur) * float(dollar))
        elif j == 2:
            print(float(valeur) * float(livre))
    elif i == 1:
        if j == 0:
            print(float(valeur) / float(dollar))
        elif j == 2:
            print(float(valeur) * float(livre))
    elif i == 2:
        if j == 0:
            print(float(valeur) / float(livre))
        elif j == 1:
            print(float(valeur) * float(dollar))

Conv()