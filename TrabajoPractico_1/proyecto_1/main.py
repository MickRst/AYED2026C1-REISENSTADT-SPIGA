"""
proyecto_1 / main.py
Gráfica de N vs tiempo de ejecución para len, copiar e invertir de ListaDobleEnlazada.
"""

import sys
import os
sys.path.insert(0, r'C:\Users\edgar\AYED2026C1-REISENSTADT-SPIGA')

import time
import random
import matplotlib.pyplot as plt
from biblioteca_ayed_fiuner.ayedfiuner.estructuras.LDE import ListaDobleEnlazada


def construir_lista(n):
    lista = ListaDobleEnlazada()
    for _ in range(n):
        lista.agregar_al_final(random.randint(0, 10000))
    return lista


def medir_tiempo(funcion, *args, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


tamanios = list(range(0, 5001, 100))
tiempos_len, tiempos_copiar, tiempos_invertir = [], [], []

print("Midiendo tiempos...")
for n in tamanios:
    lista = construir_lista(n)
    tiempos_len.append(medir_tiempo(len, lista) * 1e6)
    tiempos_copiar.append(medir_tiempo(lista.copiar) * 1e6)
    tiempos_invertir.append(medir_tiempo(lista.invertir) * 1e6)

print("Generando gráfica...")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("ListaDobleEnlazada: N vs Tiempo de ejecución", fontsize=14, fontweight="bold")

axes[0].plot(tamanios, tiempos_len, color="steelblue", linewidth=1.5)
axes[0].set_title("len(lista)")
axes[0].set_xlabel("N (cantidad de elementos)")
axes[0].set_ylabel("Tiempo (microsegundos)")
axes[0].annotate("O(1): tiempo constante", xy=(0.5, 0.75), xycoords="axes fraction",
                 ha="center", fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.5))

axes[1].plot(tamanios, tiempos_copiar, color="darkorange", linewidth=1.5)
axes[1].set_title("lista.copiar()")
axes[1].set_xlabel("N (cantidad de elementos)")
axes[1].set_ylabel("Tiempo (microsegundos)")
axes[1].annotate("O(n): tiempo lineal", xy=(0.35, 0.75), xycoords="axes fraction",
                 ha="center", fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor="moccasin", alpha=0.5))

axes[2].plot(tamanios, tiempos_invertir, color="seagreen", linewidth=1.5)
axes[2].set_title("lista.invertir()")
axes[2].set_xlabel("N (cantidad de elementos)")
axes[2].set_ylabel("Tiempo (microsegundos)")
axes[2].annotate("O(n): tiempo lineal", xy=(0.35, 0.75), xycoords="axes fraction",
                 ha="center", fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.5))

plt.tight_layout()
plt.savefig("grafica_tiempos_LDE.png", dpi=150, bbox_inches="tight")
plt.show()
print("Gráfica guardada como 'grafica_tiempos_LDE.png'")
