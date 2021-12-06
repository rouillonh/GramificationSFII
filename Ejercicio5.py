def tabla_multiplicar():  
  n = int(input('Introduce un número entero entre 1 y 10: '))
  file_name = 'tabla-' + str(n) + '.txt'
  f = open(file_name, 'w')
  for i in range(10):
      f.write(str(n) + ' x ' + str(i+1) + ' = ' + str(n * (i+1)) + '\n')
  f.close()

tabla_multiplicar()