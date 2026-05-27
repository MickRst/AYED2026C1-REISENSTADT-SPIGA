"""
proyecto_2 / main.py
Ejecuta una partida del juego Guerra.
"""
import random
from modules.juego_guerra import JuegoGuerra

if __name__ == "__main__":
    n = random.randint(0, 1000)
    print(f"Semilla: {n}")
    juego = JuegoGuerra(random_seed=n)
    juego.iniciar_juego(ver_partida=False)
    print(f"Ganador: {juego.ganador}")
    print(f"Turnos jugados: {juego.turnos_jugados}")
