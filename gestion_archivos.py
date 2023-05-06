from Clase import PlanAhorro
#from Menu_Opciones import Menu

def cargar_planes_desde_archivo(nombre_archivo:str):
    planes = []
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(";")
            codigo = datos[0]
            modelo = datos[1]
            version = datos[2]
            valor_vehiculo = float(datos[3])
            cantidad_cuotas = int(datos[4])
            cuotas_licitacion = int(datos[5])
            plan = PlanAhorro(codigo, modelo, version, valor_vehiculo, cantidad_cuotas, cuotas_licitacion)
            planes.append(plan)
    return planes