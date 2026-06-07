# Trabajo Práctico N° 2 — Algoritmos y Estructuras de Datos

## Integrantes
- Reisenstadt Micol
- Spiga Edgardo

## Estructura

```
TrabajoPractico_2/
├── proyecto_1/   → Sala de Emergencias (MinHeap + triaje)
├── proyecto_2/   → Temperaturas_DB (Árbol AVL)
└── proyecto_3/   → Palomas Mensajeras (Grafo + Prim)
```

## Cómo ejecutar

### Instalar la biblioteca (desde la raíz del repo):
```bash
pip install -e biblioteca_ayed_fiuner
```

### Correr cada proyecto:
```bash
cd TrabajoPractico_2/proyecto_1 && python main.py
cd TrabajoPractico_2/proyecto_2 && python main.py
cd TrabajoPractico_2/proyecto_3 && python main.py
```

### Correr los tests:
```bash
cd TrabajoPractico_2/proyecto_1 && python -m unittest tests/test_sala_emergencias -v
cd TrabajoPractico_2/proyecto_3 && python -m unittest tests/test_palomas -v
```
