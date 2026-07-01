//Ejercicio 10
//Numero de control 23030022

grammar Expr;
root : expr EOF;
expr : EOF;

PRINT : 'print';
CADENA : '"' ~["\r\n]* '"';
PARENTESOS_AB : '(';
PARENTESOS_CI : ')';
PUNTO_COMA :';';
WS : [ \t\r\n]+ -> skip;
