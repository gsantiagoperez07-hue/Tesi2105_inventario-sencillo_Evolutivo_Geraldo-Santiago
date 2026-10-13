# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("849x426")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))


style = ttk.Style(main)
style.theme_use("clam")

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)

style.configure("entry.TEntry", fieldbackground="#fff", foreground="#000")

entry = ttk.Entry(master=main, style="entry.TEntry")
entry.place(x=12, y=130, width=200, height=30)

style.configure("entry1.TEntry", fieldbackground="#fff", foreground="#000")

entry1 = ttk.Entry(master=main, style="entry1.TEntry")
entry1.place(x=9, y=76, width=200, height=30)

style.configure("entry2.TEntry", fieldbackground="#fff", foreground="#000")

entry2 = ttk.Entry(master=main, style="entry2.TEntry")
entry2.place(x=2, y=187, width=200, height=30)

style.configure("entry3.TEntry", fieldbackground="#fff", foreground="#000")

entry3 = ttk.Entry(master=main, style="entry3.TEntry")
entry3.place(x=26, y=32, width=200, height=30)

style.configure("entry4.TEntry", fieldbackground="#fff", foreground="#000")

entry4 = ttk.Entry(master=main, style="entry4.TEntry")
entry4.place(x=8, y=241, width=200, height=30)

style.configure("button.TButton", background="#E4E2E2", foreground="#000")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Registrar", style="button.TButton")
button.place(x=12, y=281, width=80, height=40)

style.configure("label.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label = ttk.Label(master=main, text="Nombre:", style="label.TLabel")
label.configure(anchor="center")
label.place(x=236, y=18, width=80, height=40)

style.configure("label1.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label1 = ttk.Label(master=main, text="RAM:", style="label1.TLabel")
label1.configure(anchor="center")
label1.place(x=232, y=71, width=80, height=40)

style.configure("label2.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label2 = ttk.Label(master=main, text="Estado:", style="label2.TLabel")
label2.configure(anchor="center")
label2.place(x=229, y=126, width=80, height=40)

style.configure("label3.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label3 = ttk.Label(master=main, text="Tipo de identificador:", style="label3.TLabel")
label3.configure(anchor="center")
label3.place(x=242, y=188, width=80, height=40)

style.configure("label4.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label4 = ttk.Label(master=main, text="Valor del identificador:", style="label4.TLabel")
label4.configure(anchor="center")
label4.place(x=235, y=244, width=80, height=40)

style.configure("label5.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label5 = ttk.Label(master=main, text="Resultado:", style="label5.TLabel")
label5.configure(anchor="center")
label5.place(x=14, y=339, width=550, height=40)

def registrar_equipo():
    nombre = entry.get()
    ram = entry1.get()
    estado = entry2.get()
    tipo = entry3.get()
    valor = entry4.get()
    
    equipo = {
        "nombre": nombre,
        "ram": ram,
        "estado": estado
    }
    
    dato_alternativo = {"tipo": tipo, "valor": valor}
    
    texto = (f"{equipo['nombre']} | {equipo['ram']} GB | "
             f"{equipo['estado']}: "
             f"{dato_alternativo['valor']}"
             )
    label5.config(text=texto)
    
button.config(command=registrar_equipo)
main.mainloop()