#Ejercicio 10
#numero de control 23030022

from antlr4 import *
from ExprLexer import ExprLexer

Lexer = ExprLexer(InputStream(input("? ")))
tokens = CommonTokenStream(Lexer)
tokens.fill()
print(tokens)

for token in tokens.tokens:
    print("Texto : ", token.text)
    print("linea : ", token.line)
    print("columna : ", token.column)
    nombre_token = Lexer.symbolicNames[token.type]
    print("tipo : ", nombre_token)
    print("----------------------")