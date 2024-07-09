import mysql.connector

miconexion = mysql.connector.connect(host="localhost", user ="root", password ="")
micursor = miconexion.cursor()

#comentas
micursor.execute("drop database  if exists proyecto_bbdd")
micursor.execute("create database proyecto_bbdd")
micursor.execute("use proyecto_bbdd")
micursor.execute("create table clientes (id_cliente int primary key auto_increment, codigo text (50),nombre text (50), direccion text (50), telefono text(50), situacion text (50), codigo_peli text (50) null)")
micursor.execute("create table peliculas(id_pelicula int primary key auto_increment, codigo text (50),nombre_peli text (50),genero text(50),situacion text (50), codigo_cliente text(50) null)")

sql = "INSERT INTO clientes(codigo, nombre, direccion, telefono, situacion) VALUES (%s, %s, %s, %s, %s)"
val =[
    ("C001", "Dayana", "Murguiondo 123", "34151234", "L"),
    ("C002", "María", "Avenida Siempre Viva 742", "34155678", "L"),
    ("C003", "Carlos", "Calle Principal 456", "34158765", "L"),
    ("C004", "Ana", "Boulevard de los Sueños 890", "34154321", "L"),
    ("C005", "Pedro", "Calle Secundaria 101", "34156789", "L"),
    ("C006", "Luisa", "Avenida de la Paz 102", "34159876", "L"),
    ("C007", "Miguel", "Calle de la Amistad 203", "341534562", "L"),
    ("C008", "Laura", "Calle de la Esperanza 304", "34156543", "L"),
    ("C009", "Jorge", "Avenida del Sol 405", "34157890", "L"),
    ("C010", "Sofia", "Calle de las Flores 506", "34150987", "L")
]
micursor.executemany(sql, val )
miconexion.commit() 

sql = "INSERT INTO peliculas(codigo, nombre_peli, genero, situacion) VALUES (%s, %s, %s, %s)"
val =[
    ("C001", "Inception", "Ciencia ficción", "L"),
    ("C002", "Titanic", "Romance", "L"),
    ("C003", "The Matrix", "Acción", "L"),
    ("C004", "Gladiator", "Drama", "A"),
    ("C005", "Avatar", "Ciencia ficción", "A"),
    ("C006", "The Lion King", "Animación", "L"),
    ("C007", "Forrest Gump", "Drama", "A"),
    ("C008", "The Godfather", "Crimen", "A"),
    ("C009", "Star Wars", "Ciencia ficción", "L"),
    ("C010", "Jurassic Park", "Aventuraa", "L")
]
micursor.executemany(sql, val ) 
miconexion.commit()

