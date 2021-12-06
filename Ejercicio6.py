def leer_fichero():  
    n = int(input('Introduce un número entero entre 1 y 10: '))
    file_name = 'tabla-' + str(n) + '.txt'
    try: 
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', n)
    else:
        print(f.read())
    f.close()
leer_fichero()

