import pymysql

# Conectar con base de datos 
conn = pymysql.connect(
            host='sql5.freesqldatabase.com',
            database='sql5440351',
            user='sql5440351',
            password='gWjGTEXzxu',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )

# Creando la tabla 
cursor = conn.cursor()
sql_query = """ CREATE TABLE conductores (
    idConductor int(11) NOT NULL AUTO_INCREMENT,
    nombreCompleto varchar(255) NOT NULL,
    puesto varchar(100) NOT NULL,
    departamento varchar(100) NOT NULL,
    tipoLicencia varchar(60) NOT NULL,
    edad int(11) NOT NULL,
    fechaIngreso varchar(30) NOT NULL,
    antiguedad int(11) NOT NULL,
    ubicacion varchar(255) NOT NULL,
    PRIMARY KEY (idConductor)
    )
    AUTO_INCREMENT=1 ;"""

cursor.execute(sql_query)
conn.close()
