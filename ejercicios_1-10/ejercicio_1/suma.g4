//ejercicio 1 - suma 
//Numero de control: 23030022

grammar suma;

root : expr EOF;
expr : NUM (MAS NUM)*;
NUM : [0-9]+;
MAS : '+';
WS : [ \t\r\n]+ -> skip;