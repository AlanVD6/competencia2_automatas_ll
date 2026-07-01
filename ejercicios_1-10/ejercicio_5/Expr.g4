// Ejercicio 5
// Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : EOF;

PRINT : 'print';
CADENA : '"'~["\r\n]*'"' ;
WS : [ \t\r\n]+ -> skip ;
