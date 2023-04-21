---
marp: true
paginate: true
author: Pablo Moreira
theme: uncover
footer: ""
header: Laboratorio 3
---
# **Unidad 02**
## Módulos
___
## ¿Qué son los módulos en Python?

En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas de Python. Los módulos se utilizan para organizar el código y para evitar conflictos de nombres entre diferentes partes del programa.

---
# Contenido de un módulo 

Un módulo puede contener funciones, variables, clases, o incluso otros módulos. Para utilizar un módulo en Python, primero debes importarlo en tu programa.
<!--- 
theme: default
--->
``` python
import requests
```
También se pueden importar elementos específicos
``` python
from requests import get as _get
```
---
``` python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    else:
        return a / b
```