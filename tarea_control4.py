import os
def Limpiar_pantalla():
    os.system('cls')

def mostrar_menu():
    while True:
        os.system('cls')
        try:
            op=int(input('''
            ======== MENU DE PRODUCTOS ==========
            1. Agregar producto 
            2. Buscar producto
            3. Eliminar producto
            4. Salir
            Elija opcion: '''))
            if op< 1 or op >4:
                print("Debe ingresar un numero entre 1 a 4")
                os.system('pause')
            else:
                return op
        except ValueError:
            print("Opcion invalida")
            os.system('pause')
#############################################################3333
producto_list=[]
def agregar_producto():
    nombre=str(input("Ingrese el nombre del producto: "))
    while True:
        categoria=str(input("Ingrese su categoria: "))
        if validar__categoria(categoria):
            break
    while True:
        cantidad=int(input("Ingrese la cantidad: "))    
        if validar_cantidad(cantidad):
            break
    
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad
    }
    producto_list.append(producto)
    imprimir_producto(producto)
    print("Auto grabado con exito.")
def imprimir_producto(producto):
    print(f'''
    ---------------------
    nombre: {producto["nombre"]}
    categoria: {producto["categoria"]}
    cantidad: {producto["cantidad"]}
          ''')
def validar__categoria(categoria):
    if categoria in ["electronica", "muebles", "ropa"]:
        return True
    else:
        print("ERROR: debe ingresar (electronica, muebles, ropa). ")
        return False
def validar_cantidad(cantidad):
    if cantidad <=0:
        print("Debes ingresar un numero mayor a 0")
        return False
    return True
##############################################################################
def buscar_producto():
    encontrado = False
    if not producto_list:
        print("No se han registrados productos.")
        return
    print("\n Buscar producto")
    nombre=str(input("Ingrese el nombre del producto: "))
    for producto in producto_list:
        if producto ['nombre']== nombre:
            encontrado=True
            imprimir_producto(producto)
    if not encontrado:
        print(f"ERROR: Producto mo registrado: {nombre}")
###############################################################################
def eliminar_producto():
    encontrado = False
    if not producto_list:
        print("No se han registrados productos.")
        return
    print("\n Buscar producto")
    nombre=str(input("Ingrese el nombre del producto: "))
    for producto in producto_list:
        if producto ['nombre']== nombre:
            encontrado=True
            producto_list.remove(producto)
            print("Producto eliminado correctamente.")
    if not encontrado:
        print(f"ERROR: Producto mo registrado: {nombre}")
    

    
     
           
while True:
    Limpiar_pantalla() 
    opcion=mostrar_menu()
    if opcion==1:
        os.system('cls')
        agregar_producto()
        os.system('pause')
    elif opcion==2:
        os.system('cls')
        buscar_producto()
        os.system('pause')
    elif opcion==3:
        os.system('cls')
        eliminar_producto()
        os.system('pause')
    elif opcion==4:
        os.system('cls')
        input("Salir del programa presione <ENTER>")
        break

    
