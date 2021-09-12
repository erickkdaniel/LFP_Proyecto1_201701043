from tkinter.constants import FALSE, N, TRUE
from tkinter.font import families
from typing import List
from enum import Enum
class tipo(Enum):
    TEXTO=1
    NUMERO=2
    IGUAL = 4
    COMA = 5
    CORCHETEA = 6
    CORCHETEC = 7
    LLAVEA = 8
    LLAVEC = 9
    PUNTOCOMA = 10
    NUMERAL = 11
    ARROBA = 12
    BOOL = 13
    TAB = 14
    ESPACIO = 15
    COMILLAS = 16
    FILTRO = 17
class Token:
    def __init__(self,tok,lex,fila,colu):
        self.token=tok
        self.lexe=lex
        self.fila=fila
        self.colum=colu
class Celda:
    def __init__(self):
        self.coorx = 0
        self.coory = 0
        self.color = 0
        self.paint = False
    def setCx(self, corx):
        self.coorx = corx
    def setCy(self, cory):
        self.coory = cory
    def setColor(self, color):
        self.color = color
    def setPaint(self, paint):
        if paint.upper() == "TRUE":
            self.paint == True
    
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
    def __init__(self):
        self.nameDraw = ""
        self.nCol = 0
        self.nFil = 0
        self.pxX = 0
        self.PxY = 0
        self.celdas = []
        self.filtros = []
        self.mirrorx = False
        self.mirrory = False
        self.doublemirror = False
        self.last = "" 
    def addCelda(self,celd):
        self.celdas.append(celd)
    def addFilter(self, filt):
        self.filtros.append(filt)
    def getFilter(self):
        return self.filtros
    def addParame(self,val):
        if self.last.upper()=="TITULO": 
            self.nameDraw = val
        elif self.last.upper()=="ANCHO": 
            self.pxX = val
        elif self.last.upper()=="ALTO": 
            self.PxY = val
        elif self.last.upper()=="FILAS": 
            self.nFil = val
        elif self.last.upper()=="COLUMNAS": 
            self.nCol = val
        elif self.last.upper()=="CELDAS": 
            self.nCol = val
    def addlast(self,val):
        self.last=val
    def addCeldas(self,listceld):
        self.celdas = listceld
    def addFilter(self,filer):
        if filer.upper() == "MIRRORX":
            self.mirrorx = True
        elif filer.upper() == "MIRRORY":
            self.mirrorx = True
        elif filer.upper() == "DOUBLEMIRROR":
            self.mirrorx = True

ListDoc = []
ListDraws = []
IdDraws = 1
Fila = 0
Columna = 0
Indice = 0
Texto = ""
def Analysis(tx):
    global Texto,Columna,Indice,Fila,ListDraws,ListDoc
    ListDraws=[]
    Fila = 1
    Columna = 1
    Indice = 0
    Texto = tx
    EstadoInicial()

def EstadoInicial():
    global Fila,Columna,ListDraws,ListDoc
    
    actualC=getChar()
    bol=False
    bolc = False
    nceld = 1
    actualD = Draw()
    TokensDraw = []
    while actualC:
        if actualC.isalpha():
            aux = Letras()
            
            print(aux)
            if aux == "FALSE" or aux == "TRUE":
                celdtemp.setPaint(aux)
                nceld == 4
            elif aux == "MIRRORX" or aux == "MIRRORY" or aux == "DOUBLEMIRROR":
                actualD.addFilter(aux)
            else:
                NToken = Token(tipo.TEXTO,aux,Fila,Columna)
                TokensDraw.append(NToken)
                actualD.addlast(aux)
        elif actualC == '"':
            aux = Cadenas(True)
            print(aux)
        elif actualC == "=":
            aux = kpopChar()
            print(aux)
            bol = True

        elif actualC.isnumeric():
            aux = Numeros()
            print(aux)
            if bol :
                actualD.addParame(aux)
                bol=False
            elif bolc and nceld == 1:
                celdtemp.setCx(aux)
                nceld=2
            elif bolc and nceld == 2:
                celdtemp.setCx(aux)
                nceld=3
            elif bolc and nceld == 4:
                celdtemp.setCx(aux)
                Celds.append(celdtemp)
            else:
                print("Error sintactico")
        elif actualC == "#":
            aux = Numeral()
            print(aux)
        elif actualC == "{":
            Celds = []
            aux = kpopChar()
            print(aux)
        elif actualC == "}":
            actualD.addCeldas(Celds)
            aux = kpopChar()
            print(aux)
        elif actualC == "[":
            nceld = 1
            celdtemp = Celda()
            bolc = True
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
                ListDraws.append(actualD)
                print(aux)
                actualD=Draw()
        elif actualC == "\t":
            aux = kpopChar()
        else:
            print("Error Simbolo no definido"+str(actualC))
            kpopChar()
        actualC=getChar()
    
    ListDraws.append(actualD)

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
def AddDoc(dx):
    global ListDoc
    print(dx)
    doc = open(dx)
    text = doc.read()
    dxn = dx.split("/")
    print(dxn[-1])
    ListDoc.append(Document(text,str(dxn[-1].replace(".lfp",""))))
    print(ListDoc[0].namedoc)












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