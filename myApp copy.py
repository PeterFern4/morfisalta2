import tkinter
import customtkinter
import json
from tkinter import messagebox
from Entidades.usuario import Usuario
from customtkinter import CTkFrame, CTkImage, CTkCanvas
from PIL import ImageTk, Image
import customtkinter as ctk
from tkintermapview import TkinterMapView


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')



#===============================================VENTANA
class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('MORFI Salta')
        self.iconbitmap("Imagenes\icono.ico")
        self.geometry('700x500+350+120')
        self.resizable(False, False)
        self.iniciar()
        self.cambiar_frame(self.frame_principal)
        self.id_usuario_comp = None
        

    def iniciar(self):    
            self.frame_titulo = FrameTitulo(self)
            self.frame_principal = FramePrincipal(self)
            self.frame_usuario = FrameUsuario(self)

            self.frame_titulo.pack(fill="both", expand=False)
            self.frame_principal.pack(fill="both", expand=True)
            self.frame_usuario.pack(fill="both", expand=True)

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()

    def ajustar_frame(frame):
        frame.pack(padx=0, pady=0)



#===============================================FRAME SUPERIOR
class FrameTitulo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=100)
        
        imagen_fondo = Image.open("Imagenes\Titulo.jpg")
        fondo_titulo = CTkImage(imagen_fondo, size=(700, 100))
        self.label_fondo = customtkinter.CTkLabel(self, text="", image=fondo_titulo, anchor="nw")
        self.label_fondo.pack(fill="both", expand=True)



#===============================================FRAME INFERIOR PRINCIPAL
class FramePrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=400)
        self.master = master

        self.canvas = customtkinter.CTkCanvas(self, width=700, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        imagen_frameP = Image.open(r"Imagenes\fondo_frameP.jpg")
        self.fondo_frameP = ImageTk.PhotoImage(imagen_frameP)

        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_frameP)

        
#------------------------INICIAR SESION
        def iniciar_sesion():
            iniciarSesion = customtkinter.CTkToplevel()
            iniciarSesion.title("Ingreso de Usuario")
            iniciarSesion.geometry("300x150+550+295")

            iniciarSesion.grab_set()

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
                        iniciarSesion.after(0, iniciarSesion.destroy)
                        FramePrincipal.pack_forget(self)
                        FrameUsuario.pack(self, fill="both", expand=True)
                        break
                else:
                    messagebox.showerror("Error", "No estás registrado.")
                    iniciarSesion.after(0, iniciarSesion.destroy)

        boton_ingresar = customtkinter.CTkButton(self, text='Ingresar', command= iniciar_sesion, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_ingresar.place(relx=0.2, rely=0.8, anchor=tkinter.CENTER)
#------------------------REGISTRO DE USUARIOS
        def registro_usuario():
            registrarUsuario = customtkinter.CTkToplevel()
            registrarUsuario.title("Alta de Usuario")
            registrarUsuario.geometry("300x225+550+295")

            registrarUsuario.grab_set()

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
                registrarUsuario.after(0, registrarUsuario.destroy)
    
        boton_ingresar = customtkinter.CTkButton(self, text='Registrarse', command= registro_usuario, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_ingresar.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)





#===============================================FRAME INFERIOR USUARIOS
class FrameUsuario(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=400)
        self.master = master

        self.canvas = customtkinter.CTkCanvas(self, width=700, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        imagen_frameP = Image.open(r"Imagenes\fondo_frameU.jpg")
        self.fondo_frameP = ImageTk.PhotoImage(imagen_frameP)
        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_frameP)

        
        
#------------------------MOSTRAR DESTINOS EN LISTA
        with open("DatosJson/destinos_culinarios.json", "r") as archivo:
            destinos = json.load(archivo)
            lista_destinos = []
            for destino in destinos:
                lista_destinos.append(destino["Nombre"])       

     
        def mostrar_informacion(self):
            destino_seleccionado = opcion_seleccionada.get()
            if destino_seleccionado:
                informacionDestino = customtkinter.CTkToplevel()
                informacionDestino.title("Información del Lugar")
                informacionDestino.geometry("600x300+430+180")
                informacionDestino.grab_set()

                frame_info = customtkinter.CTkFrame(informacionDestino, width=600, height=300)
                frame_info.pack(padx=0, pady=0)

                info_label = customtkinter.CTkLabel(frame_info, width=600, height=300)
                info_label.pack(fill="both", expand=True)
                                
                for destino in destinos:
                    if destino['Nombre'] == destino_seleccionado[1]:
                        print(destino['Nombre'])
                        info = f"Nombre: {destino['Nombre']}\nTipo de Cocina:{destino['Tipo de Cocina']}\nIngredientes: {destino['Ingredientes']}\nPrecio Mínimo: {destino['Precio Minimo']}\nPrecio Máximo: {destino['Precio Maximo']}\nPopularidad: {destino['Popularidad']}\nDisponibilidad: {destino['Disponibilidad']}"
                        info_label["text"]=info


                boton_mapa = customtkinter.CTkButton(frame_info, text="Ver en Mapa", fg_color='orange',hover_color ='orange3', text_color='black')
                boton_mapa.place(relx=0.01, rely=0.88)

                boton_agregar_ruta = customtkinter.CTkButton(frame_info, text="Agregar a Mi Ruta", fg_color='orange',hover_color ='orange3', text_color='black')
                boton_agregar_ruta.place(relx=0.26, rely=0.88)

                boton_calificar = customtkinter.CTkButton(frame_info, text="Calificar Lugar", fg_color='orange',hover_color ='orange3', text_color='black')
                boton_calificar.place(relx=0.51, rely=0.88)

#------------------------CERRAR VENTANA
                def cerrar_ventana():
                    informacionDestino.after(0, informacionDestino.destroy)

                boton_cerrar = customtkinter.CTkButton(frame_info, text="Cerrar", command= cerrar_ventana, fg_color='red2',hover_color ='red4', text_color='black')
                boton_cerrar.place(relx=0.76, rely=0.88)


        opcion_seleccionada = customtkinter.StringVar()
        opciones_destinos = customtkinter.CTkOptionMenu(self, values=lista_destinos, variable=opcion_seleccionada, fg_color='orange', text_color='black')
        opciones_destinos.set("Elegir Destino")
        opciones_destinos.place(relx=0.055, rely=0.045, anchor='nw')
        opciones_destinos.bind("<Button-1>", mostrar_informacion)
                
        
#------------------------EXPLORAR MAPA        
        def explorar_mapa():
            exp_mapa = TkinterMapView(self, width=490, height=320, corner_radius=0)
            exp_mapa.place(relx=0.04, rely=0.15, anchor = "nw")
            exp_mapa.set_address("Salta, Salta")
            exp_mapa.set_zoom(15)
            exp_mapa.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            

            

        boton_explorar = customtkinter.CTkButton(self, text='Explorar Mapa', command= explorar_mapa, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_explorar.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)
        
        boton_profile = customtkinter.CTkButton(self, text='Mi Cuenta', fg_color='orange',hover_color ='orange3', text_color='black')
        #command= explorar_mapa, 
        boton_profile.place(relx=0.86, rely=0.08, anchor=tkinter.CENTER)

#------------------------CERRAR SESION
        def cerrar_sesion():
            FrameUsuario.pack_forget(self)
            FramePrincipal.pack(self, fill="both", expand=True)

        boton_logout = customtkinter.CTkButton(self, text='Cerrar Sesión', command= cerrar_sesion, fg_color='red2',hover_color ='red4', text_color='black')
        boton_logout.place(relx=0.86, rely=0.92, anchor=tkinter.CENTER)










if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
