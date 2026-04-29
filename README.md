# Taller: Consumo de API Externa — OpenWeatherMap
**Estudiante:** Tu nombre aquí  
**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Instructor:** Ing. Edwin Marín  
**Fecha:** Abril 2026

---

## ¿Qué problema resuelve la API?

OpenWeatherMap resuelve el problema de acceder a datos
meteorológicos en tiempo real sin necesidad de tener
estaciones físicas propias. Permite a cualquier aplicación
consultar temperatura, humedad, viento y pronósticos de
más de 200.000 ciudades del mundo mediante simples
peticiones HTTP.

**Ejemplo de uso real:** una app de domicilios puede
mostrarle al repartidor si va a llover, o un sistema
agrícola puede activar el riego automático según
el pronóstico.

---

## ¿Qué métodos HTTP usa y qué datos retorna?

Usa principalmente el método **GET**, porque solo estamos
*consultando* datos, no creando ni modificando nada.

**Endpoint usado:**
GET https://api.openweathermap.org/data/2.5/weather

**Parámetros enviados:**
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| q | Bogota | Nombre de la ciudad |
| appid | {API_KEY} | Clave de autenticación |
| units | metric | Temperatura en Celsius |
| lang | es | Respuesta en español |

**Ejemplo de respuesta JSON:**
```json