# Ejercicio 2
#Numero de control: 23030022

from antlr4 import*
from restaLexer import restaLexer
import sys 

#leer archivos
input_stream=FileStream(sys.argv[1])

lexer = restaLexer(input_stream)
tokens = CommonTokenStream(lexer)
tokens.fill()

for token in tokens.tokens:
    print("Texto  : ", token.text)
    print("Linea  : ", token.line)
    print("Columna: ", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo   : ", nombre_token)
    print("----------------------")