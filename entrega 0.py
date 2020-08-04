# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:52:33 2020

@author: jpsil
"""

# nombre="Jose"
# dia=3
# print("hola Jose es el 3 de agosto")
# print("hola "+nombre+" es el",dia,"de agosto")
# # 1)
# print("hola {} es el {} de agosto".format(nombre,dia))
# # 2)
# print("hola {} es el {} de agosto".format(nombre,dia))
# print(f"hola {nombre} es el {dia} de agosto")

# """
# Ejemplo 2
# """
# print("hola hola hola hola hola hola hola hola")
# print("hola"*7)

"""
matriz
"""
import numpy as np
n=3
a=np.random.rand(n,n)
b=np.random.rand(n,n)
print(a)
print(f"a = \n {a}")
print(f"b = \n {b}")
c=a*b
print(f"c = \n {c}")