# chatVozAI
Pequeño chat de voz basado en modelos de lenguaje natural y conectado con un modelo LLM local o moto bajo el API de OpenAI. Es una prueba de concepto para acercarse a los asistentes de voz. 

Se trata de un ejemplo simple en python que permite chatear con un modelo LLM remoto o local. En este ejemplo, he utilizado LMStudio con el modelo Dolphin 2 1 Mistral 7B y piper como modelo TTS, 
que genera resultados muy naturales y permite entrenar modelos, lo que abremas posibilidades para aprende.

Como mi conociiento en python es basico he tenido que hacer uso de un model LLM para que me ayudara a escribirlo. ¿Que mejor forma de aprender IA, que conuna IA?.

# Intrucciones:

### Paso 1: Instalar dependencias
Asegúrate de tener instaladas las siguientes dependencias:

**openai**  Este modulo facilita la ejecución de APIs en formato OpenAI contra el modelo LLM. Es un estandar.
'''pip install openai'''

**speech_recognition** (puedes instalarlo mediante pip install SpeechRecognition). Este punto es para realizar las preguntas por voz, mediante sistema como Whisper. Lo veremos mas adelate cuando solucione mi problema de microfono con alsa.

**Piper** Además, necesitarás instalar piper y descargar un modelo, Aqui su repositorio con sintrucciones. [PIPER] (https://github.com/rhasspy/piper) Te recomiendo que veas otros repositorios de rhasspy.


## Paso 2: El servidor local de LMStudio. 
Basicamente es descargar la aplicacion para tu sistema operativao. ejecutarlo, cargar un modelo y en la pestaña de configuracion activar el server para que funcione mediante API.

Su web (https://lmstudio.ai/)

## Paso 3: variables en El código
El codigo está configurado para apuntar a un servidor local de OpenAI. Asegúrate de tener el servidor en funcionamiento en mi caso por defecto #http://localhost:1234/v1. Si estás utilizando el API de OpenAI, deberás modificar la línea donde se define client para que apunte al servidor correcto.

**Configurar el modelo de piper**
Asegúrate de que la variable modelo_piper apunte al modelo adecuado en tu sistema. Deberías tener el modelo de síntesis de voz ONNX es_ES-davefx-medium.onnx en la ubicación correcta, en mi caso, se encuentra en un directorio de model dentro de una carpeta piper.

## Paso 4: Ejecutar el código
Una vez que hayas configurado todas las dependencias y variables correctamente, ejecuta el código. Este código establece un bucle infinito donde espera la entrada del usuario, envía esa entrada al servidor local de OpenAI para obtener una respuesta, y luego envía esa respuesta a la salida de audio utilizando piper.

'''pytho3 chatLLM'''

¡Espeo que te sea de ayuda!
