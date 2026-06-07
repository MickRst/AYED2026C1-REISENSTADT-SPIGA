"""
proyecto_2 / main.py
Base de datos de temperaturas usando árbol AVL — Kevin Kelvin.
"""

import os
from modules.temperaturas_db import TemperaturaDB, FechaNoEncontradaError, RangoInvalidoError
from ayedfiuner.estructuras.avl import ArbolVacioError

ARCHIVO_MUESTRAS = os.path.join(os.path.dirname(__file__), "data", "muestras.txt")


def main():
    print("=" * 60)
    print("        TEMPERATURAS_DB — Kevin Kelvin")
    print("=" * 60)

    db = TemperaturaDB()

    # ── Carga desde archivo ──────────────────────────────────────────
    print("\n── Cargando muestras desde archivo ──")
    if os.path.exists(ARCHIVO_MUESTRAS):
        db.cargar_desde_archivo(ARCHIVO_MUESTRAS)
    else:
        print("  [AVISO] No se encontró muestras.txt. Cargando datos de ejemplo.")
        datos = [
            (20.5, "01/01/2023"), (18.3, "15/01/2023"),
            (22.1, "01/02/2023"), (25.7, "15/02/2023"),
            (30.2, "01/03/2023"), (28.9, "15/03/2023"),
            (15.4, "01/04/2023"), (19.8, "15/04/2023"),
        ]
        for temp, fecha in datos:
            db.guardar_temperatura(temp, fecha)
        print(f"  Cargadas {db.cantidad_muestras()} muestras de ejemplo.")

    print(f"\n  Total de muestras en la BD: {db.cantidad_muestras()}")

    # ── Consultas ────────────────────────────────────────────────────
    print("\n── Consultas ──")

    try:
        temp = db.devolver_temperatura("01/01/2023")
        print(f"  Temperatura el 01/01/2023: {temp} ºC")
    except FechaNoEncontradaError as e:
        print(f"  [INFO] {e}")

    try:
        max_t = db.max_temp_rango("01/01/2023", "31/03/2023")
        print(f"  Máxima entre 01/01/2023 y 31/03/2023: {max_t} ºC")
    except (RangoInvalidoError, ArbolVacioError) as e:
        print(f"  [INFO] {e}")

    try:
        min_t = db.min_temp_rango("01/01/2023", "31/03/2023")
        print(f"  Mínima entre 01/01/2023 y 31/03/2023: {min_t} ºC")
    except (RangoInvalidoError, ArbolVacioError) as e:
        print(f"  [INFO] {e}")

    try:
        lista = db.devolver_temperaturas("01/01/2023", "31/03/2023")
        print(f"\n  Mediciones entre 01/01/2023 y 31/03/2023:")
        for entrada in lista:
            print(f"    {entrada}")
    except (RangoInvalidoError, ArbolVacioError) as e:
        print(f"  [INFO] {e}")

    # ── Borrar una medición ──────────────────────────────────────────
    print("\n── Borrar medición ──")
    try:
        db.borrar_temperatura("01/01/2023")
        print(f"  Medición del 01/01/2023 eliminada.")
        print(f"  Total de muestras: {db.cantidad_muestras()}")
    except FechaNoEncontradaError as e:
        print(f"  [INFO] {e}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
