# Meredith Aguirre Machine Learning NC = 0013
import io
import os
import sys
import pandas as pd

# Permitir importar dicc_0013.py desde la subcarpeta hermana
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "..", "datos-de-entrada-ml-0013"
        )
    )
)
import dicc_0013

print("Meredith Aguirre Machine Learning pandas, NC 0013")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Meredith Aguirre Machine Learning pandas, NC 0013"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")


def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")


# 1. Convertir diccionario a DataFrame usando datos_cursos
df = pd.DataFrame(dicc_0013.datos_cursos)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de la Columna Numérica 'Duracion_horas'
registrar(
    "3. Estadísticas Generales de la Columna 'Duracion_horas'",
    df["Duracion_horas"].describe(),
)

# 4. Ordenar Ascendente por Duración
df_asc_duracion = df.sort_values(by="Duracion_horas", ascending=True)
registrar("4. Ordenar Ascendente por Duracion_horas", df_asc_duracion)

# 5. Ordenar Descendente por Inscritos
df_desc_inscritos = df.sort_values(by="Inscritos", ascending=False)
registrar("5. Ordenar Descendente por Inscritos", df_desc_inscritos)

# 6. Guardar el archivo resultados-ml-0013.md dentro de resultados-0013
carpeta_resultados = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "resultados-0013")
)
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0013.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")

print("Meredith Aguirre Machine Learning pandas, NC 0013")