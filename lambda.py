# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:35:32 2022

@author: alegu
"""

#primero se define alpha y beta
alpha_lambda = lambda x: x + 1
beta_lambda = lambda x: 2 * x

#funciones de numeros utilizando lambda
cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))

#funciones de operaciones utilizando lambda
sucessor = lambda n: lambda f: lambda x: f(n(f) (x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f) (x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f)) (x)
potencia = lambda a: lambda b: lambda f: lambda x: a(b) (f) (x)

# ejemplos de uso de funciones
"""
beta
@description
@params 
"""

print('\033[1m' + 'Beta: ' + '\033[0m', beta_lambda(1))
print(' ')

"""
alpha
@description
@params 
"""
print('\033[1m' + 'Alfa: ' + '\033[0m', alpha_lambda(1))
print(' ')

"""
cero
@description
@params 
"""
print('\033[1m' + 'Cero & Alfa: ' + '\033[0m', cero(alpha_lambda)(2))
print('\033[1m' + 'Cero & Beta: ' + '\033[0m', cero(beta_lambda)(2))
print(' ')

"""
uno
@description
@params 
"""
print('\033[1m' + 'Uno & Alfa: ' + '\033[0m', uno(alpha_lambda)(3))
print('\033[1m' + 'Uno & Beta: ' + '\033[0m', uno(beta_lambda)(3))
print(' ')

"""
dos
@description
@params 
"""
print('\033[1m' + 'Dos & Alfa: ' + '\033[0m', dos(alpha_lambda)(2))
print('\033[1m' + 'Dos & Beta: ' + '\033[0m', dos(beta_lambda)(2))
print(' ')

"""
tres
@description
@params 
"""
print('\033[1m' + 'Tres & Alfa: ', tres(alpha_lambda)(2))
print('\033[1m' + 'Tres & Beta: ', tres(beta_lambda)(2))
print(' ')

"""
sucessor
@description
@params 
"""
print('\033[1m' + 'Sucessor & Alfa: ' + '\033[0m', sucessor(uno)(alpha_lambda)(1))
print('\033[1m' + 'Sucessor & Beta: ' + '\033[0m', sucessor(uno)(beta_lambda)(1))
print(' ')

"""
suma
@description
@params 
"""
print('\033[1m' + 'Suma & Alfa: ' + '\033[0m', suma(dos)(dos)(alpha_lambda)(1))
print('\033[1m' + 'Suma & Beta: ' + '\033[0m', suma(dos)(dos)(beta_lambda)(1))
print(' ')

"""
multiplicacion
@description
@params 
"""
print('\033[1m' + 'Multiplicacion & Alfa: ' + '\033[0m', multiplicacion(uno)(dos)(alpha_lambda)(2))
print('\033[1m' + 'Multiplicacion & Beta: ' + '\033[0m', multiplicacion(uno)(dos)(beta_lambda)(2))
print(' ')


"""
potencia
@description
@params 
"""
print('\033[1m' + 'Potencia & Alfa: ' + '\033[0m', potencia(dos)(tres)(alpha_lambda)(2))
print('\033[1m' + 'Potencia & Beta: ' + '\033[0m', potencia(dos)(tres)(beta_lambda)(2))
print(' ')
