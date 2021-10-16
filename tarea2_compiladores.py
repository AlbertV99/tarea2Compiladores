ARCHIVO_SALIDA = 'salida.txt'
EOF = ''
fichero = open (ARCHIVO_SALIDA)
token = '' #declaramos como variable global

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
    token = ''
    caracter =''
    while (True) :
        token += caracter
        caracter = fichero.readline(1)
        if (caracter == '\t') :
            while (True) :
                caracter = fichero.readline(1)
                if (caracter != '\t'):
                    break
        elif (caracter == '' or caracter == '\n' or caracter == ' ') :
            break
    print (token)

def json() :

    element ()


def element () :

    if (token == 'L_LLAVE') :
        object ()
    elif (token == 'L_CORCHETE'):
        array ()
    else:
        raise Exception ('ha ocurrido un error')

def object ():
    try:
        match ('L_LLAVE')
        if (token == 'R_LLAVE'):
            match ('R_LLAVE')
        else :
            atribute_list()
            match ('R_LLAVE')
    except :
        print ("ha ocurrido un error en object()")

def array ():
    try:
        match ('L_CORCHETE')
        if (token == 'R_CORCHETE'):
            match ('R_CORCHETE')
        else :
            element_list()
            match ('R_CORCHETE')
    except:
        print ("ha ocurrido un error en array ()")


def element_list() :
    try:
        element()
        A_prima()
    except:
        print ("ha ocurrido un error en element_list()")

def A_prima():

    try:
        if (token == 'COMA') :
            match('COMA')
            element()
            A_prima()
        else :
            return #se cumple con el caso base
    except:
        print ("ha ocurrido un error en A_prima()")

def atribute_list() :
    try :
        atribute()
        B_prima()
    except:
        print ("ha ocurrido un error en atribute_list()")

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
        print ("ha ocurrido un error en B_prima()")

def atribute_name ():

    try :
        match ('STRING')
    except:
        print ("ha ocurrido un error en atribute_name()")

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
    get_token() #tomamos el primer token del archivo
    json()
    fichero.close()
