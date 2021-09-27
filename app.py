#imortacion de clases de python
from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

#inicio de la aplicacion 
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#definimos la conexion en la base de datos para el uso de ella misma en este caso 
#esta guardada en la nuebe 
def db_connexion():
    conn = None
    try:
       conn = pymysql.connect(
            host='sql5.freesqldatabase.com',
            database='sql5440351',
            user='sql5440351',
            password='gWjGTEXzxu',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
    except pymysql.Error as e:
        print(e)
    return conn

#definimos el constructor para el uso de ella
class Conductores():
#definimos el contructor
    def __init__(self, nombreCompleto, puesto, departamento, tipoLicencia,
                 edad, fechaIngreso, antiguedad, ubicacion):
        
        self.nombreCompleto = nombreCompleto
        self.puesto = puesto
        self.departamento = departamento
        self.tipoLicencia = tipoLicencia
        self.edad = edad
        self.fechaIngreso = fechaIngreso
        self.antiguedad = antiguedad
        self.ubicacion = ubicacion

#consulta a todos los registro existentes en la base de datos
@app.route('/consultar', methods=['GET'])
def Conusltar():
    conn = db_connexion()
    cursor = None
    cursor = conn.cursor()
    #si es metodo get puede ejecutar la sentencia 
    if request.method == "GET":
        cursor.execute("SELECT * FROM conductores")
        #aqui descompimimos el arreglo de conductores iterando en un for
        conductores = [
            dict(idConductor=row['idConductor'], nombreCompleto=row['nombreCompleto'],
                 puesto=row['puesto'], departamento=row['departamento'],tipoLicencia=row['tipoLicencia'],
                 edad=row['edad'], fechaIngreso=row['fechaIngreso'],antiguedad=row['antiguedad'],ubicacion=row['ubicacion'])
                 for row in cursor.fetchall()
        ]
        #retornamos las respuesta
        return jsonify(conductores)
        
#primera ruta para incertar en la base de datatos dandole el metodo post 
@app.route('/agregar', methods=['POST'])
#cracion del metodo para el consumo de la API
def create():
    conn = db_connexion()
    cursor = conn.cursor()
    sql = """INSERT INTO conductores (nombreCompleto, puesto, departamento, tipoLicencia, edad, fechaIngreso, antiguedad, ubicacion)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    nombre = request.json["nombreCompleto"],
    puesto = request.json["puesto"],
    departamento = request.json["departamento"],
    tipoLicencia = request.json["tipoLicencia"],
    edad = request.json["edad"],
    fechaIngreso = request.json["fechaIngreso"],
    antiguedad = request.json["antiguedad"],
    ubicacion = request.json["ubicacion"]
    
    cursor = cursor.execute(sql, (nombre, puesto, departamento, tipoLicencia, edad, fechaIngreso, antiguedad, ubicacion))
    conn.commit()
    return "OK"

#metodo para editar los registros del conductor en la base de datos
@app.route('/editar/<id>', methods=['PUT'])
def editar(id):
    conn = db_connexion()
    cursor = conn.cursor()
    # Se realizar la ejecucion a la tabla busacndo el id del cliente  
    sql = """UPDATE conductores
            SET nombreCompleto=%s, 
                puesto=%s, 
                departamento=%s,
                tipoLicencia=%s, 
                edad=%s, 
                fechaIngreso=%s,
                antiguedad=%s, 
                ubicacion=%s 
                WHERE idConductor=%s"""

    #hacemos el resquest n json para insercion de datos
    nombre = request.json["nombreCompleto"],
    puesto = request.json["puesto"],
    departamento = request.json["departamento"],
    tipoLicencia = request.json["tipoLicencia"],
    edad = request.json["edad"],
    fechaIngreso = request.json["fechaIngreso"],
    antiguedad = request.json["antiguedad"],
    ubicacion = request.json["ubicacion"]
    # Se hace un array de respuesta para ver que se modificaco tambien como la respuesta
    actulizar_conductor = {
        "id": id,
        "nombreCompleto": nombre,
        "puesto": puesto,
        "departamento": departamento,
        "tipoLicencia": tipoLicencia,
        "edad": edad,
        "fechaIngreso": fechaIngreso,
        "antiguedad": antiguedad,
        "ubicacion": ubicacion
    }
    # Se executa el comando sql y se pasan los datos con los onjetos obtenidos
    cursor.execute(sql, (nombre, 
                        puesto, 
                        departamento, 
                        tipoLicencia, 
                        edad, 
                        fechaIngreso, 
                        antiguedad, 
                        ubicacion, 
                        id,))
    conn.commit()
    return jsonify(actulizar_conductor) 

#metodo para buscar el registro exixtenete en la bd buscando por el id del conductor
@app.route('/buscar/<id>', methods=['GET'])
def buscar(id):
        conn = db_connexion()
        cursor = conn.cursor()
        consuctor = None
        # Si recoibe una peteción GET
        if request.method == 'GET':
            # Se realizar consulta a la base de datos donde el estatus sea 1 (activo) y el id coincida con el que se esta recibiendo
            cursor.execute("SELECT * FROM conductores WHERE idConductor=%s", (id,))
            rows = cursor.fetchall()
            for r in rows:
                conductor = r
            if conductor is not None:
                return jsonify(conductor), 200
            else:
                return "Algo salio mal", 404
            
#metodo para eliminar todos los registros de la base de datos de un conductor
@app.route('/eliminar/<id>', methods=['POST'])
def delete(id):
    conn = db_connexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM conductores WHERE idConductor=%s", (id,))
    conn.commit()
    return "se eliino el conductor"
 
@app.route('/')
def index():
    return 'Hola'

#metodo para levantar el servidor local
if __name__ == "__main__":
    app.run(debug=True)