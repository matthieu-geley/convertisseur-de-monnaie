import tkinter as tk
from tkinter import ttk
from tkinter import *

entree=tk.StringVar


win = tk.Tk()
win.title(' Convertisseur de devises ')
win.configure(bg="grey")
window_width = 500
window_height = 600
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
win.iconbitmap('./ico/gui.ico')
tk.Label(win, text='La Plateforme.io : Convertisseur de Devise', bg='#ba5e18', font=('Courier 14 underline')).pack(anchor=NW, ipady=1, ipadx=1)

tk.Label(win, text='Valeur à convertir : ', bg='grey').pack(pady=(25, 0))

a=Entry(win, width = 15)
a.pack()

tk.Label(win, text='De cette devise : ', bg='grey').pack(pady=(25, 0))
listeDevise=["Euro (€)","Dollar US ($)","Livre Sterlings (£)"]
i = listeDevise
listeCombo1 = ttk.Combobox(win, values=i, state="readonly")
listeCombo1.current(None)
listeCombo1.pack()

tk.Label(win, text='Vers cette devise : ', bg='grey').pack(pady=(25, 0))
j = listeDevise
listeCombo2 = ttk.Combobox(win,  values=j, state="readonly")
listeCombo2.current(None)
listeCombo2.pack()

tk.Label(win, text='Conversion : ', bg='grey').pack(pady=(10, 0))
Tot = Text(win, state='disabled', width=15, height=1)
Tot.configure(state='normal')
Tot.config(state=DISABLED, font=('Calibri 15'))
Tot.pack()

def Conv():
    dollar = 1.08
    livre = 0.89
    resultat = 0
    integral=a.get()
    valeur=float(integral)
    if i == 0 and j == 1:
        resultat=valeur * dollar
    elif j == 2:
        resultat=valeur * livre
    elif i == 1 and j == 0:
        resultat=valeur / dollar
    elif j == 2:
        resultat=valeur * livre
    elif i == 2 and j == 0:
        resultat=valeur / livre
    elif j == 1:
        resultat=valeur * dollar
    elif i == j:
        resultat = ("erreur: conversion inutile, la même devise est sélectionnée en entrée et en sortie.")
    print(resultat)

button = ttk.Button(win, text="Convertir", command =Conv)
button.pack(pady=(15, 5))

#tk.Label(win, text='Taux de conversion : ', bg='grey').pack(pady=(10, 0))
#taux = Text(win, state='disabled', width=10, height=1)
#taux.configure(state='normal')
#taux.insert('end', '')
#taux.config(state=DISABLED)
#taux.pack()

#tk.Label(win, text='Baril de pétrole : ', bg='grey').pack(pady=(10, 0))
#Bar = Text(win, state='disabled', width=15, height=1)
#Bar.configure(state='normal')
#Bar.insert('end', '')
#Bar.config(state=DISABLED)
#Bar.pack()

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    win.mainloop()