from tkinter.constants import FALSE, N, TRUE
from tkinter.font import families
from typing import List
from enum import Enum
import os
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
    RESERVADA=18
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
class tipoE(Enum):
    NOIDENTIFICADO=1
    MAYUSCULA=2
    SINTACTICO=3    
class Error:
    def __init__(self,  type, char,fila,colum,desc):
        self.fila = fila
        self.colum = colum
        self.type = type
        self.char = char
        self.desc = desc

class Document:
    def __init__(self, doc,namedoc):
        self.namedoc=namedoc
        self.doc = doc
        self.draws=[]
        self.tokens = []
        self.errors=[]
        self.Reportable = False
    def addDraw(self, draw):
        self.draws.append(draw)
    def addTokens(self,token):
        self.tokens.append(token)
    def addError(self,error):
        self.errors.append(error)
    def Report(self):
        self.Reportable = True
    def ReportError(self):
        if len(self.errors)==0:
            return False
        else:
            return True

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
        self.Pixeleable = True
    def addCelda(self,celd):
        self.celdas.append(celd)
    def addFilter(self, filt):
        self.filtros.append(filt)
    def getFilter(self):
        return self.filtros
    def addParame(self,val):
        if self.last.upper()=="TITULO": 
            print("Se agrego en dibujo "+val)
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
TokensDraw = []
ErrorDraw = []
IdDraws = 1
Fila = 0
Columna = 0
Indice = 0
Texto = ""
def Analysis(tx):
    global Texto,Columna,Indice,Fila,ListDraws,ListDoc,TokensDraw,ErrorDraw
    ListDraws=[]
    Fila = 1
    Columna = 1
    Indice = 0
    Texto = tx
    EstadoInicial()
    ListDoc[-1].draws=ListDraws
    ListDoc[-1].tokens=TokensDraw
    ListDoc[-1].errors=ErrorDraw


def EstadoInicial():
    global Fila,Columna,ListDraws,ListDoc,TokensDraw,ErrorDraw
    actualC=getChar()
    bol=False
    bolc = False
    nceld = 1
    actualD = Draw()
    arrobas=""
    while actualC:
        if actualC.isalpha():
            aux = Letras()
            
            print(aux)
            if aux == "FALSE" or aux == "TRUE":
                celdtemp.setPaint(aux)
                NToken = Token(tipo.BOOL,aux,Fila,Columna)
                TokensDraw.append(NToken)
                nceld == 4
            elif aux == "MIRRORX" or aux == "MIRRORY" or aux == "DOUBLEMIRROR":
                actualD.addFilter(aux)
                NToken = Token(tipo.FILTRO,aux,Fila,Columna)
                TokensDraw.append(NToken)
            else:
                if aux == "TITULO":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    actualD.addlast(aux)
                elif aux == "ANCHO":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    actualD.addlast(aux)
                elif aux == "ALTO":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    actualD.addlast(aux)
                elif aux == "FILAS":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    actualD.addlast(aux)
                elif aux == "COLUMNAS":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    actualD.addlast(aux)
                elif aux == "CELDAS":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    actualD.addlast(aux)
                elif aux.upper() == "TITULO":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    NError = Error(tipoE.MAYUSCULA,aux,Fila,Columna,"La palabra reservada era en mayusculas, pero se corrigio")
                    ErrorDraw.append(NError)
                    actualD.addlast(aux.upper())
                elif aux.upper() == "ANCHO":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    NError = Error(tipoE.MAYUSCULA,aux,Fila,Columna,"La palabra reservada era en mayusculas, pero se corrigio")
                    ErrorDraw.append(NError)
                    actualD.addlast(aux.upper())
                elif aux.upper() == "ALTO":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    NError = Error(tipoE.MAYUSCULA,aux,Fila,Columna,"La palabra reservada era en mayusculas, pero se corrigio")
                    ErrorDraw.append(NError)
                    actualD.addlast(aux.upper())
                elif aux.upper() == "FILAS":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    NError = Error(tipoE.MAYUSCULA,aux,Fila,Columna,"La palabra reservada era en mayusculas, pero se corrigio")
                    ErrorDraw.append(NError)
                    actualD.addlast(aux.upper())
                elif aux.upper() == "COLUMNAS":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    NError = Error(tipoE.MAYUSCULA,aux,Fila,Columna,"La palabra reservada era en mayusculas, pero se corrigio")
                    ErrorDraw.append(NError)
                    actualD.addlast(aux.upper())
                elif aux.upper() == "CELDAS":
                    NToken = Token(tipo.RESERVADA,aux,Fila,Columna)
                    TokensDraw.append(NToken)
                    NError = Error(tipoE.MAYUSCULA,aux,Fila,Columna,"La palabra reservada era en mayusculas, pero se corrigio")
                    ErrorDraw.append(NError)
                    actualD.addlast(aux.upper())

        elif actualC == '"':
            aux = Cadenas(True)
            NToken = Token(tipo.COMILLAS,aux,Fila,Columna)
            TokensDraw.append(NToken)
            actualD.addParame(aux.replace('"',""))
            print(aux)
        elif actualC == "=":
            aux = kpopChar()
            NToken = Token(tipo.IGUAL,aux,Fila,Columna)
            TokensDraw.append(NToken)
            print(aux)
            bol = True

        elif actualC.isnumeric():
            aux = Numeros()
            NToken = Token(tipo.NUMERO,aux,Fila,Columna)
            TokensDraw.append(NToken)
            print(aux)
            if bolc and nceld == 1:
                celdtemp.setCx(aux)
                nceld=2
            elif bolc and nceld == 2:
                celdtemp.setCx(aux)
                nceld=3
            elif bolc and nceld == 4:
                celdtemp.setCx(aux)
                Celds.append(celdtemp)
            elif bol :
                actualD.addParame(aux)
                bol=False
            else:
                NError = Error(tipoE.SINTACTICO,aux,Fila,Columna,"No se esperaba un numero")
                ErrorDraw.append(NError)
                actualD.Pixeleable = False
                print("Error sintactico")
        elif actualC == "#":
            aux = Numeral()
            NToken = Token(tipo.NUMERAL,aux,Fila,Columna)
            TokensDraw.append(NToken)
            print(aux)
        elif actualC == "{":
            Celds = []
            aux = kpopChar()
            NToken = Token(tipo.LLAVEA,aux,Fila,Columna)
            TokensDraw.append(NToken)
            print(aux)
        elif actualC == "}":
            actualD.addCeldas(Celds)
            NToken = Token(tipo.LLAVEC,aux,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
            print(aux)
        elif actualC == "[":
            NToken = Token(tipo.CORCHETEA,aux,Fila,Columna)
            TokensDraw.append(NToken)
            nceld = 1
            celdtemp = Celda()
            bolc = True
            aux = kpopChar()
            print(aux)
        elif actualC == "]":
            NToken = Token(tipo.CORCHETEC,aux,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
            print(aux)
        elif actualC == ",":
            NToken = Token(tipo.COMA,aux,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
            print(aux)
        elif actualC == ";":
            NToken = Token(tipo.PUNTOCOMA,";",Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
            print(aux)
        elif actualC == "\n":
            aux = kpopChar(True)
        elif actualC == " ":
            aux = kpopChar()
        elif actualC == "@":
            aux = Arrobas(4)
            arrobas = arrobas+aux
            if len(aux)!=4:
                Token(tipo.ARROBA,arrobas,Fila,Columna)
                NError = Error(tipoE.SINTACTICO,actualC,Fila,Columna,'Se esperaban 4 "@", pero fue corregido')
                ErrorDraw.append(NError)
                print(arrobas)
                if len(actualD.celdas) != 0:
                    ListDraws.append(actualD)
                    actualD=Draw()
            else:
                ListDraws.append(actualD)
                print(aux)
                actualD=Draw()
                
        elif actualC == "\t":
            aux = kpopChar()
        else:
            print("Error Simbolo no definido"+str(actualC))
            NError = Error(tipoE.NOIDENTIFICADO,actualC,Fila,Columna,'El simbolo "'+str(actualC)+'" no fue definido')
            ErrorDraw.append(NError)
            actualD.Pixeleable = False
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
    namedocdx = dxn[-1]
    ListDoc.append(Document(text,namedocdx))
    print(ListDoc[0].namedoc)

def ReportToken(doc):
    named = doc.namedoc
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\ReporteTokens_"+named+".html", "w")
    file.write('<!DOCTYPE html><html><head><link rel="stylesheet" href="style.css"></head><body>')
    file.write("<h1>Tokens del documento "+named+".</h1>")
    file.write('<table class="styled-table"><thead><tr><td>No.</td><td>Tipo</td><td>Lexema</td><td>Fila</td><td>Columna</td></tr></thead>')
    file.write("<tbody>")
    ListT = doc.tokens
    n=1
    for i in ListT:
        file.write('<tr><td>'+str(n)+'</td><td>'+str(i.token)+'</td><td>'+str(i.lexe)+'</td><td><B>'+str(i.fila)+'<br></td><td>'+str(i.colum)+'</td></tr>')
        n+=1
    file.write("</tbody></table>")
    file.close()

def ReportError(doc):
    named = doc.namedoc
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\ReporteErrores_"+named+".html", "w")
    file.write('<!DOCTYPE html><html><head><link rel="stylesheet" href="style.css"></head><body>')
    file.write("<h1>Tokens del documento "+named+".</h1>")
    file.write('<table class="styled-table"><thead><tr><td>No.</td><td>Tipo</td><td>Lexema</td><td>Fila</td><td>Columna</td></tr></thead>')
    file.write("<tbody>")
    ListT = doc.errors
    n=1
    for i in ListT:
        file.write('<tr><td>'+str(n)+'</td><td>'+str(i.type)+'</td><td>'+str(i.char)+'</td><td><B>'+str(i.fila)+'<br></td><td>'+str(i.colum)+'</td></tr>')
        n+=1
    file.write("</tbody></table>")
    file.close()










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
#Analysis(strin)