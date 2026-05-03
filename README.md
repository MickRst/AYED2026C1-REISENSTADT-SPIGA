# AYED2026C1 — Reisenstadt & Spiga

Repositorio del Trabajo Práctico N°1 de la materia **Algoritmos y Estructuras de Datos** — FIUNER.

## Integrantes
- Mickol Reisenstadt
- Edgardo Spiga

## Estructura del repositorio

```
AYED2026C1-REISENSTADT-SPIGA/
├── biblioteca_ayed_fiuner/          # Biblioteca reutilizable
│   ├── ayedfiuner/
│   │   ├── estructuras/LDE.py       # Lista Doblemente Enlazada
│   │   └── algoritmos/ordenamiento.py  # Burbuja, Quicksort, Radix Sort
│   ├── tests/
│   │   └── estructuras/test_LDE.py  # Tests de la LDE
│   └── setup.py
│
├── TrabajoPractico_1/
│   ├── proyecto_1/                  # Gráfica de tiempos LDE
│   ├── proyecto_2/                  # Juego de cartas Guerra
│   └── proyecto_3/                  # Gráfica de tiempos ordenamiento
│
└── informe_TP1.pdf                  # Informe del TP
```

## Cómo ejecutar

### 1. Instalar la biblioteca
Desde la raíz del repositorio:
```bash
pip install -e biblioteca_ayed_fiuner
```

### 2. Correr los tests
```bash
python -m unittest biblioteca_ayed_fiuner.tests.estructuras.test_LDE -v
cd TrabajoPractico_1/proyecto_2 && python -m unittest tests.test_mazo tests.test_juego_guerra -v
```

### 3. Generar las gráficas
```bash
cd TrabajoPractico_1/proyecto_1 && python main.py
cd TrabajoPractico_1/proyecto_3 && python main.py
```

### 4. Correr el juego Guerra
```bash
cd TrabajoPractico_1/proyecto_2 && python main.py
```
