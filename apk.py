#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os

def decompilation(path,nom):
    os.system("apktool d %s -o %s > log.txt"%(path,nom))
