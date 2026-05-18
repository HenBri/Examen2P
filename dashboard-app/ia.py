import os
from google import genai
from dotenv import load_dotenv

# Cargamos el entorno
load_dotenv(override=True)
api_key = os.environ.get("GEMINI_API_KEY")

# Inicializar cliente
client = genai.Client(api_key=api_key)

def consultar_ia(indicacion_o_pregunta: str) -> str:
    """
    Esta función recibe cualquier texto, se lo envía a Gemini 
    y te regresa la respuesta como un texto limpio (string).
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=indicacion_o_pregunta,
        )
        return response.text
    except Exception as e:
        return f"Error al conectar con la IA: {e}"

# Esto es solo por si ejecutas este archivo suelto para pruebas rapidas
if __name__ == "__main__":
    test = consultar_ia("Dame un saludo corto de felicitación.")
    print(test)