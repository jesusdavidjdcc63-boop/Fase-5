"""
Fundamentos de Programación (213022) - Fase 5 - Evaluación Final POA
Problema 1: Nivel de compromiso de sesiones de clientes

Formato de cada fila de la matriz:
    [ID del Cliente, Duración de la sesión (segundos), Número de clics]
"""

# ---------------------------------------------------------------
# Constantes (umbrales de la lógica de negocio)
# ---------------------------------------------------------------
DURACION_ALTA = 180   # segundos
CLICS_ALTOS = 8
DURACION_BAJA = 60    # segundos
CLICS_BAJOS = 3

# Posiciones de cada dato dentro de una fila de la matriz
COL_ID = 0
COL_DURACION = 1
COL_CLICS = 2


# ---------------------------------------------------------------
# Módulo (función) de clasificación
# ---------------------------------------------------------------
def clasificar_compromiso(duracion, clics):
    """Retorna 'Alto', 'Medio' o 'Bajo' según duración y número de clics."""
    if duracion > DURACION_ALTA and clics > CLICS_ALTOS:
        return "Alto"
    elif duracion < DURACION_BAJA or clics < CLICS_BAJOS:
        return "Bajo"
    else:
        return "Medio"


# ---------------------------------------------------------------
# Módulo para mostrar el informe
# ---------------------------------------------------------------
def mostrar_informe(sesiones):
    """Recorre la matriz y muestra ID del cliente y su clasificación."""
    print("=" * 40)
    print("   INFORME DE COMPROMISO DE SESIONES")
    print("=" * 40)
    print(f"{'ID Cliente':<12}{'Duración(s)':<14}{'Clics':<8}{'Compromiso'}")
    print("-" * 40)

    for fila in sesiones:
        id_cliente = fila[COL_ID]
        duracion = fila[COL_DURACION]
        clics = fila[COL_CLICS]

        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12}{duracion:<14}{clics:<8}{nivel}")

    print("=" * 40)


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
def main():
    # Matriz con 7 sesiones (cubre los tres niveles y casos límite)
    sesiones = [
        [101, 240, 12],   # Alto
        [102, 45, 10],    # Bajo (duración < 60)
        [103, 150, 5],    # Medio
        [104, 200, 2],    # Bajo (clics < 3)
        [105, 180, 9],    # Medio (180 no es > 180)
        [106, 300, 8],    # Medio (8 no es > 8)
        [107, 90, 4],     # Medio
    ]

    mostrar_informe(sesiones)


main()