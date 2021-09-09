from tkinter import ttk
from tkinter import *
from tkinter import filedialog
class Window(ttk.Frame):
    def __init__(self,wind):
        super().__init__(wind)
        wind.title("Bitxelart")
        wind.geometry("600x400")
        self.notebook = ttk.Notebook(self,width=590,height=390)
        #carga
        self.charg_label = ttk.Label(self.notebook)
        self.notebook.add(self.charg_label, text="Cargar", padding=20)
        ttk.Label(self.charg_label, text="Dirección:").place(x=10,y=5)
        self.dx = Entry(self.charg_label,width=75)
        self.dx.place(x=10,y=25,width=500)
        self.dx.focus()
        ttk.Button(self.charg_label,text = "Abrir").place(x=345,y=50)
        ttk.Button(self.charg_label,text = "Examinar",command=self.Examinar).place(x=435,y=50)
        ttk.Button(self.charg_label,text="Cerrar",command=exit).place(y=290,x=460)
        #analizar
        self.analy_label = ttk.Label(self.notebook)
        self.notebook.add(self.analy_label, text="Analizar", padding=20)
        self.combodocs = ttk.Combobox(self.analy_label,state="readonly")
        self.combodocs.place(x=10,y=20,width=350)
        self.combodocs.set("Seleccione el nombre de su documento...")
        ttk.Button(self.analy_label,text="Analizar").place(y=290,x=380)
        ttk.Button(self.analy_label,text="Cerrar",command=exit).place(y=290,x=460)
        #reportes
        self.report_label = ttk.Label(self.notebook)
        self.notebook.add(self.report_label, text="Reportes", padding=20)
        self.combordocs = ttk.Combobox(self.report_label,state="readonly")
        self.combordocs.place(x=10,y=20,width=160)
        self.combordocs.set("Seleccione un documento...")
        selecdrdoc = self.combordocs.get()
        ttk.Button(self.report_label,text="Tokens").place(x=10,y=60)
        ttk.Button(self.report_label,text="Errores").place(x=10,y=90)
        #mostrarimagen
        self.Imagen_label = ttk.Label(self.notebook)
        self.notebook.add(self.Imagen_label, text="Imagen", padding=20)
        self.combodraws = ttk.Combobox(self.Imagen_label,state="readonly")
        self.combodraws.place(x=10,y=20,width=160)
        self.combodraws.set("Seleccione una imagen...")
        selecdraw = self.combodraws.get()
        ttk.Button(self.Imagen_label,text="Original").place(x=20,y=60,width=100)
        ttk.Button(self.Imagen_label,text="Mirror X").place(x=20,y=90,width=100)
        ttk.Button(self.Imagen_label,text="Mirrox Y").place(x=20,y=120,width=100)
        ttk.Button(self.Imagen_label,text="Double Mirror").place(x=20,y=150,width=100)
        prDraw = ttk.Labelframe(self.Imagen_label, text = "Imagen").place(x=180,y=5,width=360,height=315)
        self.notebook.pack(padx=5, pady=5)
        self.pack()
    def Examinar(self):
        doc = filedialog.askopenfilename(
        initialdir="C:\\Users\\danie\\Desktop\\", 
        title="Seleccione su documento")
        self.dx.insert(0,doc)
        


windRoot = Tk()
BitWindow = Window(windRoot)
BitWindow.mainloop()
