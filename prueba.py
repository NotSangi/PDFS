from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import fitz

ventana = Tk()
ventana.geometry('600x500')
ventana.title('Selector de PDF')

ruta_var = StringVar(value='(sin archivo)')
Label(ventana, textvariable=ruta_var, font=('Arial', 12), wraplength=560, justify='left').pack(pady=10)

def select():
    file_path = filedialog.askopenfilename(
        parent=ventana,
        initialdir='C:/',
        title='Selecciona un PDF',
        filetypes=[('PDF', '*.pdf')]
    )
    if not file_path:
        return

    ruta_var.set(file_path)

    # Abrir PDF y renderizar 1ª página
    doc = fitz.open(file_path)
    page = doc[0]
    mat = fitz.Matrix(1, 1)  # zoom x2
    pix = page.get_pixmap(matrix=mat)

    # Asegurar RGB (quitar alfa si existe)
    if pix.alpha:
        pix = fitz.Pixmap(fitz.csRGB, pix)

    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # >>> IMPORTANTE: usar Toplevel, NO crear otro Tk <<<
    top = Toplevel(ventana)
    top.title('Selecciona coordenadas del PDF')

    canvas = Canvas(top, width=pix.width, height=pix.height)
    canvas.pack()

    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor='nw', image=tk_img)

    # Mantener referencia para que no se destruya
    canvas._image_ref = tk_img  # o top._image_ref = tk_img
    
    cont = 0
    def click(event):
        
        if cont == 0:
            x, y = event.x, event.y
            print(f'Coordenadas Click: {x}, {y}')
            r = 5
            canvas.create_oval(x-r, y-r, x+r, y+r, outline="red", width=2)
            respuesta = messagebox.askyesno('Coordenadas Elegidas', 'Quieres elegir estas coordenadas para firmar?')
            print(respuesta) #Booleano
        

    canvas.bind("<Button-1>", click)

Button(ventana, text='Seleccionar Archivo', command=select).pack(pady=10)

ventana.mainloop()

