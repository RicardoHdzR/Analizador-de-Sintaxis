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

operadores = ["=","+","+=","-","-=","*","*=","/","/=","%","%=","++","--"
"<",">","<=",">=","==","!=","<=>","!","&&","||",
"<<=",">>=","~","&=","|","|=","^","^=",
"(",")","[","]","->",".","->.",".*",",","::","::*",
"<?",">?"]

def syntax_highlight(archivo_entrada,archivo_salida):
    entrada = open(archivo_entrada,"r")
    salida = open(archivo_salida,"w")
    lineas = entrada.readlines()
    var = ""
    line = ""
    for linea in lineas:
        line = "<p>"
        tam = len(linea)
        i = 0
        while i <= tam:
            if i == tam:
                line = line + "</p>"
                salida.write(line)
                break
            elif linea[i] == " ":
                line = line + linea[i]
                i += 1
            elif linea[i].isalpha():
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j].isalpha() or linea[j].isnumeric():
                        var = var + linea[j]
                        j += 1
                    else:
                        if var in palabras_reservadas:
                            var = "<span class='palabra_reservada'" + var + "</span>"
                            line = line + var
                            var = ""
                            break
                        else:
                            var = "<span class='variable'" + var + "</span>"
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
                        var = "<span class='numero'" + var + "</span>"
                        line = line + var
                        var = ""
                        break
                i = j
            elif linea[i] in operadores:
                if linea[i] == "/":
                    if linea[i+1] == "/":
                        var = "<span class='numero'" + linea[i:tam] + "</span>"
                        line = line + var
                        var = ""
                        i = tam
                else:
                    var = "<span class='operador'" + linea[i] + "</span>"
                    line = line + var
                    i += 1
            elif linea[i] == "#":
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j].isalpha():
                        var = var + linea[j]
                        j += 1
                    else:
                        if var == "#include":
                            var = "<span class='palabra_reservada'" + linea[j] + "</span>"
                            line = line + var
                            var = ""
                            break
                        else:
                            var = "<span class='operador'" + linea[j] + "</span>"
                            line = line + var
                            var = ""
                            break
                i = j
            elif linea[i] == '"':
                var = var + linea[i]
                j = i+1
                while j < tam:
                    if linea[j] == '"':
                        var = "<span class='string'" + linea[j] + "</span>"
                        line = line + var
                        var = ""
                        break
                    else:
                        var = var + linea[j]
                i = j
    entrada.close()
    salida.close()
    print("Fin del Programa")

syntax_highlight('text.txt','highlighter.html')