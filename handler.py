import json


def my_info(event, context):
    body = {
        "nombre": "thomas garcia", "edad": "19", "cedula": "1094894584", 
        "direccion": "calle 25N #13-41", "profesion": "estudiante", 
        "telefono": "3157480639", "email": "garcia.thomas.9548@eam.edu.co"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
