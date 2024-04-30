import psycopg2

# Datos de conexión a la base de datos
PGHOST='ep-old-pine-a5j6vc9o.us-east-2.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='LVur8KJnz0Ua'

# Conexión a la base de datos
connection = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=5432, sslmode='require')

# Cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Solicitar al usuario el nombre del departamento
departamento = input("Ingrese el nombre del departamento: ")

# Consultar el código del municipio del departamento especificado
cursor.execute("SELECT codigo_municipio FROM municipios WHERE codigo_departamento IN (SELECT codigo_departamento FROM departamentos WHERE nombre_departamento = %s);", (departamento,))
codigo_municipio = cursor.fetchone()

if codigo_municipio:
# Utilizar el código del municipio para obtener el nombre del municipio (que será la capital)
    cursor.execute("SELECT nombre_municipio FROM municipios WHERE codigo_municipio = %s;", (codigo_municipio[0],))
    capital = cursor.fetchone()

    if capital:
        print(f"La capital del departamento {departamento} es: {capital[0]}")
    else:
        print("No se encontró la capital del departamento especificado.")
else:
    print("Departamento no encontrado.")

# Cerrar la conexión y el cursor
cursor.close()
connection.close()