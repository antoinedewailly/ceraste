#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os

def decompilation(path,nom):
    print "Début de la décompilation..."
    os.system("apktool d %s -o %s > /tmp/log.txt"%(path,nom))
    print "Fin de la décompilation"

def compilation(path,nom):
    print "Début de la compilation..."
    os.system("apktool b %s -o %s-new.apk > /tmp/log.txt"%(path,nom))
    print "Fin de la compilation"
