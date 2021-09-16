from tkinter.constants import FALSE, N, TRUE
from tkinter.font import families
from typing import List
from enum import Enum
import imgkit
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
    COLOR=19
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
        self.nceld = 0
        self.color = ""
        self.paint = False
    def setCx(self, corx):
        self.coorx = corx
    def setCy(self, cory):
        self.coory = cory
    def setColor(self, color):
        self.color = color
    def setPaint(self, paint):
        if paint.upper() == "TRUE":
            self.paint = True
class tipoE(Enum):
    SIMBOLO_NO_IDENTIFICADO=1
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
            self.mirrory = True
        elif filer.upper() == "DOUBLEMIRROR":
            self.doublemirror = True

ListDoc = []
ListDraws = []
TokensDraw = []
ErrorDraw = []
contcel = 0
IdDraws = 1
Fila = 0
Columna = 0
Indice = 0
Texto = ""
def Analysis(Doc):
    global Texto,Columna,Indice,Fila,ListDraws,ListDoc,TokensDraw,ErrorDraw
    ListDraws=[]
    TokensDraw = []
    ErrorDraw = []
    Fila = 1
    Columna = 1
    Indice = 0
    Texto = Doc.doc
    EstadoInicial()
    Doc.draws=ListDraws
    Doc.tokens=TokensDraw
    Doc.errors=ErrorDraw
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
            NToken = Token(tipo.COMILLAS,'"',Fila,Columna)
            TokensDraw.append(NToken)
            NToken = Token(tipo.TEXTO,aux.replace('"',''),Fila,Columna)
            TokensDraw.append(NToken)
            NToken = Token(tipo.COMILLAS,'"',Fila,Columna)
            TokensDraw.append(NToken)
            actualD.addParame(aux.replace('"',""))
        elif actualC == "=":
            aux = kpopChar()
            NToken = Token(tipo.IGUAL,aux,Fila,Columna)
            TokensDraw.append(NToken)
            bol = True

        elif actualC.isnumeric():
            aux = Numeros()
            NToken = Token(tipo.NUMERO,aux,Fila,Columna)
            TokensDraw.append(NToken)
            if bolc and nceld == 1:
                celdtemp.setCx(aux)
                nceld=2
            elif bolc and nceld == 2:
                celdtemp.setCy(aux)
                nceld=3
            elif bol :
                actualD.addParame(aux)
                bol=False
            else:
                NError = Error(tipoE.SINTACTICO,aux,Fila,Columna,"No se esperaba un numero")
                ErrorDraw.append(NError)
                actualD.Pixeleable = False
        elif actualC == "#":
            aux = Color(True).replace("]","")
            celdtemp.setColor(aux)
            Celds.append(celdtemp)
            NToken = Token(tipo.NUMERAL,"#",Fila,Columna)
            TokensDraw.append(NToken)
            NToken = Token(tipo.COLOR,aux,Fila,Columna)
            TokensDraw.append(NToken)
            NToken = Token(tipo.CORCHETEC,"]",Fila,Columna)
            TokensDraw.append(NToken)            
        elif actualC == "{":
            Celds = []
            aux = kpopChar()
            NToken = Token(tipo.LLAVEA,actualC,Fila,Columna)
            TokensDraw.append(NToken)
        elif actualC == "}":
            actualD.addCeldas(Celds)
            NToken = Token(tipo.LLAVEC,actualC,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
        elif actualC == "[":
            NToken = Token(tipo.CORCHETEA,actualC,Fila,Columna)
            TokensDraw.append(NToken)
            nceld = 1
            celdtemp = Celda()
            bolc = True
            aux = kpopChar()
        elif actualC == "]":
            NToken = Token(tipo.CORCHETEC,actualC,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
        elif actualC == ",":
            NToken = Token(tipo.COMA,actualC,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
        elif actualC == ";":
            NToken = Token(tipo.PUNTOCOMA,actualC,Fila,Columna)
            TokensDraw.append(NToken)
            aux = kpopChar()
        elif actualC == "\n":
            aux = kpopChar(True)
        elif actualC == " ":
            aux = kpopChar()
        elif actualC == "@":
            aux = Arrobas(4)
            arrobas = arrobas+aux
            if len(aux)!=4:
                NToken=Token(tipo.ARROBA,arrobas,Fila,Columna)
                TokensDraw.append(NToken)
                NError = Error(tipoE.SINTACTICO,actualC,Fila,Columna,'Se esperaban 4 "@", pero fue corregido')
                ErrorDraw.append(NError)
                if len(actualD.celdas) != 0:
                    ListDraws.append(actualD)
                    actualD=Draw()
            else:
                NToken=Token(tipo.ARROBA,arrobas,Fila,Columna)
                TokensDraw.append(NToken)
                ListDraws.append(actualD)
                actualD=Draw()
                
        elif actualC == "\t":
            aux = kpopChar()
        else:
            NError = Error(tipoE.SIMBOLO_NO_IDENTIFICADO,actualC,Fila,Columna,'El simbolo "'+str(actualC)+'" no fue definido')
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
def Color(bandera):
    actual=getChar()
    if actual is None:
        return ""
    if actual==']':
        if bandera == False:
            return kpopChar()
        else:
            Concat = kpopChar()+Color(False)
            return Concat
    else:
        Concat = kpopChar()+Color(False)
        return Concat
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
        Concat = kpopChar()+Cadenas()
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
    doc = open(dx)
    text = doc.read()
    dxn = dx.split("/")
    namedocdx = dxn[-1]
    ListDoc.append(Document(text,namedocdx))
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
        file.write('<tr><td>'+str(n)+'</td><td>'+str(i.token).replace("tipo.","")+'</td><td>'+str(i.lexe)+'</td><td><B>'+str(i.fila)+'<br></td><td>'+str(i.colum)+'</td></tr>')
        n+=1
    file.write("</tbody></table>")
    file.close()

def ReportError(doc):
    named = doc.namedoc
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\ReporteErrores_"+named+".html", "w")
    file.write('<!DOCTYPE html><html><head><link rel="stylesheet" href="style.css"></head><body>')
    file.write("<h1>Errores del documento "+named+".</h1>")
    file.write('<table class="styled-table"><thead><tr><td>No.</td><td>Tipo</td><td>Lexema</td><td>Fila</td><td>Columna</td><td>Descripción</td></tr></thead>')
    file.write("<tbody>")
    ListT = doc.errors
    n=1
    for i in ListT:
        file.write('<tr><td>'+str(n)+'</td><td>'+str(i.type).replace("tipoE.","")+'</td><td>'+str(i.char)+'</td><td>'+str(i.fila)+'</td><td>'+str(i.colum)+'</td><td>'+str(i.desc)+'</td></tr>')
        n+=1
    file.write("</tbody></table>")
    file.close()

def DibujarImagen(drawing):
    named = drawing.nameDraw
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\Celdas_"+named+".html", "w")
    file.write('<!DOCTYPE html><html><head><link rel="stylesheet" href="style.css"></head><body>')
    file.write("<h1>Tokens del documento "+named+".</h1>")
    file.write('<table class="styled-table"><thead><tr><td>No.</td><td>CoorX</td><td>CoorY</td><td>Color</td><td>Pintar</td></thead>')
    file.write("<tbody>")
    ListC = drawing.celdas
    n=1
    for i in ListC:
        if i.paint:
            file.write('<tr><td>'+str(n)+'</td><td>'+str(i.coorx)+'</td><td>'+str(i.coory)+'</td><td>'+str(i.color)+'</td><td>SI</td></tr>')
            n+=1
        else:
            file.write('<tr><td>'+str(n)+'</td><td>'+str(i.coorx)+'</td><td>'+str(i.coory)+'</td><td>'+str(i.color)+'</td><td>NO</td></tr>')
            n+=1
    file.write("</tbody></table>")
    file.close()
def ForFilt(Drawing):
    DrawingStyle(Drawing,0)
    if Drawing.mirrorx:
        DrawingStyle(Drawing,1)
    if Drawing.mirrory:
        DrawingStyle(Drawing,2)
    if Drawing.doublemirror:
        DrawingStyle(Drawing,3)
def DrawingStyle(Drawing,Filt):
    named=Drawing.nameDraw
    pixX=str(Drawing.pxX)
    pixY=str(Drawing.PxY)
    TamX=int(Drawing.pxX)/int(Drawing.nCol)
    TamY=int(Drawing.PxY)/int(Drawing.nFil)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if Filt == 0:
        file = open(dir_path+"\\STYLE_0_"+named+".css", "w")
    if Filt == 1:
        file = open(dir_path+"\\STYLE_1_"+named+".css", "w")
    if Filt == 2:
        file = open(dir_path+"\\STYLE_2_"+named+".css", "w")
    if Filt == 3:
        file = open(dir_path+"\\STYLE_3_"+named+".css", "w")
    file.write("""body {
    display: flex;               
    }""")
    file.write(".canvas {\n")
    file.write("width: "+pixX+"px;\n")   #/* Ancho del lienzo, se asocia al ANCHO de la entrada */
    file.write("height: "+pixY+"px;}\n")  #/* Alto del lienzo, se asocia al ALTO de la entrada */
    file.write(".pixel {\n")
    file.write("width: "+str(int(TamX))+"px;\n")    #/* Ancho de cada pixel, se obtiene al operar ANCHO/COLUMNAS (al hablar de pixeles el resultado de la división debe ser un numero entero) */
    file.write("height: "+str(int(TamY))+"px;\n")   #/* Alto de cada pixel, se obtiene al operar ALTO/FILAS (al hablar de pixeles el resultado de la división debe ser un numero entero) */
    file.write("float: left;\n")
    file.write("box-shadow: 0px 0px 1px #fff;}\n") #/*Si lo comentan les quita la cuadricula de fondo */
    if Filt == 0:
        ForCeldsO(Drawing)
    if Filt == 1:
        ForCeldsMx(Drawing)
    if Filt == 2:
        ForCeldsMy(Drawing)
    if Filt == 3:   
        ForCeldsMxy(Drawing)
    lsceld = Drawing.celdas
    for cel in lsceld:
        if cel.paint:
            file.write(".pixel:nth-child("+str(cel.nceld)+"){background: "+str(cel.color)+";}\n")

    file.close()
    DrawingHtml(Drawing,Filt)

def DrawingHtml(Drawing,Filt):
    named=Drawing.nameDraw
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if Filt ==0:
        file = open(dir_path+"\\HTML_0_"+named+".html", "w")
        file.write("<!DOCTYPE html><html><head>")
        file.write('<link rel="stylesheet" href="STYLE_0_'+named+'.css">')
    elif Filt ==1:
        file = open(dir_path+"\\HTML_1_"+named+".html", "w")
        file.write("<!DOCTYPE html><html><head>")
        file.write('<link rel="stylesheet" href="STYLE_1_'+named+'.css">')
    elif Filt ==2:
        file = open(dir_path+"\\HTML_2_"+named+".html", "w")
        file.write("<!DOCTYPE html><html><head>")
        file.write('<link rel="stylesheet" href="STYLE_2_'+named+'.css">')
    elif Filt ==3:
        file = open(dir_path+"\\HTML_3_"+named+".html", "w")
        file.write("<!DOCTYPE html><html><head>")
        file.write('<link rel="stylesheet" href="STYLE_3_'+named+'.css">')
    file.write("</head>")
    file.write("<body>")
    file.write('<div class="canvas">')
    colD=int(Drawing.nCol)
    filD=int(Drawing.nFil)
    tcel = colD*filD
    for i in range(0,tcel,1):
        file.write('<div class="pixel"></div>')
    file.write('</div>')
    file.write('</body>')
    file.write('</html>')
    file.close()
    ConvIMG(named,Filt)
def ForCeldsO(Drawing):
    listac=Drawing.celdas
    fil=int(Drawing.nFil)
    col=int(Drawing.nCol)
    n=1
    for i in range(0,fil,1):
        for j in range(0,col,1):
            for cel in listac:
                if int(cel.coorx) == j and int(cel.coory)==i:
                    cel.nceld = n
                    n=n+1
def ForCeldsMy(Drawing):
    listac=Drawing.celdas
    fil=int(Drawing.nFil)
    col=int(Drawing.nCol)
    n=1
    for i in range(fil,-1,-1):
        for j in range(0,col,1):
            for cel in listac:
                if int(cel.coorx) == j and int(cel.coory)==i:
                    cel.nceld = n
                    n=n+1
def ForCeldsMx(Drawing):
    listac=Drawing.celdas
    fil=int(Drawing.nFil)
    col=int(Drawing.nCol)
    n=1
    for i in range(0,fil,1):
        for j in range(col,-1,-1):
            for cel in listac:
                if int(cel.coorx) == j and int(cel.coory)==i:
                    cel.nceld = n
                    n=n+1
def ForCeldsMxy(Drawing):
    listac=Drawing.celdas
    fil=int(Drawing.nFil)
    col=int(Drawing.nCol)
    n=1
    for i in range(fil,-1,-1):
        for j in range(col,-1,-1):
            for cel in listac:
                if int(cel.coorx) == j and int(cel.coory)==i:
                    cel.nceld = n
                    n=n+1
kitoptions = {
  "enable-local-file-access": None
}
def ConvIMG(named,filt):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if filt == 0:
        imgkit.from_file(dir_path+"\\HTML_0_"+named+".html",dir_path+"\\D_0_"+named+".jpg", options=kitoptions)
    elif filt == 1:
        imgkit.from_file(dir_path+"\\HTML_1_"+named+".html",dir_path+"\\D_1_"+named+".jpg", options=kitoptions)
    elif filt == 2:
        imgkit.from_file(dir_path+"\\HTML_2_"+named+".html",dir_path+"\\D_2_"+named+".jpg", options=kitoptions)
    elif filt == 3:
        imgkit.from_file(dir_path+"\\HTML_3_"+named+".html",dir_path+"\\D_3_"+named+".jpg", options=kitoptions)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path+"\\D_3_"+named+".jpg"  