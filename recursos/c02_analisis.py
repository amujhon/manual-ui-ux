"""Ejercicio de análisis descriptivo de eventos sintéticos (capítulo 02).

Uso: python c02_analisis.py [ruta.csv]
No accede a red, no envía datos ni utiliza librerías externas.
No pretende representar población, inferir causas ni producir un estudio estadístico.
"""
import csv
import sys
from collections import Counter
from pathlib import Path
from statistics import median

RESULTADOS = {"completada", "fallida", "abandonada"}


def resumir(ruta: Path) -> None:
    with ruta.open(newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        columnas = {"tarea", "dispositivo", "resultado", "duracion_ms"}
        if not columnas.issubset(lector.fieldnames or []):
            raise ValueError(f"El CSV necesita las columnas: {sorted(columnas)}")
        registros = list(lector)

    if not registros:
        print("El conjunto está vacío: no hay resultados.")
        return

    grupos = Counter()
    completadas = []
    for i, fila in enumerate(registros, start=2):
        if fila["resultado"] not in RESULTADOS:
            raise ValueError(f"Resultado desconocido en línea {i}")
        try:
            duracion = int(fila["duracion_ms"])
        except ValueError as exc:
            raise ValueError(f"Duración inválida en línea {i}") from exc
        if duracion < 0:
            raise ValueError(f"Duración negativa en línea {i}")
        grupos[(fila["dispositivo"], fila["resultado"])] += 1
        if fila["resultado"] == "completada":
            completadas.append(duracion)

    total = len(registros)
    finalizadas = sum(n for (_, resultado), n in grupos.items() if resultado == "completada")
    print("Ejercicio con DATOS SINTÉTICOS (no representa una población real)")
    print(f"Eventos registrados: {total}")
    print(f"Completadas en este conjunto: {finalizadas}/{total} ({100 * finalizadas / total:.1f} %)" )
    if completadas:
        print(f"Mediana de duración de eventos completados: {median(completadas) / 1000:.1f} s")
    print("Eventos por dispositivo y resultado:")
    for (dispositivo, resultado), n in sorted(grupos.items()):
        print(f" - {dispositivo:7} | {resultado:10}: {n}")
    print("ATENCIÓN: no inferir causas, significación estadística, representatividad ni efecto de una mejora.")
    print("El porcentaje se refiere a EVENTOS, no necesariamente a usuarios únicos.")


if __name__ == "__main__":
    predeterminada = Path(__file__).with_name("c02_registros_demo.csv")
    try:
        resumir(Path(sys.argv[1]) if len(sys.argv) > 1 else predeterminada)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
