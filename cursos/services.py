import json
import urllib.request

# aca defino el servicio que consume la API REST externa de mindicador.cl
def obtener_conversion_monedas(precio_clp):
    """
    aca consulto el servicio externo de https://mindicador.cl/api
    para traer los valores oficiales del Dolar y la UF en tiempo real,
    y calcular la conversion del precio de los cursos para alumnos internacionales.
    """
    url = "https://mindicador.cl/api"
    try:
        # aca convierto el precio a float (por si viene como Decimal de Django)
        precio_num = float(precio_clp)
        # aca configuro la peticion HTTP GET con cabecera User-Agent y timeout de 3 segundos
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'DirectorioCursosDjango/1.0'}
        )
        with urllib.request.urlopen(req, timeout=3) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                
                # aca extraigo el valor del dolar observado y de la unidad de fomento (UF)
                dolar_valor = data.get('dolar', {}).get('valor', 0)
                uf_valor = data.get('uf', {}).get('valor', 0)

                # aca calculo los precios equivalentes redondeados a dos decimales
                precio_usd = round(precio_num / dolar_valor, 2) if dolar_valor > 0 else 0
                precio_uf = round(precio_num / uf_valor, 2) if uf_valor > 0 else 0

                return {
                    'disponible': True,
                    'dolar': f"{dolar_valor:,.2f}".replace(',', '.'),
                    'uf': f"{uf_valor:,.2f}".replace(',', '.'),
                    'precio_usd': f"{precio_usd:,.2f}",
                    'precio_uf': f"{precio_uf:,.2f}",
                    'fecha': data.get('fecha', '')[:10],
                    'fuente': 'mindicador.cl',
                }
    except Exception as e:
        # aca capturo cualquier excepcion (ej: fallo de internet o timeout) para que la pagina nunca se caiga
        print(f"Aviso: No se pudo conectar a la API externa mindicador.cl ({e})")
        return {
            'disponible': False,
            'error': str(e),
        }

    return {'disponible': False}
