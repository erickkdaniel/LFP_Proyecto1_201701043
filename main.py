from typing import List

class Token:
    def __init__(self,tok,lex,fila,colu):
        self.token=tok
        self.lexe=lex
        self.fila=fila
        self.colum=colu
class Celda:
    def __init__(self, corx,cory,color):
        self.coorx = corx
        self.coory = cory
        self.color = color
        self.paint = False
class Error:
    def __init__(self,  type, char,fila,colum):
        self.fila = fila
        self.colum = colum
        self.type = type
        self.char = char

class Document:
    def __init__(self, doc,namedoc):
        self.namedoc=namedoc
        self.doc = doc
        self.draws=[]
        self.tokens = []
        self.errors=[]
    def addDraw(self, draw):
        self.draws.append(draw)
    def addTokens(self,token):
        self.tokens.append(token)
    def addError(self,error):
        self.errors.append(error)

class Draw:
    def __init__(self,name, nCol, nFil,PxX, PxY):
        self.nameDraw = name
        self.nCol = nCol
        self.nFil = nFil
        self.pxX = PxX
        self.PxY = PxY
        self.celdas = []
        self.filtros = []
        self.mirrorx = False
        self.mirrory = False
        self.doublemirror = False
    def addCelda(self,celd):
        self.celdas.append(celd)
    def addFilter(self, filt):
        self.filtros.append(filt)
    def getFilter(self):
        return self.filtros


ListDraws = []
IdDraws = 1
Fila = 0
Columna = 0
Indice = 0
Texto = ""
def Analysis(tx):
    global Texto,Columna,Indice,Fila
    Fila = 1
    Columna = 1
    Indice = 0
    Texto = tx
    EstadoInicial()

def EstadoInicial():
    actualC=getChar()
    while actualC:
        if actualC.isalpha():
            aux = Letras()
            print(aux)
        elif actualC == '"':
            aux = Cadenas(True)
            print(aux)
        elif actualC == "=":
            aux = kpopChar()
            print(aux)
        elif actualC.isnumeric():
            aux = Numeros()
            print(aux)
        elif actualC == "#":
            aux = Numeral()
            print(aux)
        elif actualC == "{":
            aux = kpopChar()
            print(aux)
        elif actualC == "}":
            aux = kpopChar()
            print(aux)
        elif actualC == "[":
            aux = kpopChar()
            print(aux)
        elif actualC == "]":
            aux = kpopChar()
            print(aux)
        elif actualC == ",":
            aux = kpopChar()
            print(aux)
        elif actualC == ";":
            aux = kpopChar()
            print(aux)
        elif actualC == "\n":
            aux = kpopChar(True)
        elif actualC == " ":
            aux = kpopChar()
        elif actualC == "@":
            aux = Arrobas(4)
            if len(aux)!=4:
                print("No hay 4 @")
        
            else:
                print(aux)
        elif actualC == "\t":
            aux = kpopChar()
        else:
            print("Error Simbolo no definido"+str(actualC))
            kpopChar()
        actualC=getChar()

def Letras():
    actual=getChar()
    if actual is None:
        return ""
    if getChar().isalpha():
        Concat = kpopChar()+Letras()
        return Concat
    else:
        return ""
def Cadenas(bandera):
    actual=getChar()
    if actual is None:
        return ""
    if actual=='"':
        if bandera == False:
            return kpopChar()
        else:
            Concat = kpopChar()+Cadenas(False)
            return Concat
    else:
        Concat = kpopChar()+Cadenas(False)
        return Concat
def Numeros():
    actual=getChar()
    if actual is None:
        return ""
    if getChar().isnumeric():
        Concat = kpopChar()+Numeros()
        return Concat
    else:
        return ""
def Numeral():
    actual=getChar()
    if actual is None:
        return ""
    if getChar()=="#":
        Concat = kpopChar()+Numeros()
        return Concat
    else:
        return ""
def Arrobas(cant):
    actual=getChar()
    if actual is None:
        return ""
    if cant==0:
        return ""
    if getChar()=="@":
        
        Concat = kpopChar()+Arrobas(cant-1)
        
        return Concat
    else:
        return ""
       
def getChar():
    global Texto , Indice
    if Indice == len(Texto):
        return None
    else:
        return Texto[Indice]
def kpopChar(salto=False):
    global Texto , Indice, Fila, Columna
    if Indice == len(Texto):
        return None
    else:
        if salto:
            Fila +=1
            Columna = 1
        else:
            Columna+=1
        chr=Texto[Indice]
        Indice+=1
        return chr













strin="""TITULO="Pokebola";
ANCHO=300;
ALTO=300;
FILAS=12;
COLUMNAS=12;
CELDAS = {
[0,0,FALSE,#000000],
[0,1,FALSE,#000000],
[3,3,FALSE,#000000],
[3,4,TRUE,#000000],
    [3,5,TRUE,#000000],
[3,6,TRUE,#000000],
[3,7,TRUE,#000000],
[4,1,FALSE,#000000]
};
FILTROS = MIRRORX;
@@@@
TITULO="Estrella";
ANCHO=300;
ALTO=300;
FILAS=4;
COLUMNAS=4;
CELDAS = {
[0,0,FALSE,#000000],
[1,1,FALSE,#000000],
[3,3,FALSE,#000000],
[2,1,FALSE,#000000]
};
FILTROS = MIRRORX,MIRRORY,DOUBLEMIRROR;
"""
Analysis(strin)