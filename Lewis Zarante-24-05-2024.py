gestion_educativa = {}
pendiente = []
import os

def fnt_agregar(apellidos, nombres, contacto ,edad ,sexo, nota, direcciones):
    if sexo.lower() == 'm':
        if 11 <= int(edad) <= 36 and 1 <= int(nota) <= 5:
            gestion_educativa[apellidos] = {'nombre': nombres, 'contacto': contacto, 'edad': edad,  'sexo': sexo, 'nota': nota, 'direcciones': direcciones}
            enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')
        else:
            pendiente.append(contacto)
    elif sexo.lower() == 'f':
        if 11 <= int(edad) <= 36 and 1 <= int(nota) <= 5:
            gestion_educativa[apellidos] = {'nombre': nombres, 'contacto': contacto, 'edad': edad,  'sexo': sexo, 'nota': nota, 'direcciones': direcciones}
            enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')
        else:
            pendiente.append(contacto)
    else:
        pendiente.append(contacto)
        enter = input('\nNo cumple con los criterios de registro <ENTER>')
        
def fnt_selector():
    opcion = input('\n1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    return opcion
        
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    opcion = fnt_selector()
    if opcion == '1':
        apellidos = input('Apellidos: ')
        nombre = input('Nombre: ')
        contacto = input('Contacto: ')
        edad = input('Edad: ')
        nota = input('Nota:  ')
        sexo = input("Sexo [M/F]: ")
        direccion = input('Dirección: ')
        fnt_agregar(apellidos, nombre, contacto, edad,  sexo, nota, direccion)
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nCantidad de registros:', len(gestion_educativa), '\n')
        for Buscador, datos in gestion_educativa.items():
            print(f"{Buscador}: {datos}")
        if pendiente:
            print('\nPersonas  no registrados:')
            for contacto in pendiente:
                print(apellidos,nombre)
        input('\nPresione ENTER para continuar...')
    elif opcion == '3':
        break