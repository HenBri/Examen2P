# Ejemplo de cómo llamarlo desde otro archivo .py
from ia import consultar_ia

# Supongamos que capturas la respuesta de un alumno en una variable:
respuesta_alumno = "La fotosíntesis es el proceso mediante el cual las plantas producen oxígeno usando luz solar."
pregunta_examen = "Explica qué es la fotosíntesis."

# Creamos una instrucción clara para la IA
instruccion = f"""
Actúa como un profesor calificador. 
Pregunta del examen: {pregunta_examen}
Respuesta del alumno: {respuesta_alumno}

Por favor, califica la respuesta del 1 al 10 y dale una breve retroalimentación al alumno.
"""

# Se lo mandamos a tu función
resultado_final = consultar_ia(instruccion)
print(resultado_final)