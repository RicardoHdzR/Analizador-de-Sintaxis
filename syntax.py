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

operadores = ["=","+","+=","-","-=","*","*=","/","/=","%","%=","++","--",
"<",">","<=",">=","==","!=","<=>","!","&&","||",
"<<=",">>=","~","&=","|","|=","^","^=",
"(",")","[","]","{","}","->",".","->.",".*",",","::","::*",
"<?",">?",";"]

def syntax_highlight(archivo_entrada,archivo_salida):
    entrada = open(archivo_entrada,"r")
    salida = open(archivo_salida,"w")
    lineas = entrada.readlines()
    var = ""
    line = ""
    #contador = 1
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
    salida.write(inicio)
    for linea in lineas:
        #print("Empieza For")
        line = "<p>"
        tam = len(linea)
        i = 0
        while i <= tam:
            #print(i)
            #print("Empieza While")
            if i == tam:
                line = line + "</p>"
                salida.write(line + "\n")
                break
            
            elif linea[i] == "#":
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j].isalpha():
                        var = var + linea[j]
                        j += 1
                    else:
                        if var == "#include":
                            var = "<span class='palabra_reservada'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                        else:
                            var = "<span class='operador'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                i = j
            elif linea[i] == " ":
                j = 0
                while linea[i] == " ":
                    if linea[i+1] != " ":
                        line = line + linea[i]
                        i += 1
                    else:
                        i += 1
                        j += 1
                        #if linea[i] != " ":
                            #break
                        if j == 3:
                            line = line + "<span class='tab'></span>"
                            break
                    
            elif linea[i].isalpha():
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j].isalpha() or linea[j].isnumeric():
                        var = var + linea[j]
                        j += 1
                    else:
                        if var in palabras_reservadas:
                            var = "<span class='palabra_reservada'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                        else:
                            var = "<span class='variable'>" + var + "</span>"
                            line = line + var
                            var = ""
                            break     
                i = j
            elif linea[i].isnumeric():
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j].isnumeric() or linea[j] == "e":
                        var = var + linea[j]
                        j += 1
                    else:
                        var = "<span class='numero'>" + var + "</span>"
                        line = line + var
                        var = ""
                        break
                i = j
            elif linea[i] in operadores:
                #print("Entra al condicional de operadores")
                if linea[i] == "/":
                    if linea[i+1] == "/":
                        var = "<span class='comentario'>" + linea[i:tam-1] + "</span>"
                        line = line + var
                        var = ""
                        i = tam
                    else:
                        var = "<span class='operador'>" + linea[i] + "</span>"
                        line = line + var
                        var = ""
                        i += 1
                else:
                    var = "<span class='operador'>" + linea[i] + "</span>"
                    line = line + var
                    var = ""
                    i += 1
            
            elif linea[i] == '"':
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j] == '"':
                        var = "<span class='string'>" + var + linea[j] + "</span>"
                        j += 1
                        line = line + var
                        var = ""
                        break
                    else:
                        var = var + linea[j]
                        j += 1
                i = j
            else:
                i += 1
        #print("Fila "+str(contador)+" terminada")
        #contador +=1
    salida.write(final)
    entrada.close()
    salida.close()
    print("Fin del Programa")

syntax_highlight('test.txt','highlighter.html')