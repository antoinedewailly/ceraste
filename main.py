#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import apk

#unPath = input("Entrez le path de l'apk\n")
#unNom = input("Entrez le nom du dossier\n")
unPath="/home/toto/Documents/GIT/baptiste.apk"
unNom="bap"

unDossier="/home/toto/Documents/GIT/ceraste/bap/"


#apk.decompilation(unPath,unNom)
apk.compilation(unDossier,unNom)
