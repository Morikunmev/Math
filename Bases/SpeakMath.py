#Importaciones
import speech_recognition as sr #Biblioteca que proporciona la funcionaldiad de reconocmiento de voz, permitiendo convertir audio en texto
import keyboard #permite simular pulsaciones de teclas y enviar combinaciones de teclas al sistema
import pyautogui #Biblioteca para automatizar el control del amause y teclado
import time #funciones relacionadas con el tiempo, como pausas y esperas
import threading #permite ejecutar codigo en hilos paralelos, necesario para que el reconocimiento de voz funciones en segundo plano

# Variables globales para mantener un historial de lo dictado, se utiliza para la funcion "borra", que permite eliminar la ultima frase que se dicto
last_phrases = []

# Diccionario de símbolos matemáticos
math_symbols = {
    # Conjuntos numéricos
    "naturales": "ℕ",
    "enteros": "ℤ",
    "racionales": "ℚ",
    "irracionales": "ℝ\\ℚ",
    "reales": "ℝ",
    "complejos": "ℂ",
    
    # Operaciones entre conjuntos
    "unión": "∪",
    "intersección": "∩",
    "diferencia": "\\",
    "diferencia simétrica": "△",
    "complemento": "^c",
    "elevado":"^",
    "complen": "^",
    "comp": "^",
    "elev": "^",
    "producto cartesiano": "×",
    
    # Relaciones
    "pertenece": "∈",
    "no pertenece": "∉",
    "contiene": "∋",
    "no contiene": "∌",
    "subconjunto": "⊂",
    "subconjunto propio": "⊊",
    "no es subconjunto": "⊄",
    "superconjunto": "⊃",
    "su conjunto": "⊃",
    "superconjunto propio": "⊋",
    "no es superconjunto": "⊅",
    "subconjunto o igual": "⊆",
    "superconjunto o igual": "⊇",
    
    # Conjuntos especiales
    "conjunto vacío": "∅",
    "vacío": "∅",
    "conjunto potencia": "℘",
    "conjunto universal": "𝕌",
    
    # Cuantificadores y lógica
    "para todo": "∀",
    "existe": "∃",
    "no existe": "∄",
    "tal que": "∣",
    "tal": "∣",
    "implica": "⇒",
    "si y solo si": "⇔",
    "si y sólo si": "⇔",  # Con acento en "sólo"
    "si y solo sí": "⇔",  # Con acento en "sí"
    "si y sólo sí": "⇔",  # Con ambos acentos
    "sí y solo así": "⇔",
    "sí y solo sí" :"⇔",
    "sí y solo": "⇔",
    'sí solo sí': "⇔",
    "sii": "⇔",           # Abreviatura común
    
    "negación": "¬",
    "y lógico": "∧",
    "o lógico": "∨",
    
    # Otros símbolos útiles
    "infinito": "∞",
    "por lo tanto": "∴",
    "porque": "∵",
    "pi": "π",
    "raíz": "√",
    
    "no igual": "≠",
    "distinto": "≠",
    "distinto de": "≠",
    
    "igual": "=",
    "igual a": "=",
    "tal que": "∣",
    "donde": "∣",
    "dos puntos formal": ":",
    
    "implica": "⇒",
    "implicación": "⟹",
    "entonces": "⟹",
    "si entonces": "⟹",
    
    "flecha": "→",
    "flecha derecha": "→",
    "flecha a la derecha": "→",
    "hacia la derecha": "→",
    
    "flecha izquierda": "←",
    "flecha arriba": "↑",
    "flecha abajo": "↓",
    "flecha doble": "↔",
    
    "al cuadrado": "²",
    "cuadrado": "²"
}

#Funcion de Reconocimiento de Voz
def voice_recognition():
    global last_phrases
    r = sr.Recognizer() #crea un objeto Recognizer para procesar el audio
    
    print("Iniciando reconocimiento de voz...")
    
    #mantiene el programa continuamente escuchando
    while True:
        with sr.Microphone() as source: #abre el microfono predeterminado del sistema como fuente de audio. El bloque with asegura que el microfono se cierre correctamente despues de su uso.
            print("Escuchando...")
            r.adjust_for_ambient_noise(source) #Ajusta automaticamente el nivel de energia del reconocedor para compensar el ruido ambiental
            audio = r.listen(source) #Escucha a traves del microfono que detecta hasta que detecta una pausa en el habla y guarda el audio capturado. 
            
            try:
                text = r.recognize_google(audio, language="es-ES")
                #Envia el audio al servicio de reconocmiento de voz de Google y recibe el texto reconocido. Especifica el idiom
                print(f"Has dicho: '{text}'")
                print(f"Texto en minúsculas: '{text.lower()}'")  # Muestra exactamente lo que se está procesando

                
                # Pequeño retraso para asegurar que se procese toda la frase
                time.sleep(0.2)
                texto_lower = text.lower()
                
                # Verificar comandos específicos primero
                if "viñeta" in texto_lower:
                    print("Activando viñetas...")
                    keyboard.press_and_release('alt+h')
                    time.sleep(0.1)
                    keyboard.press_and_release('u')
                
                elif "abre paréntesis" in texto_lower:
                    keyboard.write("(")
                
                elif "cierra paréntesis" in texto_lower:
                    keyboard.write(")")
                
                elif "abre llave" in texto_lower:
                    keyboard.write("{")
                
                elif "cierra llave" in texto_lower:
                    keyboard.write("}")
                
                elif texto_lower == "punto":
                    keyboard.write(".")
                
                elif texto_lower == "dos puntos":
                    # Escribir dos puntos
                    keyboard.write(":")
                    # Esperar un tiempo más largo antes de desactivar la negrita
                    time.sleep(0.5)  # Aumentado a 0.5 segundos
                    # Desactivar negrita con una secuencia más explícita
                    keyboard.press('ctrl')
                    time.sleep(0.2)
                    keyboard.press('n')
                    time.sleep(0.2)
                    keyboard.release('n')
                    time.sleep(0.2)
                    keyboard.release('ctrl')
                
                elif "desactivar negrita" in texto_lower or "quitar negrita" in texto_lower:
                    print("Desactivando negrita...")
                    keyboard.press('ctrl')
                    time.sleep(0.2)
                    keyboard.press('n')
                    time.sleep(0.2)
                    keyboard.release('n')
                    time.sleep(0.2)
                    keyboard.release('ctrl')
                
                elif "borra" in texto_lower:
                    if last_phrases:
                        last_phrase = last_phrases.pop()
                        print(f"Borrando: '{last_phrase}'")
                        for _ in range(len(last_phrase) + 1):
                            keyboard.press_and_release('backspace')
                    else:
                        print("No hay frases para borrar")
                
                else:
                    # Buscar coincidencias ordenando las palabras clave por longitud (de más larga a más corta)
                    matched = False
                    # Convertir el diccionario a una lista y ordenar por longitud de la palabra clave
                    sorted_symbols = sorted(math_symbols.items(), key=lambda x: len(x[0]), reverse=True)
                    
                    for keyword, symbol in sorted_symbols:
                        if keyword in texto_lower:
                            print(f"¡Palabra clave '{keyword}' detectada! Insertando símbolo: {symbol}")
                            keyboard.write(symbol)
                            matched = True
                            break
                    
                    # Si no hay coincidencia, escribir el texto normal
                    if not matched:
                        last_phrases.append(text)
                        keyboard.write(text + " ")
                        
                        # Verificar si el texto termina con dos puntos
                        if text.strip().endswith(":"):
                            print("Detectados dos puntos: desactivando negrita...")
                            time.sleep(0.5)  # Aumentado a 0.5 segundos
                            keyboard.press('ctrl')
                            time.sleep(0.2)
                            keyboard.press('n')
                            time.sleep(0.2)
                            keyboard.release('n')
                            time.sleep(0.2)
                            keyboard.release('ctrl')
                
            except sr.UnknownValueError:
                print("No se pudo entender el audio")
            except sr.RequestError as e:
                print(f"Error en la solicitud a Google Speech Recognition; {e}")

# Iniciar reconocimiento de voz en un hilo separado
thread = threading.Thread(target=voice_recognition)
thread.daemon = True
thread.start()

# Mantener el programa en ejecución hasta que se presione Esc
print("Reconocimiento de voz activado con los siguientes comandos:")
print("- Di 'viñeta' para insertar una viñeta")
print("- Di 'abre paréntesis' para insertar (")
print("- Di 'cierra paréntesis' para insertar )")
print("- Di 'abre llave' para insertar {")
print("- Di 'cierra llave' para insertar }")
print("- Di 'punto' para insertar .")
print("- Di 'dos puntos' para insertar : y desactivar negrita")
print("- Di 'desactivar negrita' o 'quitar negrita' para desactivar formato de negrita")
print("- Di 'borra' para borrar la última frase")
print("- Para insertar símbolos matemáticos, solo menciona nombres como:")
print("  - 'naturales' para ℕ")
print("  - 'enteros' para ℤ")
print("  - 'racionales' para ℚ")
print("  - 'reales' para ℝ")
print("  - 'complejos' para ℂ")
print("  - 'pertenece' para ∈")
print("  - 'no pertenece' para ∉")
print("  - 'para todo' para ∀")
print("  - 'existe' para ∃")
print("  - 'subconjunto' para ⊂")
print("  - 'subconjunto o igual' para ⊆")
print("  - 'conjunto vacío' para ∅")
print("  - ... y muchos otros símbolos matemáticos")
print("Presiona Esc para salir.")
keyboard.wait('esc')