#!/usr/bin/env python3

#mi primer script en python3

print("Python is aweson.")

#esto es una funcion
def my_function():
	mynum1 = 10
	mynum2 = 30
	print(mynum1 + mynum2)

my_function()


#variables locales vs globales
def my_function1():
	"""ejemplo de function.
	vamos a declarar una variable dentro de esta funcion.
	"""
	global message
	message = "Hello World!"
	print(message)

my_function1()


