class PlanAhorro:
    # Atributos estáticos
    __cant_cuotas = 0
    __cuotas_para_licitar = 0
    __codigo:int
    __modelo:str
    __version:str
    __valor_vehiculo:float

    planes = []

    def __init__(self, codigo, modelo, version, valor_vehiculo, cant_cuotas, cant_cuotas_licitacion):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor_vehiculo = valor_vehiculo
        self.__cant_cuotas = cant_cuotas
        self.__cuotas_para_licitar = cant_cuotas_licitacion
        PlanAhorro.planes.append(self)




    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version

    def get_valor_vehiculo(self):
        return self.__valor_vehiculo

    def set_valor_vehiculo(self, valor_vehiculo):
        self.__valor_vehiculo = valor_vehiculo

    def get_cant_cuotas(self):
        return self.__cant_cuotas

    def set_cant_cuotas(self, cant_cuotas):
        self.__cant_cuotas = cant_cuotas

    def get_cuotas_para_licitar(self):
        return self.__cuotas_para_licitar

    def set_cuotas_para_licitar(self, cuotas_para_licitar):
        self.__cuotas_para_licitar = cuotas_para_licitar

    def calcular_valor_cuota(self):
        importe_cuota = (self.__valor_vehiculo / self.__cant_cuotas) + self.__valor_vehiculo * 0.10
        return importe_cuota

    @staticmethod
    def actualizar_valor_vehiculo(plan, nuevo_valor):
        plan.set_valor_vehiculo(nuevo_valor)

    @staticmethod
    def mostrar_planes_valor_inferior(valor):
        planes_inferiores = []
        for plan in PlanAhorro.planes:
            valor_cuota = (plan.get_valor_vehiculo() / plan.get_cant_cuotas()) + plan.get_valor_vehiculo() * 0.10
            if valor_cuota < valor:
                planes_inferiores.append(plan)
        return planes_inferiores

    @staticmethod
    def monto_pagar_licitacion(plan):
        return plan.get_cuotas_para_licitar() * plan.calcular_valor_cuota()

    @staticmethod
    def modificar_cuotas_licitacion(plan:int, nuevas_cuotas:int):
        plan.set_cuotas_para_licitar(nuevas_cuotas)