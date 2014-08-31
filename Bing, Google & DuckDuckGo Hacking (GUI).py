#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import webbrowser

def mostrar(window): 
	 window.deiconify()

def ocultar(window):
	 window.withdraw()

def ejecutar(f): 
	 ventana.after(0,f)

def search(peticion):
	google =  "https://www.google.com/?#q="+ peticion
	bing = "https://www.bing.com/search?q="+ peticion
	duckgo = "https://duckduckgo.com/?q="+ peticion
	list = [google,bing,duckgo]
	for item in list:
		webbrowser.open(item)
	caja.delete(0,END)

if __name__ == "__main__":
	ventana = Tk()
	ventana.title('Browser Hacking')
	ventana.config(bg='Black')

	#ventana
	label= Label(ventana, text= 'Bing, Google & DuckDuckGo Hacking',bg="black" ,fg= 'white', font=('Verdana', 20, 'bold'))
	label.grid(row=1, column = 2)
	label1 = Label(ventana, bg='black')
	label1.grid(row=2, column=2)
	texto = """
GOOGLE. Búsquedas avanzadas:
- https://sites.google.com/site/recursosdweb20idiomas/google

Bing. Búsquedas avanzadas: 

- http://onlinehelp.microsoft.com/en-us/bing/ff808421.aspx

DuckDuckGo. Búsquedas avanzadas: 
- https://duck.co/help/results/syntax
	"""
	label2 = Label(ventana, text = texto,height=11, width= 50,bg='white')
	label2.grid(row=3,column =2)
	label3 = Label(ventana, bg='black')
	label3.grid(row=4, column=2)
	caja = Entry(ventana, width =50)
	caja.grid(row=5, column =2)
	label4=Label(ventana, bg='black')
	label4.grid(row=6,column = 2)
	boton = Button(ventana, text="Buscar", command = lambda: search(caja.get()))
	boton.grid(row=7, column=2)

	ventana.mainloop()
