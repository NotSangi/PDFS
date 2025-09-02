from tkinter import *
from tkinter import messagebox
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
        
        #Etiquetas
        self.lbl_menu = Label(ventana, text="¿Qué deseas realizar?", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_menu.place(x=self.posicion_x, y=30)
        self.lbl_opcion_1 = Label(ventana, text="1. Juntar PDF's", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_opcion_1.place(x=self.posicion_x+20, y=80)
        self.lbl_opcion_2 = Label(ventana, text="2. Separar PDF", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_opcion_2.place(x=self.posicion_x+20, y=130)
        self.lbl_opcion_3 = Label(ventana, text="3. Firmar PDF",bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_opcion_3.place(x=self.posicion_x+20, y=180)

        
        self.opcion = Entry(ventana)
        self.opcion.place(x=self.posicion_x+40, y=250)
        
        self.boton_opcion = Button(ventana, width=10, text="Elegir", bg=self.color_principal, fg=self.color_texto, font=('Arial', 10), command=self.opcion_elegida)
        self.boton_opcion.place(x=self.posicion_x+55, y=280)
        
        self.boton_volver = Button(self.ventana, width=10, text='Volver', bg=self.color_principal, fg=self.color_texto, font=('Arial', 10), command=self.volver)
        
        
    def opcion_elegida(self):
        if self.opcion.get() == '1':
            self.opcion_1()
        elif self.opcion.get() == '2':
            self.opcion_2()
        elif self.opcion.get() == '3':
            self.opcion_3()
            
    def ocultar_labels(self):
        self.lbl_menu.place_forget()
        self.lbl_opcion_1.place_forget()
        self.lbl_opcion_2.place_forget()
        self.lbl_opcion_3.place_forget()
        self.opcion.place_forget()
        self.boton_opcion.place_forget()
    
    def mostrar_labels(self):
        self.posicion_x = 150
        self.lbl_menu.place(x=self.posicion_x, y=30)
        self.lbl_opcion_1.place(x=self.posicion_x+20, y=80)
        self.lbl_opcion_2.place(x=self.posicion_x+20, y=130)
        self.lbl_opcion_3.place(x=self.posicion_x+20, y=180)
        self.opcion.place(x=self.posicion_x+40, y=250)
        self.boton_opcion.place(x=self.posicion_x+55, y=280)
    
    def volver(self):
        if self.opcion.get() == '1':
            self.lbl_pdf_1.place_forget()
            self.lbl_pdf_2.place_forget()
            self.nombre_pdf_1.place_forget()
            self.nombre_pdf_2.place_forget()
            self.boton_unir.place_forget()
            self.boton_volver.place_forget()
            self.opcion.delete(0, END)
            self.mostrar_labels()
        elif self.opcion.get() == '2':
            self.lbl_pdf.place_forget()
            self.nombre_pdf.place_forget()
            self.boton_separar.place_forget()
            self.boton_volver.place_forget()
            self.mostrar_labels()
            self.opcion.delete(0, END)
        elif self.opcion.get() == '3':
            self.lbl_pdf.place_forget()
            self.nombre_pdf.place_forget()
            self.lbl_img.place_forget()
            self.nombre_img.place_forget()
            self.lbl_ancho_img.place_forget()
            self.ancho_img.place_forget()
            self.lbl_alto_img.place_forget()
            self.alto_img.place_forget()
            self.lbl_x_img.place_forget()
            self.x_img.place_forget()
            self.lbl_y_img.place_forget()
            self.y_img.place_forget()
            self.boton_firmar.place_forget()
            self.boton_volver.place_forget()
            self.lbl_pagina_pdf.place_forget()
            self.pagina_pdf.place_forget()

            self.mostrar_labels()
            self.opcion.delete(0, END)
                
    def opcion_1(self):
        self.ocultar_labels()
        self.posicion_x = 25
        
        self.lbl_pdf_1 = Label(self.ventana, text="Ingresa el nombre del pdf 1 con su extensión (.pdf)", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_pdf_1.place(x=self.posicion_x, y=30)
        self.nombre_pdf_1 = Entry(self.ventana, width=50)
        self.nombre_pdf_1.place(x=self.posicion_x + 75, y=80)
        
        self.lbl_pdf_2 = Label(self.ventana, text="Ingresa el nombre del pdf 2 con su extensión (.pdf)", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_pdf_2.place(x=self.posicion_x, y=120)
        self.nombre_pdf_2 = Entry(self.ventana, width=50)
        self.nombre_pdf_2.place(x=self.posicion_x + 75, y=170)
        
        def unir():
            pdf_1 = self.nombre_pdf_1.get()
            pdf_2 = self.nombre_pdf_2.get()
            if pdf_1 and pdf_2:
                Operaciones.unir_pdf(pdf_1, pdf_2)
                self.mostrar_labels()
                self.volver()         
            else:
                messagebox.showwarning('Advertencia', 'Debes llenar los campos')
            
        self.boton_unir = Button(self.ventana, width=10, text='Unir', bg=self.color_principal, fg=self.color_texto, font=('Arial', 10), command=unir)
        self.boton_unir.place(x=200, y=220)
        
        self.boton_volver.place(x=200, y=270)
        
    def opcion_2(self):
        self.ocultar_labels()
        self.posicion_x = 25
        
        self.lbl_pdf = Label(self.ventana, text="Ingresa el nombre del pdf con su extensión (.pdf)", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_pdf.place(x=self.posicion_x, y=30)
        self.nombre_pdf = Entry(self.ventana, width=50)
        self.nombre_pdf.place(x=self.posicion_x + 75, y=80)
        
        def separar():
            pdf = self.nombre_pdf.get()
            if pdf:
                Operaciones.separar_pdf(pdf)
                self.mostrar_labels()
                self.volver()
                
            else:
                messagebox.showwarning('Advertencia', 'Debes llenar los campos')
            
        self.boton_separar = Button(self.ventana, width=10, text='Separar', bg=self.color_principal, fg=self.color_texto, font=('Arial', 10), command=separar)
        self.boton_separar.place(x=self.posicion_x + 175, y=220)
        
        self.boton_volver.place(x=self.posicion_x + 175, y=270)   
    
    def opcion_3(self):
        self.ocultar_labels()
        self.posicion_x = 25
        
        self.lbl_pdf = Label(self.ventana, text="Ingresa el nombre del pdf con su extensión (.pdf)", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_pdf.place(x=self.posicion_x, y=10)
        self.nombre_pdf = Entry(self.ventana, width=50)
        self.nombre_pdf.place(x=self.posicion_x + 75, y=50)
        
        self.lbl_img = Label(self.ventana, text="Nombre de la imagen con su extensión (.png/.jpg)", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_img.place(x=self.posicion_x+10, y=80)
        self.nombre_img = Entry(self.ventana, width=50)
        self.nombre_img.place(x=self.posicion_x + 75, y=120)
        
        self.lbl_ancho_img = Label(self.ventana, text="Ancho Imagen", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_ancho_img.place(x=self.posicion_x, y=150)
        self.ancho_img = Entry(self.ventana, width=10)
        self.ancho_img.place(x=self.posicion_x+150, y=155)
        
        self.lbl_alto_img = Label(self.ventana, text="Alto Imagen", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_alto_img.place(x=self.posicion_x, y=180)
        self.alto_img = Entry(self.ventana, width=10)
        self.alto_img.place(x=self.posicion_x+150, y=185)
        
        self.lbl_x_img = Label(self.ventana, text="Posición en X", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_x_img.place(x=self.posicion_x+250, y=150)
        self.x_img = Entry(self.ventana, width=10)
        self.x_img.place(x=self.posicion_x+380, y=155)
        
        self.lbl_y_img = Label(self.ventana, text="Posición en Y", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_y_img.place(x=self.posicion_x+250, y=180)
        self.y_img = Entry(self.ventana, width=10)
        self.y_img.place(x=self.posicion_x+380, y=185)
        
        self.lbl_pagina_pdf = Label(self.ventana, text="Página en la que se firma", bg=self.color_principal, fg=self.color_texto, font=('Arial', 15))
        self.lbl_pagina_pdf.place(x=self.posicion_x+30, y=210)
        self.pagina_pdf = Entry(self.ventana, width=10)
        self.pagina_pdf.place(x=self.posicion_x+300, y=215)
        
        
        def firmar():
            pdf = self.nombre_pdf.get()
            img = self.nombre_img.get()
            ancho = self.ancho_img.get()
            alto = self.alto_img.get()
            x = self.x_img.get()
            y = self.y_img.get()
            pagina = self.pagina_pdf.get()
            
            if pdf and img and ancho and alto and x and y and pagina:
                Operaciones.firmar_pdf(pdf, img, x, y, ancho, alto, pagina)
                self.mostrar_labels()
                self.volver()
            else:
                messagebox.showwarning('Advertencia', 'Debes llenar los campos')
                
        
        self.boton_firmar = Button(self.ventana, width=10, text='Firmar', bg=self.color_principal, fg=self.color_texto, font=('Arial', 10), command=firmar)
        self.boton_firmar.place(x=self.posicion_x + 130, y=270)
        
        self.boton_volver.place(x=self.posicion_x + 235, y=270)   
        
        
                
                
        
        
        