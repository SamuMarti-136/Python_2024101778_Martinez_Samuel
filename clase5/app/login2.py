from flask import Blueprint, request, jsonify # type: ignore
import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

login2 = Blueprint('login2', __name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123samu456',
    'database': 'localhost',
    'port':'3306'
}

@login2.route('/login2', methods=['POST'])
def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
    
    codRes, menRes, usuario, accion = verificar_credenciales(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': usuario,
        'accion': accion
    }
    return jsonify(salida)

def verificar_credenciales(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    usuario = None
    
    try:
        print("Verificar login")
        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        
        # Ejecutar la consulta SQL
        query = "SELECT username FROM users WHERE username = %s AND pass = %s"
        cursor.execute(query, (user, password))
        
        # Obtener el resultado
        result = cursor.fetchone()
        
        if result:
            usuario = result['username']
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, usuario, accion