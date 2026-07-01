// Ejercicio 3
// Numero de control 23030022

grammar declaracion;

root : expr EOF;
expr : EOF;

ID: [a-zA-Z]+ ;
IGUAL : '=' ;
NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;