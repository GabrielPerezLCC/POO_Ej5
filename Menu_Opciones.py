class Menu:
    # Menú de opciones  
    @classmethod 
    def mostrar_menu(cls):
        while True:
            print("Menú de opciones:")
            print("1- Actualizar valor del vehículo de cada plan")
            print("2- Mostrar planes con cuota inferior a un valor dado")
            print("3- Mostrar monto a pagar para licitación")
            print("4- Modificar cantidad de cuotas para licitar")
            print("5- Salir")
            opcion = input("Elija la opción deseada: ")
            if opcion in['1','2','3','4','5']:
                return opcion
            else:
                print("opcion invalida, intente nuevamente:   ")
            

        