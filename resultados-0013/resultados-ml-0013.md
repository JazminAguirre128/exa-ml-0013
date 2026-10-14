# Reporte de Análisis de Datos - Pandas

`Meredith Aguirre Machine Learning pandas, NC 0013`

## 1. DataFrame Convertido
```text
        Curso  Duracion_horas  Inscritos
0      Python              40       1200
1  JavaScript              35        980
2        Java              50        750
3         C++              60        540
4        Ruby              30        320
5         PHP              45        680
```

## 2.1 Primeras Filas (head)
```text
        Curso  Duracion_horas  Inscritos
0      Python              40       1200
1  JavaScript              35        980
```

## 2.2 Últimas Filas (tail)
```text
  Curso  Duracion_horas  Inscritos
4  Ruby              30        320
5   PHP              45        680
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Curso               str
Duracion_horas    int64
Inscritos         int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Curso           6 non-null      str  
 1   Duracion_horas  6 non-null      int64
 2   Inscritos       6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Duracion_horas'
```text
count     6.000000
mean     43.333333
std      10.801234
min      30.000000
25%      36.250000
50%      42.500000
75%      48.750000
max      60.000000
Name: Duracion_horas, dtype: float64
```

## 4. Ordenar Ascendente por Duracion_horas
```text
        Curso  Duracion_horas  Inscritos
4        Ruby              30        320
1  JavaScript              35        980
0      Python              40       1200
5         PHP              45        680
2        Java              50        750
3         C++              60        540
```

## 5. Ordenar Descendente por Inscritos
```text
        Curso  Duracion_horas  Inscritos
0      Python              40       1200
1  JavaScript              35        980
2        Java              50        750
5         PHP              45        680
3         C++              60        540
4        Ruby              30        320
```

`Meredith Aguirre Machine Learning pandas, NC 0013`