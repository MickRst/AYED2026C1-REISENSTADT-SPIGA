"""
proyecto_3 / main.py
Palomas Mensajeras de William — MST con algoritmo de Prim.
"""

import os
from modules.grafo import Grafo, VerticeNoExisteError
from modules.prim import prim, construir_arbol_msm, distancia_total_mst, GrafoDesconectadoError

ORIGEN = "Peligros"
ARCHIVO = os.path.join(os.path.dirname(__file__), "data", "aldeas.txt")


def mostrar_aldeas_alfabetico(grafo: Grafo) -> None:
    print("\n" + "=" * 60)
    print("  LISTA DE ALDEAS (orden alfabético)")
    print("=" * 60)
    for i, aldea in enumerate(sorted(grafo.vertices()), 1):
        print(f"  {i:2}. {aldea}")


def mostrar_plan_comunicacion(padre: dict, arbol: dict, origen: str) -> None:
    print("\n" + "=" * 60)
    print("  PLAN DE COMUNICACIÓN ÓPTIMO (MST desde Peligros)")
    print("=" * 60)
    for aldea in sorted(padre.keys()):
        info_padre = padre[aldea]
        hijos = arbol.get(aldea, [])
        if aldea == origen:
            recibe_de = "— (es el origen)"
        else:
            progenitor, dist = info_padre
            recibe_de = f"{progenitor}  (dist: {dist} leguas)"
        if hijos:
            replicas = ", ".join(f"{h} ({d} leguas)" for h, d in sorted(hijos))
        else:
            replicas = "— (no replica, es hoja)"
        print(f"\n  {aldea}")
        print(f"    Recibe de  : {recibe_de}")
        print(f"    Replica a  : {replicas}")


def mostrar_distancia_total(padre: dict) -> None:
    total = distancia_total_mst(padre)
    print("\n" + "=" * 60)
    print("  DISTANCIA TOTAL RECORRIDA POR TODAS LAS PALOMAS")
    print("=" * 60)
    print(f"  Suma de todas las rutas del MST: {total} leguas")
    print("=" * 60)


def main():
    print("=" * 60)
    print("      AGENCIA DE NOTICIAS — PALOMAS WILLIAM")
    print("=" * 60)

    grafo = Grafo()
    try:
        grafo.cargar_desde_archivo(ARCHIVO)
        print(f"\n  Grafo cargado: {grafo}")
    except FileNotFoundError:
        print(f"  [ERROR] No se encontró el archivo: {ARCHIVO}")
        return

    if not grafo.contiene_vertice(ORIGEN):
        print(f"  [ERROR] La aldea origen '{ORIGEN}' no está en el grafo.")
        return

    try:
        padre = prim(grafo, ORIGEN)
    except (GrafoDesconectadoError, VerticeNoExisteError) as e:
        print(f"  [ERROR] {e}")
        return

    arbol = construir_arbol_msm(padre)
    mostrar_aldeas_alfabetico(grafo)
    mostrar_plan_comunicacion(padre, arbol, ORIGEN)
    mostrar_distancia_total(padre)


if __name__ == "__main__":
    main()
