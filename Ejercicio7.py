def get_code(file, sistema):

    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if sistema in directory:
            return directory[sistema]
        else:
            return('¡El cliente ' + sistema + ' no existe!\n')


def add_code(file, sistema, codigo):
    try: 
        f = open(file, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        f.write(sistema + ',' + codigo + '\n')
        f.close()
        return('El código se ha añadido.\n')

def remove_code(file, sistema):
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if sistema in directory:
            del directory[sistema]
            f = open(file, 'w')
            for name, telf in directory.items():
                f.write(name + ',' + telf)
            f.close()
            return ('¡El cliente se ha borrado!\n')
        else:
            return('¡El cliente ' + sistema + ' no existe!\n')


def menu():
    print('\n\tSistema de Apertura')
    print('============================')
    print('1 - Consultar un código')
    print('2 - Añadir un código')
    print('3 - Eliminar un código')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directory():
    file = 'listin.txt' 
    print("Bienvenido al sistema de apertura. Presione enter para continuar",end="")
    input()
    while True:
        option = menu()
        if option == '1':
            sistema = input('Introduce el nombre del sistema: ').title()
            print(get_code(file, sistema))
        elif option == '2':
            sistema = input('Introduce el nombre del sistema: ').title()
            code = input('Introduce el código del sistema: ')
            print(add_code(file, sistema, code))
        elif option == '3':
            sistema= input('Introduce el nombre del sistema: ').title()
            print(remove_code(file, sistema))
        elif option == '0':
            break
        else:
            print("Opción inválida")
            break
    return

directory()