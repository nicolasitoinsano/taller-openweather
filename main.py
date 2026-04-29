import requests
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# URL base de OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def consultar_clima(ciudad):
    """Consulta el clima actual de una ciudad."""
    
    # Parámetros que le enviamos a la API
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",   # temperatura en Celsius
        "lang": "es"         # respuesta en español
    }
    
    try:
        # Hacemos la petición GET a la API
        response = requests.get(BASE_URL, params=params)
        
        # Verificamos si la respuesta fue exitosa (código 200)
        response.raise_for_status()
        
        # Convertimos la respuesta a JSON
        datos = response.json()
        
        # Extraemos los datos que nos interesan
        print("\n===== CLIMA ACTUAL =====")
        print(f"Ciudad:      {datos['name']}, {datos['sys']['country']}")
        print(f"Descripción: {datos['weather'][0]['description']}")
        print(f"Temperatura: {datos['main']['temp']}°C")
        print(f"Sensación:   {datos['main']['feels_like']}°C")
        print(f"Humedad:     {datos['main']['humidity']}%")
        print(f"Viento:      {datos['wind']['speed']} m/s")
        print("========================\n")
        
    except requests.exceptions.HTTPError as e:
        # Error del servidor (401 key inválida, 404 ciudad no encontrada)
        print(f"Error HTTP: {e}")
        print(f"Código: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        # Sin conexión a internet
        print("Error: No hay conexión a internet.")
        
    except requests.exceptions.Timeout:
        # La API tardó demasiado
        print("Error: La petición tardó demasiado.")

# Programa principal
if __name__ == "__main__":
    ciudad = input("¿De qué ciudad quieres saber el clima? ")
    consultar_clima(ciudad)