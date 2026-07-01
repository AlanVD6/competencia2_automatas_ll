//ejercicio 2 
//Numero de control: 23030022

grammar resta;

root : expr EOF;
expr : EOF;

NUM : [0-9]+;
MENOS : '-';
WS : [ \t\r\n]+ -> skip;
