#Ricardo Hernández Rincón A00831818
#Isaias Alvarez Vargas A01233838
#Pedro Andres Fernandez Lopez A01235998
#Act 3.4 
#El siguiente programa es un analizador léxico para programas hechos en el lenguaje C++

#Definimos una lista con todas las palabras reservadas
from curses.ascii import isalpha


palabras_reservadas = ["auto","const","double","float","int","short","struct",
"unsigned","break","continue",
"else","for","long","signed","switch",
"void","case","default","enum","goto",
"register","sizeof","typedef","volatile","char",
"do","extern","if","return","static",
"union","while","asm","dynamic_cast","namespace","reinterpret_cast",    
"try","bool","explicit","new","static_cast","typeid","catch","false",    
"operator","template","typename","class","friend","private","this",    
"using","const_cast","inline","public","throw","virtual","delete","mutable","protected","true","wchar_t"]
#Definimos una lista con todos los operadores
operadores = ["=","+","+=","-","-=","*","*=","/","/=","%","%=","++","--",
"<",">","<=",">=","==","!=","<=>","!","&&","||",
"<<=",">>=","~","&=","|","|=","^","^=",
"(",")","[","]","{","}","->",".","->.",".*",",","::","::*",
"<?",">?",";"]
#definimos la función
def syntax_highlight(archivo_entrada,archivo_salida):
    entrada = open(archivo_entrada,"r") # el archivo de entrada es el programa escrito en C++
    salida = open(archivo_salida,"w") # en el archivo de salida es el archivo HTML se generará
    lineas = entrada.readlines() # creamos una lista con todas las líneas del archivo de entrada
    var = "" # var nos ayudará a definir cada elemento que entrará al archivo por separado
    line = "" # line será la línea que se insertará en el archivo de entrada
    # definimos el inicio y final que tendrá el documento HTML
    inicio = """<!DOCTYPE html>
    <html>
    <head>
        <link href="https://allfont.es/allfont.css?fonts=lucida-console" rel="stylesheet" type="text/css" />
        <meta charset="UTF-8">
        <title> Analizador de Sintaxis </title>
        <link rel="stylesheet" href="formato.css">
    </head>
    <body>\n"""
    final = """</body>
    </html>"""
    # antes de analizar el archivo escribimos el inicio en el archivo
    salida.write(inicio)
    # empieza el análisis
    for linea in lineas: # analiza cada elemento de las líneas
        line = "<p>" # iniciamos line como un párrafo 
        tam = len(linea) # definimos el tamaño de la línea y nuestro contador i
        i = 0
        # mientras el contador sea menor al tamaño de la línea
        while i <= tam:
            # si i es igual al tamaño, significa que toda la línea fue analizada
            if i == tam:
                # cerramos el párrafo, lo escribimos en el archivo y terminamos el ciclo
                line = line + "</p>"
                salida.write(line + "\n")
                break
            # si encuntra un símbolo # se puede tratar de un #include
            elif linea[i] == "#":
                # agrega a var el # y inicializa j como i+1, para anlizar los elementos que siguen del #
                var = var + linea[i]
                j = i+1
                # mientras j sea menor al tamaño de la línea
                while j < tam:
                    # mientras el elemento sea alfabético lo agrega a var y aumenta j
                    if linea[j].isalpha():
                        var = var + linea[j]
                        j += 1
                    # si no es alfabético
                    else:
                        # si se trata de un #include lo trata como una palabra reservada y lo agrega a la línea
                        if var == "#include":
                            var = "<span class='palabra_reservada'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                        # si no es un #include lo trata todo como un operador y lo agrega a la línea
                        else:
                            var = "<span class='operador'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                i = j # cuando termina hace que el valor de i sea igual a j
            # si encuentra un espacio
            elif linea[i] == " ": 
                # inicializa un contador y abre un ciclo while
                j = 0
                while linea[i] == " ":
                    if linea[i+1] != " ": # si el siguiente elemento es diferente de un espacio agrega el espacio a la línea
                        line = line + linea[i]
                        i += 1
                    else: # si hay más espacios aumenta ambos contadores
                        i += 1
                        j += 1
                        if j == 3: # si j llega a 3 significa que encontró una tabulación, la inserta en la línea y continúa
                            line = line + "<span class='tab'></span>"
                            break
            # si encuentra una letra
            elif linea[i].isalpha():
                # la agrega y define j como i+1
                var = var + linea[i]
                j = i+1
                # mientras j sea menor al tamaño de la línea 
                while j < tam:
                    # si j es una letra o número las agrega a var y aumenta j
                    if linea[j].isalpha() or linea[j].isnumeric():
                        var = var + linea[j]
                        j += 1
                    # si no lo es
                    else:
                        # si var está en las palabras reservadas, la clasifica como una y la agrega a la línea
                        if var in palabras_reservadas:
                            var = "<span class='palabra_reservada'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                        # si no es palabra reservada la trata como una variable y la agrega a la línea
                        else:
                            var = "<span class='variable'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break     
                i = j # cuando terminamos igualamos el valor de i a j
            # si encuntra un número
            elif linea[i].isnumeric():
                # lo agrega y inicializa j como i+1
                var = var + linea[i]
                j = i+1
                # mientras j sea menor al tamaño de la línea
                while j < tam:
                    # si es un número, un punto o una e (para los exponenciales) lo agrega a var y aumenta j
                    if linea[j].isnumeric() or linea[j] == "e" or linea[j] == ".":
                        var = var + linea[j]
                        j += 1
                    # si es una letra, lee todo mientras sea una letra o número
                    elif linea[j].isalpha():
                        while linea[j].isnumeric() or linea[j].isalpha():
                            var = var + linea[j]
                            j += 1
                        # si es diferente de letra o número clasifica la variable como error y lo agrega a la línea
                        var = "<span class='error'>" + var + "</span>"
                        line = line + var
                        var = ""
                        break
                    # si no lo es lo clasifica como un número y lo agrega a la línea
                    else:
                        var = "<span class='numero'>" + var + "</span>"
                        line = line + var
                        var = ""
                        break
                i = j # cuando terminamos igualamos i a j
            # si el elemento se encuentra en los operadores
            elif linea[i] in operadores:
                # revisa si es un símbolo de dísivisón
                if linea[i] == "/":
                    # si hay otro símbolo de división más adelante significa que es un comentario 
                    # lo agrega a la línea e iguala i al tamaño de la línea
                    if linea[i+1] == "/":
                        var = "<span class='comentario'>" + linea[i:tam-1] + "</span>"
                        line = line + var
                        var = ""
                        i = tam
                    # si no, lo trta como un símbolo de división y lo agrega a la línea
                    else:
                        var = "<span class='operador'>" + linea[i] + "</span>"
                        line = line + var
                        var = ""
                        i += 1
                # si no es un símbolo de división lo agrega a la linea como operador 
                else:
                    var = "<span class='operador'>" + linea[i] + "</span>"
                    line = line + var
                    var = ""
                    i += 1
            # si encuentra comillas
            elif linea[i] == '"':
                # lo agrega e inicializa j omo i+1
                var = var + linea[i]
                j = i+1
                # mientras j sea menor al tamaño de la línea
                while j < tam:
                    # si encuentra la comilla de cierre, agrega var como comentario
                    if linea[j] == '"':
                        var = "<span class='string'>" + var + linea[j] + "</span>"
                        j += 1
                        line = line + var
                        var = ""
                        break
                    # mientras no encuentre la comilla de cierre, agregará todo a var
                    else:
                        var = var + linea[j]
                        j += 1
                i = j # cuando terminamos igualamos i a j
            else: # si nada coincide, incrementa el contador
                i += 1
    # cuando termina de analizar las líneas, exribe el final del HTML
    salida.write(final)
    # cerramos ambos archivos
    entrada.close()
    salida.close()
    # imprimimos Fin del Programa para indicar en la terminal que hemos terminado
    print("Fin del Programa")
# mandamos llamar la función
syntax_highlight('test.txt','highlighter.html')