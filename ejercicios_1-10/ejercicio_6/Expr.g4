//Ejercicio 6
// Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : EOF;

INT : 'int';
ID : [a-zA-Z]+;
IGUAL : '=';
NUM : [0-9]+;
WS : [ \t\r\n]+ -> skip ;
