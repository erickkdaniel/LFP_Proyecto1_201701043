from typing import List


class Celda:
    def __init__(self, corx,cory,color):
        self.coorx = corx
        self.coory = cory
        self.color = color
        self.paint = False
class Error:
    def __init__(self, line, type, char):
        self.line = line
        self.type = type
        self.char = char

class Draw:
    def __init__(self,name, nCol, nFil,PxX, PxY):
        self.nameDraw = name
        self.nCol = nCol
        self.nFil = nFil
        self.pxX = PxX
        self.PxY = PxY
        self.celdas = []
        self.filtros = []
        self.Errors = []
    def addError(self, line, type, char):
        self.Errors.append(Error(line,type,char))
    def addCelda(self,celd):
        self.celdas.append(celd)
    def addFilter(self, filt):
        self.filtros.append(filt)
ListDraws = []
IdDraws = 1
def AnalysisTx(doc):
    fDraws = doc.split("@@@@")
    for drw in fDraws:
        fAtributs = drw.split(";")
        fName = fAtributs[0].replace('"','')
        Name = fName.split("=")
        fAncho = fAtributs[1].split("=")
        Ancho=  fAncho[1].replace('"','')
        fAlto = fAtributs[2].split("=")
        Alto=  fAlto[1].replace('"','')
        fFilas = fAtributs[3].split("=")
        Filas=  fFilas[1].replace('"','')
        fColum = fAtributs[4].split("=")
        Colum=  fColum[1].replace('"','')
        fCelda1 = fAtributs[5].split("=")
        fCelda = fCelda1[1].replace("{","")
        fCelda = fCelda.replace("}","")
        fCelda = fCelda.replace(" ","")
        fCelda = fCelda.replace("\n","")
        fCelda = fCelda.replace("}","")
        fCelda = fCelda.replace("{","")
        fCeldas = fCelda.split("],[")
        fFilt = fAtributs[6].split("=")
        fFilter = fFilt[1].replace(" ","")
        fFilters = fFilter.split(",")
        DrawAc=Draw(Name,Colum,Filas,Ancho,Alto)
        ListDraws.append(DrawAc)
        for celd in fCeldas:
            CeldaAt = celd.replace("[","")
            CeldaAt = CeldaAt.replace("]","")
            fCeldaAt = CeldaAt.split(",")
            posX = fCeldaAt[0]
            posY = fCeldaAt[1]
            Paint = fCeldaAt[2]
            Color = fCeldaAt[3]
            ListDraws[IdDraws-1].addCelda(Celda(posX,posY,Color))
        for filt in fFilters:
            DrawAc.addFilter(str(filt))
        IdDraws = IdDraws+1