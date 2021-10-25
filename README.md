# tarea2Compiladores
##Descripcion
Implementar un analizador sintáctico descendente recursivo o LL(1) para el lenguaje Json
simplificado.  Recibe un archivo fuente Json, y debe imprimir en pantalla si el fuente es
sintácticamente correcto o los errores encontrados en caso de existir (se adjuntan ejemplos
de fuentes correctos). En caso de error se deberá implementar la estrategia de manejo de
errores Panic Mode con sincronización y continuar el análisis.

##Analisis
Json -> element eof
element -> object | array
array -> [element-list] | []
element-list -> element A'
A' -> element A' | e
object -> {atribute-list} | {}
atribute-list -> atribute B'
B' -> atribute B' | e
atribute -> atribute-name : atribute-value
atribute-name -> string
atribute-value -> element | string | number | true | false | null

###Primero
json = {P(element)} = {{;[}
element = {P(object);P(array)}={{;[}
array = {[}
element-list = {P(element)} = {{;[}
A' = {,;e}
object = {{}
atribute-list = {P(atribute)}={string}}
B' = {,;e}
atribute = {P(atribute-name)}={string}
atribute-value{P(element);string;number;true;false;null}

###Siguiente
S(json)={$} ->{$}
element = {$;,;];}} -> {$;,;];}}
array = {$;,;];}} -> {$;,;];}}
element-list {]} -> {]}
A' = {]} -> {]}
object = {$;,;];}
atribute-list = {}}->{}}
B'={}} -> {}}
atribute = {,;}} -> {,;}}
atribute-name = {:} ->{:}
atribute-value = {,;}}->{,;}}
