# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:13:16 2023

@author: Aleksandra Grzenia
"""

#Użyj przybliżeń różnic skończonych O(h^2) do obliczenia f'(2,36) i f"(2,36) 
#z następujących danych:


def first_derivative(x_values,f_values):
    h=x_values[1]-x_values[0]               # Obliczenie kroku h po przez różnicę między kolejnymi wartosciami x.
    index_x=x_values.index(2.36)            # Indeks wartości x = 2.36
  
    # Przybliżenie pierwszej pochodnej. Wykorzystałam przybliżenie różnic skończonych drugiego rzędu, 
    # korzystałam z trzech sąsiednich wartosci funkcji f(x) w x=2.36
    
    if index_x>0 and index_x <len(x_values)-1:
        return (f_values[index_x+1]-f_values[index_x-1])/(2*h)
    else:
        return None                         # Nie można obliczyć dla krawędzi
    
def second_derivative(x_values,f_values):
    h=x_values[1]-x_values[0]               # Obliczenie kroku h jak dla przykładu pierwszej pochodnej.
    index_x=x_values.index(2.36)            # Indeks wartości x = 2.36
    
   # Przybliżenie drugiej pochodnej, wzór różnic skończonych drugiego rzędu, x=2.36
    if index_x>0 and index_x<len(x_values)-1:
        return (f_values[index_x+1]-2*f_values[index_x]+f_values[index_x-1])/(h**2)
    else:
        return None                         # Nie można obliczyć dla krawędzi
    
    
# Dane
x_values=[2.36, 2.37, 2.38, 2.39]
f_values=[0.85866, 0.86289, 0.86710, 0.87129]

# Obliczenia dla pierwszej i drugiej pochodnej.
first_derivative_approximation=first_derivative(x_values,f_values)
second_derivative_approximation=second_derivative(x_values,f_values)

# Wyświetlenie wyników
print(f"Pierwsza pochodna w punkcie x = 2.36: {first_derivative_approximation}")
print(f"Druga pochodna w punkcie x = 2.36: {second_derivative_approximation}")


# None wyswietli się, gdy przy obliczaniu przybliżonej pochodnej metodą różnic skończonych,
# brakuje wystarczającej ilosci punktów danych wokół punktu, dla którego liczona jest pochodna. 
# Po przez krawedź mam na mysli skrajne punkty zbioru danych.