# Ejercicio 1
# Numero de control: 23030022

from antlr4 import *
from sumaLexer import sumaLexer

lexer = sumaLexer(InputStream(input("?")))

tokens = CommonTokenStream(lexer)
tokens.fill()

for token in tokens.tokens:
    print("Texto  : ", token.text)
    print("Linea  : ", token.line)
    print("Columna: ", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo   : ", nombre_token)
    print("----------------------")