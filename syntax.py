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
    
