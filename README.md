# Analizador de Representación de Datos
**Desarrollado por:** Raúl Raudales
## Requisitos y Comandos de Docker
# Construir la imagen y ejecutar el contenedor

```bash
# Construir e iniciar el contenedor
docker compose up --build -d

# Ver estadísticas de recursos en tiempo real 
docker stats

# Detener aplicacion
docker compose down

#Von Neumann
CPU porque ejecuta la logica en las vista de Django mediante las views.py aparte de procesar las expresiones regulares de validacion y realizar los calculos de conversion.
RAM almacena la informacion temporalmente mediante las peticiones HTTP esto durante el proceso de la vista y rendeerizacion del html.
E/S 
Entrada es lo que enviamos osea el texto y numero
Salida es lo que nos devuelve el html

#¿Por qué el contenedor comparte el kernel del host?
Debido a lo que estamos usando que es docker esto lo que hace es ejecutar de manera aislada pero utilizando directamente el kernel de la computadora donde se ejecute por ejemplo nosotros por django estamos usando el kernel de linux pero mi computadora es windows, pero no es malo mas bien al hacer elimina la sobrecarga que tendriamos virtualizando algo aparte que el arranque es mayor.

#Ejecute el contenedor con un límite de 256 MB de RAM y 1 CPU, y adjunte evidencia de docker stats.
CONTAINER ID   NAME                                                           CPU %     MEM USAGE / LIMIT    MEM %     NET I/O           BLOCK I/O        PIDS
049b38f623ec   analizadorderepresentacindedatosusandopython312ydjango-web-1   0.34%     83.52MiB / 256MiB    32.62%    1.7kB / 126B      15.2MB / 0B      3
44c0797594ed   dockerprojectogrupal-db-1                                      0.01%     24.84MiB / 31.3GiB   0.08%     1.7kB / 126B      30.2MB / 365kB   6
20af481b6355   hbbr                                                           0.01%     1.621MiB / 31.3GiB   0.01%     1.95kB / 126B     2.76MB / 0B      23
e4d1b6be7f85   hbbs                                                           0.03%     3.535MiB / 31.3GiB   0.01%     9.54kB / 3.15kB   8.94MB / 0B      45

PS C:\Users\jonat\Videos\Analizador de representación de datos usando Python 3.12 y Django>









