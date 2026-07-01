//Ejercicio 9 
//Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : EOF;

IF : 'if';
PARENTESIS_AB: '(';
ID :  [a-zA-Z]+;
MAYOR : '>';
NUM : [0-9]+;
PARENTESIS_CE: ')';
WS : [ \t\r\n]+ -> skip;