---
marp: true
size: 4:3
---

# Módulo time en Python

El módulo `time` en Python es una herramienta muy útil para trabajar con operaciones de tiempo en aplicaciones de Python.

---

## ¿Por qué es importante saber sobre time?

El conocimiento del módulo `time` es especialmente importante si se está trabajando en aplicaciones que requieren la gestión del tiempo.

---

## Funciones útiles del módulo time

- `time()`: devuelve el tiempo actual en segundos desde la época de Unix.
- `sleep()`: detiene la ejecución del programa durante un número determinado de segundos.
- `gmtime()`: convierte un número de segundos desde la época de Unix en una estructura de tiempo en formato UTC.
- `localtime()`: convierte un número de segundos desde la época de Unix en una estructura de tiempo en la zona horaria local.
- `strftime()`: convierte una estructura de tiempo en una cadena de caracteres con un formato específico.

---

## La época de Unix

La época de Unix es el momento en que se inició el contador de tiempo utilizado en los sistemas operativos Unix y en muchos otros sistemas informáticos. La época de Unix es el 1 de enero de 1970, 00:00:00 UTC.

---

## Ejemplo de uso del módulo time en Python

```python
import time

# Obtener el tiempo actual en segundos desde la época de Unix
tiempo_actual = time.time()
print(f"Tiempo actual en segundos desde la época de Unix: {tiempo_actual}")

# Esperar 2 segundos
print("Esperando 2 segundos...")
time.sleep(2)
print("¡Listo!")

# Convertir el tiempo actual en UTC
tiempo_utc = time.gmtime(tiempo_actual)
print(f"Tiempo actual en UTC: {time.strftime('%Y-%m-%d %H:%M:%S', tiempo_utc)}")

# Convertir el tiempo actual en la zona horaria local
tiempo_local = time.localtime(tiempo_actual)
print(f"Tiempo actual en la zona horaria local: {time.strftime('%Y-%m-%d %H:%M:%S', tiempo_local)}")
print(tiempo_local)
``` 
---

La función gmtime() toma un argumento opcional que representa el número de segundos desde la época de Unix. Si no se especifica un argumento, se utiliza el tiempo actual. La función devuelve una estructura de tiempo en formato UTC que contiene los siguientes campos:

    tm_year: El año (ejemplo: 2023)
    tm_mon: El mes (1-12)
    tm_mday: El día del mes (1-31)
    tm_hour: La hora (0-23)
    tm_min: Los minutos (0-59)
    tm_sec: Los segundos (0-59)
    tm_wday: El día de la semana (0-6, donde 0 es el lunes)
    tm_yday: El día del año (1-366)
    tm_isdst: Indicador del horario de verano (0, 1 o -1)

---
# Las Zonas Horarias

Las zonas horarias son áreas geográficas del mundo en las que se utiliza la misma hora. Las zonas horarias se utilizan para mantener una consistencia en la hora y la fecha en todo el mundo, y permiten que las personas se comuniquen y coordinen a nivel internacional.
# Funcionamiento de las zonas horarias

Cada zona horaria está separada por una cantidad determinada de horas de diferencia con respecto al Tiempo Universal Coordinado (UTC), que es la hora de referencia mundial. Por ejemplo, la zona horaria de Nueva York está a 5 horas detrás del UTC, mientras que la zona horaria de Moscú está a 3 horas adelante del UTC.

---
# `strftime()` 

La función strftime() es una función del módulo time en Python que se utiliza para formatear una estructura time como una cadena de fecha y hora.

` cadena_formateada = time.strftime("%Y-%m-%d %H:%M:%S", estructura_time) `

---

# `strptime()`

La función strptime() es una función del módulo time en Python que se utiliza para analizar una cadena de fecha y hora y crear una estructura time correspondiente.

Por ejemplo, si tienes una cadena de fecha y hora en el formato `YYYY-MM-DD HH:MM:SS`

---

# mktime():

la función mktime() del módulo time, que convierte una estructura time en el número de segundos 

```
import time
la función mktime() del módulo time, que convierte una estructura time en el número de segundos 

# Obtener la estructura time actual
estructura_time = time.localtime()

# Convertir a segundos
segundos = time.mktime(estructura_time)

print(segundos)

```
---
## Ejercicios prácticos con el módulo time

1. Fácil: Escribe un programa que muestre la fecha y hora actual en el siguiente formato: `dd/mm/aaaa hh:mm:ss`.

2. Intermedio: Escribe una función que tome como entrada dos fechas en formato `dd/mm/aaaa` y calcule la cantidad de días transcurridos entre ambas fechas.

3. Difícil: Escribe una función que tome como entrada una lista de fechas en formato `dd/mm/aaaa` y devuelva la fecha que ocurrió con mayor frecuencia. Si hay varias fechas que ocurren con la misma frecuencia máxima, devuelve la fecha más reciente.

---
## Ejercicios prácticos con el módulo time (nivel difícil)

1. Escribe una función que tome como entrada una fecha en formato `dd/mm/aaaa` y calcule el día de la semana correspondiente (por ejemplo, "lunes", "martes", etc.) utilizando el módulo `time`.

2. Escribe una función que tome como entrada una lista de fechas en formato `dd/mm/aaaa` y calcule la cantidad de días transcurridos entre la fecha más antigua y la fecha más reciente.

3. Escribe una función que tome como entrada una lista de fechas en formato `dd/mm/aaaa` y devuelva las dos fechas que están más cerca entre sí en términos de días transcurridos. La función debe devolver ambas fechas en formato `dd/mm
