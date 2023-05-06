      
from Clase import PlanAhorro
from Menu_Opciones import Menu
from gestion_archivos import cargar_planes_desde_archivo
class Calculos:
    planes = cargar_planes_desde_archivo("planes.csv")
    @classmethod
    def actualiza_valor(cls,opcion:int):
        # Opción: Actualizar valor del vehículo de cada plan
        
        for plan in cls.planes:
            print("Plan:", plan.get_codigo())
            print("Modelo:", plan.get_modelo())
            print("Versión:", plan.get_version())
            nuevo_valor = float(input("Ingrese el nuevo valor del vehículo: "))
            PlanAhorro.actualizar_valor_vehiculo(plan, nuevo_valor)
        return "valor actualizado correctamente"
        
    @classmethod
    def muestraPlanes(cls):
        valorDado=float(input("Ingrese el valor que desea comparar:  "))
        planesInferiores=PlanAhorro.mostrar_planes_valor_inferior(valorDado)
        print("Planes con cuota inferior a", valorDado)
        if not planesInferiores:
            
            print("No hay cuotas inferiores a la ingresada ")
        else:
            for plan in planesInferiores:
        
                print("Plan:  ",plan.get_codigo())
                print("Modelo:   ",plan.get_modelo())
                print("Version:  ",plan.get_version())
                print("Valor:  ",plan.get_valor_vehiculo())
        return
    @classmethod
    def montoParalicitar(cls):
        for plan in cls.planes:
                        print("Plan:", plan.get_codigo())
                        print("Modelo:", plan.get_modelo())
                        print("Versión:", plan.get_version())
                        monto_licitacion = PlanAhorro.monto_pagar_licitacion(plan)
                        print("Monto a pagar para licitación:", monto_licitacion)


    @classmethod
    def modificarCuotas(cls):
        codigo_plan = int(input("Ingrese el código del plan a modificar: "))
        encontrado = False
        
        for i in range(len(cls.planes)):
        
            if cls.planes[i].get_codigo() == codigo_plan:
                print("get_codigo es:      y codigo plan es:   ",cls.planes[i].get_codigo(), codigo_plan)
                nuevas_cuotas = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
                cls.planes[i].set_cuotas_para_licitar(nuevas_cuotas)
                print("Cantidad de cuotas para licitar modificada exitosamente.")
                encontrado = True
        if not encontrado:
            print("No se encontró ningún plan con el código ingresado.")

         

                

                   
'''
                elif opcion == "2":
                    # Opción: Mostrar planes con cuota inferior a un valor dado
                    valor_dado = float(input("Ingrese un valor para comparar: "))
                    planes_inferiores = PlanAhorro.mostrar_planes_valor_inferior(valor_dado, planes)
                    print("Planes con cuota inferior a", valor_dado)
                    for plan in planes_inferiores:
                        print("Plan:", plan.get_codigo())
                        print("Modelo:", plan.get_modelo())
                        print("Versión:", plan.get_version())
                        print("Valor cuota:", plan.calcular_valor_cuota())

                elif opcion == "3":
                    # Opción: Mostrar monto a pagar para licitación
                    for plan in planes:
                        print("Plan:", plan.get_codigo())
                        print("Modelo:", plan.get_modelo())
                        print("Versión:", plan.get_version())
                        monto_licitacion = PlanAhorro.monto_pagar_licitacion(plan)
                        print("Monto a pagar para licitación:", monto_licitacion)

                elif opcion == "4":
                    # Opción: Modificar cantidad de cuotas para licitar
                    codigo_plan = input("Ingrese el código del plan a modificar: ")
                    encontrado = False
                    for plan in planes:
                        if plan.get_codigo == codigo_plan:
                            nuevas_cuotas = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
                            PlanAhorro.modificar_cuotas_licitacion(plan, nuevas_cuotas)
                            print("Cantidad de cuotas para licitar modificada exitosamente.")
                            encontrado = True
                    if not encontrado:
                        print("No se encontró ningún plan con el código ingresado.")

                
                elif opcion == "5":
                    # Opción: Salir
                    print("Programa finalizado.")'''