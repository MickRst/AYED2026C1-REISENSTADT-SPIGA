"""
proyecto_1 / main.py
Simulación de la Sala de Emergencias con triaje usando MinHeap.
"""

from ayedfiuner.estructuras.heap import MinHeap, HeapVacioError
from modules.paciente import Paciente, NivelRiesgoInvalidoError


def registrar_paciente(heap: MinHeap, nombre: str, nivel_riesgo: int) -> Paciente:
    """
    Crea un paciente y lo inserta en la cola de prioridad.

    Precondición:  nivel_riesgo debe ser 1, 2 o 3.
    Postcondición: el paciente queda en el heap y se retorna la instancia creada.
    Raises:        NivelRiesgoInvalidoError si el nivel de riesgo no es válido.
    """
    paciente = Paciente(nombre=nombre, nivel_riesgo=nivel_riesgo)
    heap.insertar(paciente)
    print(f"  [INGRESO]  {paciente}")
    return paciente


def atender_siguiente(heap: MinHeap) -> Paciente:
    """
    Extrae y atiende al paciente de mayor prioridad.

    Precondición:  el heap no debe estar vacío.
    Postcondición: el paciente es removido del heap y retornado.
    Raises:        HeapVacioError si no hay pacientes en espera.
    """
    paciente = heap.extraer_minimo()
    print(f"  [ATENCIÓN] {paciente}")
    return paciente


def simular_sala_emergencias():
    """Ejecuta la simulación completa de la sala de emergencias."""
    print("=" * 60)
    print("       SIMULACIÓN — SALA DE EMERGENCIAS (TRIAJE)")
    print("=" * 60)

    cola = MinHeap()

    print("\n── INGRESOS ──")
    pacientes_data = [
        ("Ana García",     3),
        ("Luis Pérez",     1),
        ("Marta López",    2),
        ("Juan Rodríguez", 1),
        ("Sofía Martínez", 3),
        ("Carlos Ruiz",    2),
        ("Elena Torres",   1),
        ("Pedro Sánchez",  2),
    ]

    for nombre, riesgo in pacientes_data:
        try:
            registrar_paciente(cola, nombre, riesgo)
        except NivelRiesgoInvalidoError as e:
            print(f"  [ERROR] {e}")

    print(f"\n── ATENCIÓN (pacientes en espera: {cola.tamanio()}) ──")
    while not cola.esta_vacio():
        try:
            atender_siguiente(cola)
        except HeapVacioError as e:
            print(f"  [ERROR] {e}")
            break

    print("\n── No quedan pacientes en espera. ──")
    print("=" * 60)

    print("\n── PRUEBA DE EXCEPCIONES ──")
    try:
        atender_siguiente(cola)
    except HeapVacioError as e:
        print(f"  [HeapVacioError capturada] {e}")

    try:
        registrar_paciente(cola, "Paciente Inválido", 5)
    except NivelRiesgoInvalidoError as e:
        print(f"  [NivelRiesgoInvalidoError capturada] {e}")

    print("=" * 60)


if __name__ == "__main__":
    simular_sala_emergencias()
