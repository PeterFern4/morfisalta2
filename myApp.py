import tkinter
import customtkinter
import json
from tkinter import messagebox
from Entidades.usuario import Usuario
from customtkinter import CTkFrame, CTkImage
from PIL import ImageTk, Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
#===============================================VENTANA
app = customtkinter.CTk()
app.geometry('700x500')
app.resizable(False, False)

#===============================================FRAME SUPERIOR
frame_titulo = customtkinter.CTkFrame(master=app, width=700, height=100, corner_radius=10, bg_color='red')
frame_titulo.pack(padx=0, pady=0)

imagen_fondo = Image.open("Imagenes\Titulo.jpg")
fondo_titulo = CTkImage(imagen_fondo, size=(700, 100))
label_fondo = customtkinter.CTkLabel(frame_titulo, text="", image=fondo_titulo, anchor="nw")
label_fondo.pack(fill="both", expand=True)

#===============================================FRAME INFERIOR PRINCIPAL
frame_principal = customtkinter.CTkFrame(master=app, width=700, height=400, corner_radius=10, bg_color='gold')
frame_principal.pack(padx=0, pady=0)

canvas = customtkinter.CTkCanvas(frame_principal, width=700, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

imagen_frameP = Image.open(r"Imagenes\fondo_frameP.jpg")
fondo_frameP = ImageTk.PhotoImage(imagen_frameP)

canvas.create_image(0, 0, anchor="nw", image=fondo_frameP)

#------------------------INICIAR SESION
def iniciar_sesion():
    iniciarSesion = customtkinter.CTkToplevel()
    iniciarSesion.title("Ingreso de Usuario")
    iniciarSesion.geometry("300x150")

    label_id = customtkinter.CTkLabel(iniciarSesion, text="Ingrese DNI")
    label_id.pack(pady=10)

    entry_id = customtkinter.CTkEntry(iniciarSesion, placeholder_text='Sin puntos')
    entry_id.pack(pady=10)

    boton_validar = customtkinter.CTkButton(iniciarSesion, text="Aceptar", command=lambda: validar_ingreso(entry_id.get()),fg_color='orange',hover_color ='orange3', text_color='black')
    boton_validar.pack(pady=10)

    def validar_ingreso(id_usuario):
        with open(r"DatosJson\usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario["ID"] == id_usuario:
                messagebox.showinfo("EUREKA!","Inicio de sesión exitoso.")
                iniciarSesion.destroy()
                break
        else:
            messagebox.showerror("Error", "No estás registrado.")
            iniciarSesion.destroy()

#------------------------REGISTRO DE USUARIOS
def registro_usuario():
    registrarUsuario = customtkinter.CTkToplevel()
    registrarUsuario.title("Alta de Usuario")
    registrarUsuario.geometry("300x225")

    id_entry_reg = customtkinter.CTkEntry(registrarUsuario, placeholder_text='Ingrese DNI sin puntos')
    id_entry_reg.pack(pady=10)
    
    nombre_entry_reg = customtkinter.CTkEntry(registrarUsuario, placeholder_text='Nombre')
    nombre_entry_reg.pack(pady=10)

    apellido_entry_reg = customtkinter.CTkEntry(registrarUsuario, placeholder_text='Apellido')
    apellido_entry_reg.pack(pady=10)

    boton_validar = customtkinter.CTkButton(registrarUsuario, text="Aceptar", command=lambda: alta_usuario(id_entry_reg.get(), nombre_entry_reg.get(), apellido_entry_reg.get()),fg_color='orange',hover_color ='orange3', text_color='black')
    boton_validar.pack(pady=10)

    def alta_usuario(id, nombre, apellido):
        usuLista = []
        with open("DatosJson/usuarios.json", "r") as archivo:
            usuarios_json = json.load(archivo)
            for usuario in usuarios_json:
                usuLista.append(Usuario.from_json(usuario))

        nuevoUsuario = Usuario(id, nombre.title(), apellido.title(), historial_rutas=[])
        usuLista.append(nuevoUsuario)

        with open("DatosJson/usuarios.json", "w") as archivo:
            lista = []
            for usuario in usuLista:
                lista.append(usuario.a_json())
            json.dump(lista, archivo, indent =3)
        messagebox.showinfo("EUREKA!","¡Registro exitoso!")
        registrarUsuario.destroy()
    
#------------------------BOTONES FRAME PRINCIPAL
boton_ingresar = customtkinter.CTkButton(frame_principal, text='Ingresar', command=iniciar_sesion, fg_color='orange',hover_color ='orange3', text_color='black')
boton_ingresar.place(relx=0.2, rely=0.8, anchor=tkinter.CENTER)

boton_ingresar = customtkinter.CTkButton(frame_principal, text='Registrarse', command=registro_usuario, fg_color='orange',hover_color ='orange3', text_color='black')
boton_ingresar.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)



#===============================================FRAME INFERIOR USUARIOS
frame_usuario = customtkinter.CTkFrame(master=app, width=700, height=400, corner_radius=10, bg_color='gold')
frame_usuario.pack(padx=0, pady=0)

canvas = customtkinter.CTkCanvas(frame_usuario, width=700, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

imagen_frameU = Image.open(r"Imagenes\fondo_frameP.jpg")
fondo_frameU = ImageTk.PhotoImage(imagen_frameU)

canvas.create_image(0, 0, anchor="nw", image=fondo_frameU)








def ajustar_frame(frame):
        frame.pack(padx=20, pady=20)

def cambiar_frame(frame_destino):
        frame_destino.tkraise()

app.cambiar_Frame(frame_principal)


app.mainloop()
