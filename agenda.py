import csv

class agenda:
    def __init__(self):
        print 'Menu\n'
        print '1 Ver Agenda'
        print '2 Insertar'
        print '3 Salir'
        
        self.opcion = int(raw_input('Ingrese la opcion que desee:\t'))
        
        if self.opcion == 1:
            with open('data.csv','r') as file:
                data = csv.reader(file, delimiter = '|')
                for line in data:
                    print line
                        
        elif self.opcion == 2:
            self.nombre = str(raw_input('Ingrese el nombre: '))
            self.email = str(raw_input('Ingrese el email: '))
            self.telefono = str(raw_input('Ingresa el numero de telefono: '))
            
            with open('data.csv', 'a') as file:
                data = csv.writer(file, delimiter = '|')
                data.writerow([self.nombre, self.email, self.telefono])
                
        elif self.opcion == 3:
            exit()
        
            
agenda = agenda()
