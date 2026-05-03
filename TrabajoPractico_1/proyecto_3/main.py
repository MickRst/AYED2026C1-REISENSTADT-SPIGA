"""
proyecto_3 / main.py
Mide y grafica tiempos de burbuja, quicksort, radix sort y sorted().
"""

import sys
import os
sys.path.insert(0, r'C:\Users\edgar\AYED2026C1-REISENSTADT-SPIGA')

import time
import random
import matplotlib.pyplot as plt
from biblioteca_ayed_fiuner.ayedfiuner.algoritmos.ordenamiento import burbuja, quicksort, radix_sort


def generar_lista(n):
    return [random.randint(10000, 99999) for _ in range(n)]


def medir(funcion, lista):
    inicio = time.perf_counter()
    funcion(lista)
    return time.perf_counter() - inicio


print("Verificando correctitud con 500 elementos...")
lista_prueba = generar_lista(500)
assert burbuja(lista_prueba)    == sorted(lista_prueba), "Error en burbuja"
assert quicksort(lista_prueba)  == sorted(lista_prueba), "Error en quicksort"
assert radix_sort(lista_prueba) == sorted(lista_prueba), "Error en radix sort"
print("Los tres algoritmos ordenan correctamente.\n")

tamanios = list(range(1, 1001, 10))
t_burbuja, t_quicksort, t_radix, t_sorted = [], [], [], []

print("Midiendo tiempos...")
for n in tamanios:
    lista = generar_lista(n)
    t_burbuja.append(  medir(burbuja,    lista) * 1000)
    t_quicksort.append(medir(quicksort,  lista) * 1000)
    t_radix.append(    medir(radix_sort, lista) * 1000)
    t_sorted.append(   medir(sorted,     lista) * 1000)

print("Generando gráfica...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Comparación de algoritmos de ordenamiento (N=1 a 1000)", fontsize=13, fontweight="bold")

ax1 = axes[0]
ax1.plot(tamanios, t_burbuja,   label="Burbuja  O(n²)",        color="crimson",    linewidth=1.5)
ax1.plot(tamanios, t_quicksort, label="Quicksort  O(n log n)", color="steelblue",  linewidth=1.5)
ax1.plot(tamanios, t_radix,     label="Radix Sort  O(n·k)",    color="darkorange", linewidth=1.5)
ax1.plot(tamanios, t_sorted,    label="sorted() Python",       color="seagreen",   linewidth=1.5, linestyle="--")
ax1.set_title("Todos los algoritmos")
ax1.set_xlabel("N (cantidad de elementos)")
ax1.set_ylabel("Tiempo (milisegundos)")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2 = axes[1]
ax2.plot(tamanios, t_quicksort, label="Quicksort  O(n log n)", color="steelblue",  linewidth=1.5)
ax2.plot(tamanios, t_radix,     label="Radix Sort  O(n·k)",    color="darkorange", linewidth=1.5)
ax2.plot(tamanios, t_sorted,    label="sorted() Python",       color="seagreen",   linewidth=1.5, linestyle="--")
ax2.set_title("Sin burbuja (escala más clara)")
ax2.set_xlabel("N (cantidad de elementos)")
ax2.set_ylabel("Tiempo (milisegundos)")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("grafica_ordenamiento.png", dpi=150, bbox_inches="tight")
plt.show()
print("Gráfica guardada como 'grafica_ordenamiento.png'")
