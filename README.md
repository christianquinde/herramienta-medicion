# herramienta-medicion
Esta herramienta permite obtener el valor de delay end-to-end, el throughput y el porcentaje de packet loss tanto para audio como video.

Esta herramienta se diseñó mediante scripts de Linux para cumplir con las distintas funcionalidades y los experimentos se efectuaron en ordenadores con sistema operativo Ubuntu 20.04. Para efectuar los diferentes cálculos también se implementaron scripts en Python 3.7.

Esta herramienta se ejecuta en paralelo con la herramienta App-videoconferencia disponible en: https://github.com/christianquinde/GUI-rx

En la siguiente Figura se muestra el diagrama secuencial de la herramienta.

![c9686710-536c-4a4d-a31c-3682daf4b5fe](https://user-images.githubusercontent.com/100379892/155769283-bfb509f5-bc87-403d-abdb-cfa82bb9280d.png)


En las siguiente Figura se muestran la interfaz de la herramienta.

![final](https://user-images.githubusercontent.com/100379892/155769483-290f91a4-cb32-4e37-8d12-227da4e001f8.jpg)


# Funcionamiento
## 1: Capturar
Se da clic en el botón "Capturar" después de ingresar las IPs de origen y destino. Así como seleccionar si nosotros fuimos quienes realizamos la llamada (TX) o recibimos la llamada (RX). Permitiendo realizar una captura de trafico sobre la interfaz que envía y recibe los flujos multimedia.

## 2: STOP
Después de 2 minutos de llamada se cerrará la captura. 
Al finalizar la captura se da clic en el botón STOP para filtrar los puertos y con la herramienta tshark y de esta manera separar los flujos de audio y video, así como los flujos que se envían o reciben.
Cabe mencionar que si se desea realizar una captura más corta al dar clic en el botón STOP también detendrá la captura. Se recomienda usar el mismo tiempo de captura para un análisis estadístico.

## 3: Calcular métricas

Para obtener los resultados de las métricas se da clic en el botón Calcular Métricas. Permitiendo mostrar el perfil de audio y video y los valores promedios de las métricas como el throughput, delay y packet loss.

## 4: Promediar
Finalmente, se da clic al botón promediar para obtener un análisis estadístico de las 10 capturas realizadas.

## Funciones Adicionales
Se puede verificar los resultados de cualquier transmisión en algún piso en específico, dando al botón Cargar y después al botón Calcular métricas.

