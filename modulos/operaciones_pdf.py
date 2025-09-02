import fitz
import os
from tkinter import *
from tkinter import messagebox

class Operaciones():
    
    def unir_pdf(documento_pdf_1, documento_pdf_2):
        pdf_1 = fitz.open(documento_pdf_1)
        pdf_2 = fitz.open(documento_pdf_2)
        
        pdf_unido = fitz.open()
        pdf_unido.insert_pdf(pdf_1)
        pdf_unido.insert_pdf(pdf_2)
        
        pdf_unido.save('pdf_unido.pdf')
        pdf_1.close()
        pdf_2.close()
        messagebox.showinfo('Información', 'PDF Unido correctamente')
        
    def separar_pdf(pdf):
        documento_pdf = fitz.open(pdf)
    
        if len(documento_pdf) < 2:
            messagebox.showwarning('Advertencia', 'No se puede dividir el pdf, solo es 1 página')
            return

        nombre, extension = os.path.splitext(pdf)
        os.makedirs(f'{nombre}_separado')
        
        for i in range(len(documento_pdf)):
            pagina_individual = fitz.open()
            pagina_individual.insert_pdf(documento_pdf, from_page=i, to_page=i)
            
            if i < 9:
                nombre_pagina = f'0{i+1}_{nombre}{extension}'
            else:
                nombre_pagina = f'{i+1}_{nombre}{extension}'
            
            os.chdir(f'{nombre}_separado')
            pagina_individual.save(nombre_pagina)
            
            pagina_individual.close()
            os.chdir('../')
            
        documento_pdf.close()
        messagebox.showinfo('Informacion', f'Documento divido, se creo la carpeta {nombre}_separado')
    
    def firmar_pdf(pdf_original, imagen_png, x, y, ancho, alto, numero_pagina):
        
        x = int(x)
        y = int(y)
        ancho = int(ancho)
        alto = int(alto)
        numero_pagina = int(numero_pagina)
        
        documento_pdf = fitz.open(pdf_original)
        imagen = fitz.open(imagen_png)
        pagina = documento_pdf[numero_pagina-1]
        img_rect = fitz.Rect(x,y,x+ancho,y+alto)
        pagina.insert_image(img_rect, pixmap = imagen[0].get_pixmap(alpha=True))
        documento_pdf.save('pdf_firmado.pdf')
        documento_pdf.close()
        imagen.close()
        
        messagebox.showinfo('Informacion', 'Documento firmado correctamente')
        