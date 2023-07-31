import tkinter
import customtkinter
import json
from tkinter import messagebox
from Entidades.usuario import Usuario
from customtkinter import CTkFrame, CTkImage
from PIL import ImageTk, Image
import customtkinter as ctk

class FrameTitulo(ctk.CTk):
    def __init__(self):
        super().__init__(master, height=100)

Frame_titulo = customtkinter.CTkFrame(master=app, width=700, height=100, corner_radius=10, bg_color='red')
frame_titulo.pack(padx=0, pady=0)

imagen_fondo = Image.open("Imagenes\Titulo.jpg")
fondo_titulo = CTkImage(imagen_fondo, size=(700, 100))
label_fondo = customtkinter.CTkLabel(frame_titulo, text="", image=fondo_titulo, anchor="nw")
label_fondo.pack(fill="both", expand=True)