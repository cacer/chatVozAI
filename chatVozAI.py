import subprocess
from openai import OpenAI

import speech_recognition as sr

samplerate = "22000"

path_piper = "/media/carlos/HD2/IA/piper_amd64/piper/"
modelo_piper = "es_ES-davefx-medium.onnx"

# Caracteres de puntuación que indican el final de una oración
puntuacion_final = ".,"

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

history = [
    {"role": "system", "content": "Eres un asistente virtual con la mejor intelgencia artificial dispuesto a solucionar cualquier pregunta. Limita tus respuestas a un maximo de 200 palabras salvo que te diga lo contrario"},
    {"role": "user", "content": "Hola. Introduce tu consulta y se conciso"},
]

# comando para enviar respuesta de texto a la salida de audio
def enviar_respuesta(respuesta_texto, path_piper, modelo_piper, samplerate):
    salida = "--output-raw | aplay -r " + samplerate + " -f S16_LE -t raw -"
    command = f"echo '{respuesta_texto}' | {path_piper}piper --model {path_piper}model/{modelo_piper} {salida}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("Hubo un error:", stderr.decode())
    else:
        print("Respuesta enviada exitosamente.")
    print(respuesta_texto)  # Imprimir la respuesta en la salida estándar también

# Recibe la respuesta del modelo LLM y la envía a la salida de audio cada vez que se encuentra un punto o una coma
def recibir_respuesta_y_enviar_audio():
    completado = client.chat.completions.create(
        model="local-model", # este campo actualmente no se utiliza
        messages=history,
        temperature=0.7,
        stream=True,
    )

    nueva_respuesta = ""
    for chunk in completado:
        if chunk.choices[0].delta.content:
            nueva_respuesta += chunk.choices[0].delta.content

            # Verificar si el último carácter es un punto o una coma
            if nueva_respuesta[-1] in puntuacion_final:
                enviar_respuesta(nueva_respuesta, path_piper, modelo_piper, samplerate)
                nueva_respuesta = ""

# Bucle principal
while True:
    recibir_respuesta_y_enviar_audio()
    history.append({"role": "user", "content": input("> ")})
