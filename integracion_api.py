import requests

def obtener_datos_api(url):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"Error: Código de estado {respuesta.status_code}")
    except Exception as e:
        print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    url_api = "https://jsonplaceholder.typicode.com/posts/1"
    datos = obtener_datos_api(url_api)
    if datos:
        print(datos)
