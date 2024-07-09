from bbdd import miconexion,micursor

def menu():
    print("BIENVENIDO A LA APP")#menu pricipal
    usuario = int(input("OPCIONES:\n1-INICIAR SESION\n2-REGISTARSE\n3-SALIR\n"))
    if usuario ==1:
        datos = iniciarsesion()
        if len(datos) != 0:
            menuUser(datos)
    elif usuario ==2:
        registrarse()
        menu()
    elif usuario ==3:
        print("GRACIAS POR USAR LA APLICACION")
        quit()#salir
    else:
        print("elija una opcion correcta\n")


def iniciarsesion():#inicio de sesion
    nombre = str(input("ingrese su nombre\n"))
    password = str(input("Ingrese su password\n"))
    micursor.execute(f"select * from clientes where nombre ='{nombre}' and codigo ='{password}'\n")
    resultado =micursor.fetchall() #todo lo que encuentra guarda aca en fetchall sinonimo de select de sql
    if len(resultado) !=0:
        print("Sesion iniciada correctamente\n")
    else:
        print("ACCESO DENEGADO\n")
        menu()
    return resultado


def registrarse():
    #codigo = str(input("Ingrese su codigo\n"))
    nombre = str(input("Ingrese su nombre\n"))
    direccion = str(input("Ingrese su direcion\n"))
    telefono = str(input("Ingrese su telefono\n"))
    sql = ("insert into clientes (codigo,nombre,direccion,telefono, situacion ) values (%s,%s,%s,%s, %s)")
    val = ("C011", nombre, direccion, telefono, "L") # codigo y situacion colocamos manual
    micursor.execute(sql, val)
    miconexion.commit()
    print("Usuario registrado.")

def menuUser(usuario):
    print(f"BIENVENIDO {usuario[0][2]} AL MENU USUARIO\n") #sub indice 2 de la tupla
    opcion2 =int(input("OPCIONES:\n1-Ver sus datos\n2-Modificar sus datos\n3-Darse de baja\n4-Ver todas las peliculas\n5-Ver solo disponibles\n6-Alquilar pelicula\n7-Devolver pelicula\n8-Atras\n9-SALIR\n"))
    if opcion2 ==1:
        verDatos(usuario)#el parametro es del input de iniciar sesion
        menuUser(usuario)
    elif opcion2 ==2:
       modificarDatos(usuario)#el parametro es del input de iniciar sesion
       menu()
    elif opcion2 ==3:
        darsedebaja(usuario)#el parametro es del input de iniciar sesion
        menu()
    elif opcion2 ==4:
        ver_todas_las_pelis()#ver todas las pelis
        menuUser(usuario)
    elif opcion2 ==5:
        ver_solo_disponibles()#ver solo disponibles
        menuUser(usuario)
    elif opcion2 ==6:
        alquilar_peli(usuario)#alquilar pelicula
        menuUser(usuario)
    elif opcion2 ==7:
        devolver_peli(usuario)#devolver pelicula
        menuUser(usuario)
    elif opcion2 ==8:
        menu()#atras
    elif opcion2 ==9:
        print("GRACIAS POR USAR LA APLICACION")
        quit()#sirve salir
    else:
        print("elija una opcion correcta\n")

def verDatos(user):
    print("DATOS PERSONALES\n")
    print("ID", " CODIGO ", " NOMBRE ", " DIRECCION ", " TELEFONO ", " SITUACION ", "CODIGO_PELI")#ID Y CODIGO PELI NO VA corregir
    for i in user:
        1
        print(i)
        
def modificarDatos(user): #user colocar en parametro
    opcion = int(input("Elija una opcion:\n1-Modificar telefono.\n2-Modificar direccion\n"))
    if opcion == 1:
        newtelefono =str(input("Ingrese su nuevo numero\n"))
        micursor.execute(f"update  clientes set telefono ='{newtelefono}' where  id_cliente= {user[0][0]} ") # id del usuario
        miconexion.commit()
        print("EL TELEFONO SE MODIFICO CORRECTAMENTE\n")
    elif  opcion == 2:
        newdireccion =str(input("Ingrese su nnueva direccion\n"))
        micursor.execute(f"update clientes set direccion = '{newdireccion}' where id_cliente='{user[0][0]}'")# id del usuario con la tupla y subindice
        miconexion.commit()
        print("LA DIRECCION SE MODIFICO CCORRECTAMENTE\n")
       
    else:
       print("Opción no válida, por favor ingrese una opcion valida.\n") #corregido
       
       
       
def darsedebaja(user):
    usuario1=int(input("Esta seguro que quiere darce de baja\n1-Si estoy seguro\n2-No estoy seguro\n"))
    if usuario1 ==1:
        micursor.execute(f"delete  from  clientes where  id = {user[0][0]} ")
        miconexion.commit()
        print("Usuario dado de baja correctamente")
    elif usuario1 ==2:
        menuUser(user)
    else:
        print("Ingrese una opcion correcta\n")
#pelis
def ver_todas_las_pelis ():   #corregido
        print("PELICULAS\n")
        micursor.execute("select * from peliculas")
        resultado =micursor.fetchall()
        print("CODIGO   NOMBRE  SITUACION  GENERO  SITUACION\n")
        for i in resultado:
            print(i[1], i[2])
            
def ver_solo_disponibles():
        print("PELICULAS DISPONIBLES\n")
        micursor.execute("select * from peliculas where  situacion = 'l'")
        resultado =micursor.fetchall()
        print("CODIGO   NOMBRE  SITUACION\n")
        for i in resultado:
            print(i[1]  , i[2]  ,i[4])
           
             
            
def alquilar_peli(user):
        codigo_peli =str(input("Ingrese el codigo de la pelicula que quiere alquilar\n"))
        micursor.execute(f"update clientes set situacion ='A' where id_cliente = '{user[0][0]}' ")
        micursor.execute(f"update clientes set codigo_peli = '{codigo_peli}' where id_cliente = '{user[0][0]}' ")  #corregir
        micursor.execute(f"update peliculas set situacion ='A' where  codigo = '{codigo_peli}' ")
        micursor.execute(f"update peliculas set codigo_cliente= '{user[0][1]}' where codigo = '{codigo_peli}' ") #CODIGO QUE PASO EL USUARIO
        miconexion.commit()
        print("Pelicula alquilada correctamente\n")

def devolver_peli (user):
        codigo_peli =str(input("Ingrese el codigo de la pelicula que quiere devolver\n"))
        micursor.execute(f"update clientes set situacion ='L' where id ={[0][0]}") #id_user
        micursor.execute(f"update clientes set codigo_peli = 'null' where id = {user[0][0]}")
        micursor.execute(f"update peliculas set situacion ='L' where id = {codigo_peli}")
        micursor.execute(f"update peliculas set codigo_cliente = null where codigo = {codigo_peli}")
        miconexion.commit()
        print("Pelicula devuelta correctamente\n")
    
menu()

