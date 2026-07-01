//Ejercicio 6
// Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : EOF;

NUM : [0-9]+;
MAS : '+';
POR : '*';
WS : [ \t\r\n]+ -> skip;
