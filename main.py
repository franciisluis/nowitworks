#!/usr/bin/python
#FRANCIS E ESTER
import sys
sys.path.append("../..")

import gramatica
import erros
import lexico

with open("teste.txt", "r") as arquivo:
    data = arquivo.read()
    print("\n --- LEXER------")
    lexico.lexico(data)
    print("\n --- ERROS NO SINTATICO ---- ")
    gramatica.parser.parse(data)
