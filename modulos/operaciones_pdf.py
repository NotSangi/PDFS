import fitz
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

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
        
        nombre_pdf = os.path.basename(pdf)
        nombre, extension = os.path.splitext(nombre_pdf)
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
        img_rect = fitz.Rect(x - ancho/2, y - ancho/2, x + ancho/2, y + alto/2)
        pagina.insert_image(img_rect, pixmap = imagen[0].get_pixmap(alpha=True))
        documento_pdf.save('pdf_firmado.pdf')
        documento_pdf.close()
        imagen.close()
        
        messagebox.showinfo('Informacion', 'Documento firmado correctamente')
    
    def buscar_archivo():
        file_path = filedialog.askopenfilename(
        initialdir ='C:/',
        title ='Selecciona un PDF',
        filetypes =[('PDF', '*.pdf')]
        )
        if not file_path:
            return
        
        return file_path
    
    def buscar_imagen():
        file_path = filedialog.askopenfilename(
        initialdir ='C:/',
        title ='Selecciona una imágen',
        filetypes =[('PNG', '*.png'), ('JPG', ('*.jpg', '*.jpeg'))]
        )
        if not file_path:
            return
        
        return file_path
    
    def abrir_pagina_pdf(pdf, ventana, pagina):
        doc = fitz.open(pdf)
        numero_pagina = int(pagina)
        page = doc[numero_pagina-1]
        mat = fitz.Matrix(1, 1) 
        pix = page.get_pixmap(matrix=mat)

        if pix.alpha:
            pix = fitz.Pixmap(fitz.csRGB, pix)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        top = Toplevel(ventana)
        top.title('Selecciona coordenadas del PDF')

        frame = Frame(top)
        frame.pack(fill=BOTH, expand=True)

        canvas = Canvas(frame, width=pix.width, height=pix.height, bg="gray")
        vbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)

        canvas.configure(yscrollcommand=vbar.set)
        vbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        tk_img = ImageTk.PhotoImage(img, master=canvas)
        canvas.create_image(0, 0, anchor='nw', image=tk_img)

        canvas.config(scrollregion=(0, 0, pix.width, pix.height))

        canvas._image_ref = tk_img 

        def click(event):
            global x, y
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)

            r = 3
            ovalo = canvas.create_oval(x-r, y-r, x+r, y+r, outline="red", width=2)
            respuesta = messagebox.askyesno('Coordenadas Elegidas', '¿Quieres elegir estas coordenadas para firmar?')
            if respuesta:
                top.destroy()
            else:
                canvas.delete(ovalo)
                del x, y
        
        canvas.bind("<Button-1>", click)

        top.wait_window()
        
        try:
            return x, y
        except:
            print('Coordenadas no elegidas')
            

    
    