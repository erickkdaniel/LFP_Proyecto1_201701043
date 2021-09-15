from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from main import Analysis, Document
from main import AddDoc
from main import ReportToken
from main import ReportError
from main import DibujarImagen
from main import DrawingStyle
from main import DrawingHtml
from main import ForFilt
from main import ListDoc , ListDraws
listDocComb = []
listDrawComb = []
listDocAComb = []
class Window(ttk.Frame):
    def __init__(self,wind):
        super().__init__(wind)
        wind.title("Bitxelart")
        wind.geometry("600x400")
        self.notebook = ttk.Notebook(self,width=590,height=390)
        #carga------------------------------------------------------------------------------------------
        self.charg_label = ttk.Label(self.notebook)
        self.notebook.add(self.charg_label, text="Cargar", padding=20)
        ttk.Label(self.charg_label, text="Dirección:").place(x=10,y=5)
        self.dx = Entry(self.charg_label,width=75)
        self.dx.place(x=10,y=25,width=500)
        self.dx.focus()
        ttk.Button(self.charg_label,text = "Abrir", command= self.Abrir).place(x=345,y=50)
        ttk.Button(self.charg_label,text = "Examinar",command=self.Examinar).place(x=435,y=50)
        ttk.Button(self.charg_label,text="Cerrar",command=exit).place(y=290,x=460)
        #analizar------------------------------------------------------------------------------------------
        self.analy_label = ttk.Label(self.notebook)
        self.notebook.add(self.analy_label, text="Analizar", padding=20)
        self.combodocsa = ttk.Combobox(self.analy_label,state="readonly")
        self.combodocsa.place(x=10,y=20,width=350)
        self.combodocsa.set("Seleccione el nombre de su documento...")
        ttk.Button(self.analy_label,text="Analizar",command=self.Analizar).place(y=290,x=380)
        ttk.Button(self.analy_label,text="Cerrar",command=exit).place(y=290,x=460)
        #reportes------------------------------------------------------------------------------------------
        self.report_label = ttk.Label(self.notebook)
        self.notebook.add(self.report_label, text="Reportes", padding=20)
        self.combordocs = ttk.Combobox(self.report_label,state="readonly")
        self.combordocs.place(x=10,y=20,width=160)
        self.combordocs.set("Seleccione un documento...")
        selecdrdoc = self.combordocs.get()
        ttk.Button(self.report_label,text="Tokens",command=self.ReportarToken).place(x=10,y=60)
        ttk.Button(self.report_label,text="Errores",command=self.ReportarError).place(x=10,y=90)
        #mostrarimagen------------------------------------------------------------------------------------------
        self.Imagen_label = ttk.Label(self.notebook)
        self.notebook.add(self.Imagen_label, text="Imagen", padding=20)
        self.combodraws = ttk.Combobox(self.Imagen_label,state="readonly")
        self.combodraws.bind("<<ComboboxSelected>>",lambda _ : self.SelectedDraw())
        self.combodraws.place(x=10,y=20,width=160)
        self.combodraws.set("Seleccione una imagen...")
        self.selecdraw = self.combodraws.get()
        self.btOri = ttk.Button(self.Imagen_label,text="Original",command=self.Dibujar).place(x=20,y=60,width=100)
        self.btMx = ttk.Button(self.Imagen_label,text="Mirror X").place(x=20,y=90,width=100)
        self.btMy = ttk.Button(self.Imagen_label,text="Mirrox Y").place(x=20,y=120,width=100)
        self.btMxy = ttk.Button(self.Imagen_label,text="Double Mirror").place(x=20,y=150,width=100)
        prDraw = ttk.Labelframe(self.Imagen_label, text = "Imagen").place(x=180,y=5,width=360,height=315)
        self.notebook.pack(padx=5, pady=5)
        self.pack()
    def Examinar(self):
        self.dx.delete("0",END)
        self.doc = filedialog.askopenfilename(
        initialdir="C:\\Users\\danie\\Desktop\\", 
        title="Seleccione su documento")
        self.dx.insert(0,self.doc)
    def Abrir(self):
        AddDoc(str(self.dx.get()))
        global listDocComb
        dic = str(self.dx.get())
        print(dic)
        dxn = dic.split("/")
        listDocComb.append(dxn[-1])
        self.combodocsa['values'] = listDocComb     

    def Analizar(self):
        global listDocAComb,listDrawComb
        docselect = self.combodocsa.get()
        print(docselect)
        for doc in ListDoc:
            if doc.namedoc == docselect:
                docac = doc
                Analysis(doc)
                print(ListDraws)
                pass
        listDrawComb = []
        listDocAComb.append(docac.namedoc) 
        self.combordocs['values'] = listDocAComb
        self.docactual=docac
        lsd = self.docactual.draws
        for dr in lsd:
            if dr.Pixeleable:
                ForFilt(dr)
                listDrawComb.append(dr.nameDraw) 
        self.combodraws['values'] = listDrawComb 

    def ReportarToken(self):
        docselect = self.combordocs.get()
        print(docselect)
        for doc in ListDoc:
            if doc.namedoc == docselect:
                ReportToken(doc)
    def ReportarError(self):
        docselect = self.combordocs.get()
        print(docselect)
        for doc in ListDoc:
            if doc.namedoc == docselect:
                ReportError(doc)

    def Dibujar(self):
        drw=self.combodraws.get()
        for i in self.docactual.draws:
            if i.nameDraw == drw:
                DibujarImagen(i)
                DrawingStyle(i)
                DrawingHtml(i)
    def SelectedDraw(self):
        drw=self.combodraws.get()
        for i in self.docactual.draws:
            if i.nameDraw == drw:
                if i.mirrorx:
                    pass
                else:
                    self.btMx = ttk.Button(self.Imagen_label,text="Mirror X",state=DISABLED).place(x=20,y=90,width=100)
                if i.mirrory:
                    pass
                else:
                    self.btMy = ttk.Button(self.Imagen_label,text="Mirrox Y",state=DISABLED).place(x=20,y=120,width=100)
                if i.doublemirror:
                    pass
                else:
                    self.btMxy = ttk.Button(self.Imagen_label,text="Double Mirror",state=DISABLED).place(x=20,y=150,width=100)

windRoot = Tk()
BitWindow = Window(windRoot)
BitWindow.mainloop()
