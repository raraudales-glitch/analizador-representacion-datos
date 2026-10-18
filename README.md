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