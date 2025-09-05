continuar = 'si'
while continuar == 'si' or continuar == 's':
    nombre = input('\nDime tú nombre: ')
    edad = int(input('Dime tú edad: '))
    
    if edad > 18:
        print('Eres mayor de edad\n')
        print (f"Hola {nombre}, tienes: {edad}")
    
    elif edad == 18:
        print('Tienes 18 años, apenas mayor de edad')    
    
    else:
        print('No cumples con la mayoría de edad')

    continuar = input('\n¿Quieres continuar? (si/no): \nResp/ ')