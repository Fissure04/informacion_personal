import json


def info(event, context):
    body = {
        "nombre": "Juan Miguel Ceron Ocampo", "codigo": "240220232013", "fecha nacimiento": "17/07/2004", "edad": "20 años", "correo": "juan.ceron.0368@eam.edu.co", "direccion": "La Tebaida, Quindio"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
