from flask import Blueprint, request, jsonify # type: ignore

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamaServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')

    codRes, menRes, accion = inicializarVariables(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(user,password):
    userLocal = "root"
    passLocal = "123samu456"
    codRes = 'SIN_ERROR'
    menRes = 'OK'

    try:
        print("Verificar login")
        if password == passLocal and user == userLocal:
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecto")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales o ususario incorrectas'


    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion
        
