from Clase import PlanAhorro
from Menu_Opciones import Menu
from Calculos import Calculos

if __name__ == "__main__":
    opcion=None
    continuar=True
    while opcion !=5 and continuar:

        opcion=int(Menu.mostrar_menu())
        #print("opcion elegida   ",opcion)
        if opcion==1:
            resultado=Calculos.actualiza_valor(opcion)
            print(resultado)

        elif opcion==2:
            Calculos.muestraPlanes()
            
        elif opcion==3:
            Calculos.montoParalicitar()
        
        elif opcion==4:
            Calculos.modificarCuotas()
            






        if opcion==5:
            continuar=False
