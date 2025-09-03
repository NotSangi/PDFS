from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from modulos.operaciones_pdf import Operaciones

class App():
    def __init__(self, ventana):
        self.color_principal = "#307AA5"
        self.color_texto = "#C1E1F3"
        self.posicion_x = 150
        
        self.ventana = ventana
        self.ventana.title('Operaciones PDF')
        self.ventana.geometry('500x350+660+300')
        self.ventana.config(bg=self.color_principal)
        self.ventana.resizable(0,0)
        self.funciones = Operaciones()
        self.file_path = ""
        
        #Etiquetas Menu Principal
        
        self.lbl_menu = Label(ventana, text="¿Qué deseas realizar?", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_menu.place(x=self.posicion_x, y=30)

        self.btn_opcion_1 = Button(ventana, width=15, text="Juntar PDF", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15), command=self.opcion_1)
        self.btn_opcion_1.place(x=self.posicion_x+20, y=80)
        
        self.btn_opcion_2 = Button(ventana, width=15, text="Separar PDF", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15), command=self.opcion_2)
        self.btn_opcion_2.place(x=self.posicion_x+20, y=160)
        
        self.btn_opcion_3 = Button(ventana, width=15, text="Firmar PDF", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15), command=self.opcion_3)
        self.btn_opcion_3.place(x=self.posicion_x+20, y=240)
        
        self.boton_volver = Button(self.ventana, width=10, text='Volver', bg=self.color_principal, fg=self.color_texto, font=('Arial', 10), command=self.volver)
        
        # Etiquetas Opciones
        self.lbl_archivo_1 = Label(self.ventana, text="Abre el archivo PDF", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_archivo_2 = Label(self.ventana, text="Abre el archivo PDF", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        
        self.nombre_archivo_1 = Entry(self.ventana, width=50, font=('Arial', 10), state='readonly')
        self.nombre_archivo_2 = Entry(self.ventana, width=50, font=('Arial', 10), state='readonly')
        
        self.abrir_archivo_1 = Button(self.ventana, text = "Buscar", bg=self.color_principal, fg=self.color_texto, font=('Arial', 12))
        self.abrir_archivo_2 = Button(self.ventana, text = "Buscar", bg=self.color_principal, fg=self.color_texto, font=('Arial', 12))
        
        self.boton_ejecutar = Button(self.ventana, width=10, text='Listo', bg=self.color_principal, fg=self.color_texto, font=('Arial', 10))
        self.x = Entry(ventana)
        self.y = Entry(ventana)
        
        
    # FUNCIONES
        
    def ocultar_labels(self):
        self.lbl_menu.place_forget()
        self.btn_opcion_1.place_forget()
        self.btn_opcion_2.place_forget()
        self.btn_opcion_3.place_forget()
        
    def mostrar_labels(self):
        self.posicion_x = 150
        self.lbl_menu.place(x=self.posicion_x, y=30)
        self.btn_opcion_1.place(x=self.posicion_x+20, y=80)
        self.btn_opcion_2.place(x=self.posicion_x+20, y=160)
        self.btn_opcion_3.place(x=self.posicion_x+20, y=240)
        
    def borrar_entrys(self):
        self.nombre_archivo_1.config(state='normal')
        self.nombre_archivo_2.config(state='normal')
        self.nombre_archivo_1.delete(0, END)
        self.nombre_archivo_2.delete(0, END)
        self.nombre_archivo_1.config(state='readonly')
        self.nombre_archivo_2.config(state='readonly')
    
    def volver(self):
            self.lbl_archivo_1.place_forget()
            self.lbl_archivo_2.place_forget()
            self.nombre_archivo_1.place_forget()
            self.nombre_archivo_2.place_forget()
            self.boton_ejecutar.place_forget()
            self.boton_volver.place_forget()
            self.abrir_archivo_1.place_forget()
            self.abrir_archivo_2.place_forget()
            self.lbl_ancho_img.place_forget()
            self.ancho_img.place_forget()
            self.lbl_alto_img.place_forget()
            self.alto_img.place_forget()
            self.lbl_pagina_pdf.place_forget()
            self.pagina_pdf.place_forget()
            self.btn_seleccionar_coordenadas.place_forget()
            self.mostrar_labels()
            self.borrar_entrys()
                
    def opcion_1(self):
        self.ocultar_labels()
        self.posicion_x = 25
        
        def url():
            file_path = Operaciones.buscar_archivo()
            if file_path: 
                self.nombre_archivo_1.place(x=self.posicion_x+20, y=70)
                self.nombre_archivo_1.config(state='normal')
                self.nombre_archivo_1.insert(0, file_path)
                self.nombre_archivo_1.config(state='readonly')
        
        def url_2():
            file_path_2 = Operaciones.buscar_archivo()
            if file_path_2:
                self.nombre_archivo_2.place(x=self.posicion_x+20, y=140)
                self.nombre_archivo_2.config(state='normal')
                self.nombre_archivo_2.insert(0, file_path_2)
                self.nombre_archivo_2.config(state='readonly')
        
        def unir():
            pdf_1 = self.nombre_archivo_1.get()
            pdf_2 = self.nombre_archivo_2.get()
            if pdf_1 and pdf_2:
                Operaciones.unir_pdf(pdf_1, pdf_2)
                self.borrar_entrys()  
                self.mostrar_labels()
                self.volver()
                   
            else:
                messagebox.showwarning('Advertencia', 'Debes elegir los pdfs')
                
        self.lbl_archivo_1.place(x=self.posicion_x, y=30)
        self.lbl_archivo_2.place(x=self.posicion_x, y=100)
            
        self.abrir_archivo_1.config(command=url)
        self.abrir_archivo_1.place(x=self.posicion_x+350, y=30)
        
        self.abrir_archivo_2.config(command=url_2)
        self.abrir_archivo_2.place(x=self.posicion_x+350, y=100)
            
        self.boton_ejecutar.config(command=unir)
        self.boton_ejecutar.place(x=200, y=220)
        self.boton_volver.place(x=200, y=270)
        
    def opcion_2(self):
        self.ocultar_labels()
        self.posicion_x = 25
        
        def url():
            file_path = Operaciones.buscar_archivo()
            if file_path: 
                self.nombre_archivo_1.place(x=self.posicion_x+20, y=70)
                self.nombre_archivo_1.config(state='normal')
                self.nombre_archivo_1.insert(0, file_path)
                self.nombre_archivo_1.config(state='readonly')
                
        def separar():
            pdf = self.nombre_archivo_1.get()
            if pdf:
                Operaciones.separar_pdf(pdf)
                self.borrar_entrys()
                self.mostrar_labels()
                self.volver()
            else:
                messagebox.showwarning('Advertencia', 'Debes elegir el archivo pdf')
        
        self.lbl_archivo_1.place(x=self.posicion_x, y=30)
        
        self.abrir_archivo_1.config(command=url)
        self.abrir_archivo_1.place(x=self.posicion_x+350, y=30)
        
        self.boton_ejecutar.config(command=separar)
        self.boton_ejecutar.place(x=200, y=220)
        
        self.boton_volver.place(x=self.posicion_x + 175, y=270)   
    
    def opcion_3(self):
        self.ocultar_labels()
        self.posicion_x = 25
        
        def url():
            file_path = Operaciones.buscar_archivo()
            if file_path: 
                self.nombre_archivo_1.place(x=self.posicion_x+20, y=70)
                self.nombre_archivo_1.config(state='normal')
                self.nombre_archivo_1.insert(0, file_path)
                self.nombre_archivo_1.config(state='readonly')
                
        def url_2():
            file_path_2 = Operaciones.buscar_imagen()
            if file_path_2: 
                self.nombre_archivo_2.place(x=self.posicion_x+20, y=140)
                self.nombre_archivo_2.config(state='normal')
                self.nombre_archivo_2.insert(0, file_path_2)
                self.nombre_archivo_2.config(state='readonly')
            
        def firmar():
            pdf = self.nombre_archivo_1.get()
            img = self.nombre_archivo_2.get()
            ancho = self.ancho_img.get()
            alto = self.alto_img.get()
            x = self.x
            y = self.y
            pagina = self.pagina_pdf.get()
            
            if pdf and img and ancho and alto and x and y and pagina:
                Operaciones.firmar_pdf(pdf, img, x, y, ancho, alto, pagina)
                self.mostrar_labels()
                self.volver()
            else:
                messagebox.showwarning('Advertencia', 'Debes llenar los campos')
        
        def seleccionar_coordenada():
            pdf = self.nombre_archivo_1.get()
            ventana = self.ventana
            pagina = self.pagina_pdf.get()
            
            if pdf and ventana and pagina:
                self.x, self.y = Operaciones.abrir_pagina_pdf(pdf, ventana, pagina)
            else:
                messagebox.showwarning('Advertencia', 'Debes elegir el archivo y la página')
                
        self.lbl_archivo_1.place(x=self.posicion_x, y=30)
        self.lbl_archivo_2.configure(text="Abrir Imagen")
        self.lbl_archivo_2.place(x=self.posicion_x, y=100)
        
        self.abrir_archivo_1.config(command=url)
        self.abrir_archivo_1.place(x=self.posicion_x+350, y=30)
        
        self.abrir_archivo_2.config(command=url_2)
        self.abrir_archivo_2.place(x=self.posicion_x+350, y=100)

        self.lbl_ancho_img = Label(self.ventana, text="Ancho Imagen", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_ancho_img.place(x=self.posicion_x, y=170)
        self.ancho_img = Entry(self.ventana, width=10)
        self.ancho_img.place(x=self.posicion_x+150, y=175)
        
        self.lbl_alto_img = Label(self.ventana, text="Alto Imagen", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_alto_img.place(x=self.posicion_x+240, y=170)
        self.alto_img = Entry(self.ventana, width=10)
        self.alto_img.place(x=self.posicion_x+370, y=175)
        
        self.lbl_pagina_pdf = Label(self.ventana, text="Página en la que se firma", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_pagina_pdf.place(x=self.posicion_x+30, y=210)
        self.pagina_pdf = Entry(self.ventana, width=10)
        self.pagina_pdf.place(x=self.posicion_x+300, y=215)
        
        self.btn_seleccionar_coordenadas = Button(self.ventana, text = "Seleccionar posición", bg=self.color_principal, fg=self.color_texto, font=('Arial', 12), command=seleccionar_coordenada)
        self.btn_seleccionar_coordenadas.place(x=self.posicion_x + 140, y=250)
      
        self.boton_ejecutar.config(command=firmar)
        self.boton_ejecutar.place(x=self.posicion_x + 120, y=290)
        
        self.boton_volver.place(x=self.posicion_x + 235, y=290)   
        
        
                
                
        
        
        