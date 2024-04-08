# Detector de Objetos con Cámara en Tiempo Real - Ultralytics YOLOv8

Este proyecto te permite detectar objetos en un video utilizando el modelo `yolov8s.pt` de YOLOv8, y visualizar los resultados en tiempo real. Personaliza tu experiencia con este modelo pre-entrenado y experimenta con la detección de objetos en diversas situaciones.

## Demostración

![Demostración del proyecto](https://ruta/hacia/imagen.gif)

## Requisitos

- Python 3.6 o superior
- Biblioteca OpenCV
- Biblioteca Ultralytics

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python y las bibliotecas requeridas instaladas en tu sistema.
3. Descarga los pesos pre-entrenados del modelo YOLOv8 y colócalos en la carpeta del proyecto.
4. Ejecuta el script `detect_objects.py` para iniciar la detección de objetos en el video.

## Cómo Usar

1. Ejecuta el script `detect_objects.py`.
2. Observa cómo se abre la ventana del video y las personas se detectan en tiempo real.
3. Experimenta cambiando el tipo de objetos que desees detectar, cambiando las variables `etiqueta` y `name_etiqueta`, de acuerdo con los objetos que desees detectar. Para ello, ten en cuenta la lista de elementos que pueden ser detectados con el modelo `yolov8s.pt`; esta lista la puedes encontrar en el archivo `labels.txt`.

## Estructura del Proyecto

- **`detect_objects.py`**: El script principal que contiene el código para la detección de objetos en video.
- **`yolov8s.pt`**: Los pesos pre-entrenados del modelo YOLOv8.

## Agradecimientos

Agradezco a la comunidad de Ultralytics por sus contribuciones al desarrollo de modelos de detección de objetos. ¡Disfruta explorando el mundo de la detección de objetos en tiempo real con YOLOv8!
