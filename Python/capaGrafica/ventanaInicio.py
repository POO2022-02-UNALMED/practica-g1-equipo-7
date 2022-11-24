import tkinter as tk
import os

class VentanaInicio(tk.Tk):
    absolute_folder_path = os.path.dirname(os.path.realpath(__file__))

    absolute_image_chica_path = os.path.join(absolute_folder_path, '../recursos/Icono-chico.png')
    absolute_image_grande_path = os.path.join(absolute_folder_path, '../recursos/Icono-grande.png')
    
    imagenes = []
    imagenesHV = []
    

    def __init__(self):
        super().__init__()
        self.geometry("1024x750")
        self.title("Ventana Inicio JJ Library")
        self.option_add("*tearOff", False)
        self.resizable(False,False)
        #Cargar el archivo de icono e imagen
        iconoChico = tk.PhotoImage(file=self.absolute_image_chica_path)
        iconoGrande = tk.PhotoImage(file=self.absolute_image_grande_path)
        self.iconphoto(False, iconoGrande, iconoChico)

        self.indiceImagenActual = 0
        #cargar y almacenar en una lista las 5imagenes de inicio
        for i in range(5):
            local_path = "../recursos/imgInicio{}.png".format(i)
            absolute_imageInicio_path = os.path.join(self.absolute_folder_path, local_path)
            imagenInicio = tk.PhotoImage(file = absolute_imageInicio_path)
            self.imagenes.append(imagenInicio)
        
        frameP1 = tk.Frame(self, width=500, height=700)
        frameP2 = tk.Frame(self, width=500, height=800)
        #frameP3 = tk.Frame(frameP1, width=400, height=400)
        #frameP4 = tk.Frame(frameP1, width=400, height=250)
        #frameP5 = tk.Frame(frameP2, bg="gray", width=400, height=250)
        frameP6 = tk.Frame(frameP2, bg="#61727C", width=430, height=430)

        frameP1.pack(side="left", padx=30)
        frameP2.pack(side="right", padx=30)
        #frameP3.pack(side="top", padx=50, pady=15)
        #frameP4.pack(side="bottom", padx=50, pady=15)
        #frameP5.pack(side="top", padx=50, pady=15)
        frameP6.grid(row=1,column=0, padx=20, pady=20)

        #Menu
        menuBar = tk.Menu(self)
        self.config(menu=menuBar)
        
        menu = tk.Menu(menuBar)
        menuBar.add_cascade(label="Menu", menu=menu)
        
        menu.add_command(label="Salir", command = self.destroy)
        menu.add_command(label="Descripcion", command = self.mostrarDescripcion)
        
        #entrada a la aplicación y saludos
        self.mensajeBienvenida = "Bienvendio a la aplicación JJ library\n\n Biblioteca: Libreria POO"
        self.labelBienvenida = tk.Label(frameP1, text=self.mensajeBienvenida, font=("verdana", 16), fg="white",bg="#61727C", width=30, height=5, borderwidth=5, relief="groove", justify="left")
        self.labelBienvenida.grid(row=0, column=0,padx=20, pady=20)
        self.labelImagenInicio = tk.Label(frameP1, image=self.imagenes[0],width=400, height=375)
        self.labelImagenInicio.grid(row=1, column=0, padx=20, pady=20)
        self.labelImagenInicio.bind('<Enter>', self.cambiarImagenInicio)

        botonAplicacion = tk.Button(frameP1, text="Ir a la aplicacion", font=("verdana", 16), fg="white", bg="#61727C")
        botonAplicacion.grid(row=2, column=0, padx=20, pady=20)
        
        #Hojas de vida
        #Texto hoja de vida inicial
        self.indiceTextoHV = 0
        absolute_text_pack = os.path.join(self.absolute_folder_path, '../recursos/hv{}.txt'.format(self.indiceTextoHV))
        self.labelHojaVida = tk.Label(frameP2, text="", font=("verdana", 8), fg="white",bg="#61727C", width=60, height=15, relief="groove",border=5, justify="left")
        self.labelHojaVida.grid(row=0, column=0, padx=20, pady=20) 
        self.labelHojaVida.bind('<Button-1>', self.cambiarImagenesHV)
        with open(absolute_text_pack, "r+") as hvTexto:
            self.labelHojaVida.config(text=hvTexto.read())
            hvTexto.close()

        #Imagenes de la hoja de vida
        #Cargar las 4 de cada integrante imagenes en un array 
        
        for i in range(1,6):
            imagenesList = []
            for j in range(1,5):
                local_path = "../recursos/imagenHV-{}-{}.png".format(i, j)
                absolute_imageHV_path = os.path.join(self.absolute_folder_path, local_path)
                imagenHV = tk.PhotoImage(file = absolute_imageHV_path)
                imagenesList.append(imagenHV)
            self.imagenesHV.append(imagenesList)

        

        #Organizar las imagenes en p6
        self.indiceImagenesHVActuales = 0
        self.imagenesHVActuales = self.imagenesHV[self.indiceImagenesHVActuales]
        self.labelsImgHV = []
        for i in range(0,4):
            posiciones = [(0, 0), (0, 1), (1, 0), (1, 1)]
            (r, c) = posiciones[i]
            labelImagenHV = tk.Label(frameP6, image=self.imagenesHVActuales[i])
            labelImagenHV.grid(row=r, column=c, padx=2.5, pady=2.5)
            self.labelsImgHV.append(labelImagenHV)


        self.mainloop()

    def cambiarImagenInicio(self, args):
        if (self.indiceImagenActual == 4):
            self.indiceImagenActual = 0
        else:
            self.indiceImagenActual += 1
        
        self.labelImagenInicio.configure(image=self.imagenes[self.indiceImagenActual])
    
    def cambiarImagenesHV(self,args):
        if (self.indiceImagenesHVActuales == 4) and (self.indiceTextoHV == 4):
            self.indiceImagenesHVActuales = 0
            self.indiceTextoHV = 0
        else:
            self.indiceImagenesHVActuales += 1
            self.indiceTextoHV += 1

        #Cambiar el texto
        absolute_text_pack = os.path.join(self.absolute_folder_path, '../recursos/hv{}.txt'.format(self.indiceTextoHV))
        with open(absolute_text_pack, "r+") as hvTexto:
            self.labelHojaVida.config(text=hvTexto.read())
        
        for i in range(0,4):
            self.labelsImgHV[i].configure(image=self.imagenesHV[self.indiceImagenesHVActuales][i])
        
    def mostrarDescripcion(self):
        absolute_desc_path = os.path.join(self.absolute_folder_path, '../recursos/descripcion.txt')
        with open(absolute_desc_path, "r+") as descripcion:
            self.labelBienvenida.configure(text=descripcion.read(), font=("verdana", 8), width=55, height=12, justify="left")
            
        self.labelBienvenida.bind('<Button-1>', self.mostrarBienvenida)
        
    def mostrarBienvenida(self, args):
            self.labelBienvenida.configure(text=self.mensajeBienvenida, font=("verdana", 16), width=30, height=5)

class ventanaDescripcion(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("720x480")
        self.title("Descripcion")
        self.resizable(False,False)
        
        #Texto descripcion
        self.labelDescripcion = tk.Label(self, text="Soy la descripcion")
        self.labelDescripcion.pack(expand=True)
        self.mainloop()