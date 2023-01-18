import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title(' Convertisseur de devises ')
root.configure(bg="grey")
window_width = 500
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('./ico/gui.ico')
tk.Label(root, text='La Plateforme.io : Convertisseur de Devise', bg='#ba5e18', font=('Courier 14 underline')).pack(anchor=NW, ipady=1, ipadx=1)

tk.Label(root, text='Valeur à convertir : ', bg='grey').pack(pady=(25, 0))
T1 = Entry(root, width = 15,)
T1.pack()
tk.Label(root, text='De cette devise : ', bg='grey').pack(pady=(25, 0))
listeDevise=["Euro (€)","Dollar US ($)","Livre Sterlings (£)"]
listeCombo1 = ttk.Combobox(root,  values=listeDevise, state="readonly")
listeCombo1.current(0)
listeCombo1.pack()

tk.Label(root, text='Vers cette devise : ', bg='grey').pack(pady=(25, 0))
listeCombo2 = ttk.Combobox(root,  values=listeDevise, state="readonly")
listeCombo2.current(2)
listeCombo2.pack()

def Conv():
    dollar = 1.08
    livre = 0.89
    i = listeCombo1.get()
    j = listeCombo2.get()
    valeur = T1.get()

    if i == j:
        print("erreur: conversion inutile, la même devise est sélectionnée en entrée et en sortie.")
    if i == 0:
        if j == 1:
            print(float(valeur) * float(dollar))
        elif j == 2:
            print(float(valeur) * float(livre))
    elif i == 1:
        if j == 0:
            print(float(valeur) / float(dollar))
        elif j == 2:
            print(float(valeur) * float(livre))
    elif i == 2:
        if j == 0:
            print(float(valeur) / float(livre))
        elif j == 1:
            print(float(valeur) * float(dollar))

def Conversion():
    Conv()
button = ttk.Button(root, text="Convertir", command = Conv())
button.pack(pady=(15, 5))

tk.Label(root, text='Taux de conversion : ', bg='grey').pack(pady=(10, 0))
taux = Text(root, state='disabled', width=10, height=1)
taux.configure(state='normal')
taux.insert('end', '')
taux.config(state=DISABLED)
taux.pack()

tk.Label(root, text='Conversion : ', bg='grey').pack(pady=(10, 0))
Tot = Text(root, state='disabled', width=15, height=1)
Tot.configure(state='normal')
Tot.insert('end', '')
Tot.config(state=DISABLED)
Tot.pack()

tk.Label(root, text='Baril de pétrole : ', bg='grey').pack(pady=(10, 0))
Bar = Text(root, state='disabled', width=15, height=1)
Bar.configure(state='normal')
Bar.insert('end', '')
Bar.config(state=DISABLED)
Bar.pack()

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()