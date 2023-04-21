 El módulo datetime en Python

El módulo `datetime` es un módulo incorporado en Python que proporciona clases para trabajar con fechas, horas y duraciones. Este módulo permite manejar de manera eficiente y fácil la manipulación de fechas y horas en programas Python.

## Importar el módulo datetime

Para utilizar el módulo `datetime`, primero debes importarlo en tu script o programa Python. Puedes hacerlo utilizando la siguiente línea de código:

```python
import datetime
```
Clases principales del módulo datetime

# El módulo datetime proporciona varias clases principales para trabajar con fechas y horas:

* datetime: Representa una combinación de fecha y hora, con atributos como año, mes, día, hora, minuto, segundo y microsegundo.
* date: Representa una fecha (año, mes y día) sin información de hora.
* time: Representa una hora (hora, minuto, segundo y microsegundo) sin información de fecha.
* timedelta: Representa una duración de tiempo entre dos fechas o horas.
* tzinfo: Es una clase base abstracta para definir zonas horarias personalizadas.

# Funciones y métodos útiles del módulo datetime

El módulo datetime también proporciona varias funciones y métodos útiles para trabajar con fechas y horas, incluyendo:

* datetime.now(): Retorna un objeto datetime que representa la fecha y hora actuales.
* datetime.strptime(): Convierte una cadena de texto en un objeto datetime según un formato especificado.
* datetime.strftime(): Convierte un objeto datetime en una cadena de texto con un formato especificado.
* date.today(): Retorna un objeto date que representa la fecha actual sin información de hora.
* time(hour, minute, second, microsecond): Crea un objeto time con la hora, minuto, segundo y microsegundo especificados.
* timedelta(days, hours, minutes, seconds, microseconds): Crea un objeto timedelta que representa una duración de tiempo.
* Métodos como year, month, day, hour, minute, second, etc., para acceder a los componentes de una fecha o hora.