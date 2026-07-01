//Ejercicio 8 
//Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : EOF;

ID : [a-zA-Z]+;
MAYOR : '>';
IGUAL : '=';
NUM : [0-9]+;
WS : [ \t\r\n]+ -> skip;