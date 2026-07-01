#Ejercicio 5
# Numero de control 23030022

from antlr4 import*
from ExprLexer import ExprLexer

lexer = ExprLexer (InputStream(input("? ")))
tokens = CommonTokenStream(lexer)
tokens.fill()
print (tokens)

for token in tokens.tokens:
    print ("Texto : ",token.text)
    print ("linea : ",token.line)
    print ("columna : ",token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print ("tipo : ",nombre_token)
    print ("----------------------")

