import tabla_simbolos as t
import tarea_compiladores as lexer
ARCHIVO_ENTRADA = 'prueba.txt'
ARCHIVO_SALIDA = 'salida.txt'
EOF = ''
token = '' #declaramos como variable global
linea = 1
cadena = ''
posicion = 0
lista_errores = []
def main():
    tabla = t.TablaSimbolos()

    with open(ARCHIVO_ENTRADA) as fichero:
        try:
            cadena = lexer.procesar_fichero(fichero,tabla)
            print(cadena +"\n longitud = "+ str(len(cadena)))
            analizador_sintactico(cadena)
        except Exception as e:
            print(e)
    fichero.close()


def analizador_sintactico(dato):
    global cadena
    cadena = dato
    get_token()
    json()

def match(token_esperado) :
    if (token == token_esperado) : # aqui se compara con el token actual
        print ("hice match con " + token)
        get_token()
        if (token == '') :
            get_token()
    else :
        raise Exception ('ha ocurrido un error se esperaba ----> ' + token_esperado)

#aqui se actualiza el valor del token por el siguiente que viene en el fichero
def get_token():

    global token #aqui le decimos que queremos utilizar la variable global creada
    global linea
    global cadena
    global posicion
    token = ''
    caracter =''
    while (True and posicion <len(cadena)) :
        if(caracter!='\t'):
            token += caracter

        caracter = cadena[posicion]
        posicion+=1
        if (caracter == '' or caracter == '\n' or caracter == ' ') :
            break

    if (token not in ['','\n',' ','\t']) :
        print (token)

def json() :

    element ()

def element () :

    if (token == 'L_LLAVE') :
        object()
    elif (token == 'L_CORCHETE'):
        array ()
    else:
        raise Exception ('ha ocurrido un error en la linea ' + str(linea))

def object ():
    try:
        global token

        match ('L_LLAVE')
        if (token == 'R_LLAVE') :
            match ('R_LLAVE')
        else :
            atribute_list()
            match ('R_LLAVE')
    except Exception as error:
        print ("ha ocurrido un error en object() en la linea  "+ str(posicion)+ str(error))

def array ():
    try:
            global token
            match ('L_CORCHETE')
            if (token == 'R_CORCHETE') :
                # print ("es una lista vacia")
                match ('R_CORCHETE')
            else :
                element_list()
                match ('R_CORCHETE')
    except:
        print ("ha ocurrido un error en array () en la linea "+ str(linea))

def element_list() :
    try:
        element()
        A_prima()
    except:
        print ("ha ocurrido un error en element_list() en la linea "+ str(linea))

def A_prima():

    try:
        if (token == 'COMA') :
            match('COMA')
            element()
            A_prima()
        else :
            print ("lista vacia")
            return #se cumple con el caso base
    except:
        print ("ha ocurrido un error en A_prima() en la linea "+ str(linea))

def atribute_list() :
    try :
        atribute()
        B_prima()
    except:
        print ("ha ocurrido un error en atribute_list() en la linea "+ str(linea))

def atribute ():

        atribute_name()
        match ('DOS_PUNTOS')
        atribute_value()

def B_prima():

    try :
        if (token == 'COMA'):
            match('COMA')
            atribute()
            B_prima()
        else :
            return # se cumple con el caso base
    except :
        print ("ha ocurrido un error en B_prima() en la linea "+ str(linea))

def atribute_name ():

    try :
        match ('STRING')
    except:
        print ("ha ocurrido un error en atribute_name() en la linea "+ str(linea))

def atribute_value():

    if (token == 'L_CORCHETE' or token == 'L_LLAVE') :
        element()
    elif (token == 'STRING'):
        match('STRING')
    elif (token == 'NUMBER'):
        match('NUMBER')
    elif (token == 'PR_FALSE'):
        match('PR_FALSE')
    elif (token == 'PR_TRUE'):
        match('PR_TRUE')
    elif (token == 'PR_NULL'):
        match('PR_NULL')
    else:
        raise Exception ('ha ocurrido un error en atribute_value')


if (__name__ == '__main__') :
    # get_token() #tomamos el primer token del archivo
    # json()
    # fichero.close()
    main()
