class Employee:
    '''Main Class with empty values for employee details'''
    first_name =''
    last_name = ""
    age = 0
    position = ''
    gender = ''

    def get_position(self):
        '''Returns the position of the employee'''
        return self.position

    def get_fullname(self):
        '''Returns the fullname of the employee'''
        return f'{self.first_name} {self.last_name}'


class Aaron(Employee):
    '''Employee Aaron details'''
    first_name = "Aaron"
    last_name = "Dela Cruz"
    position = "Tambay"

class Joelle(Employee):
    '''Employee Joelle details'''
    first_name = "Joelle"
    last_name = "Villanueva"
    position = "Python Developer"

class Miguel(Employee):
    '''Employee Miguel details'''
    first_name = "Miguel"
    last_name = "Santos"
    position = "Java Developer"

class Joelo(Employee):
    '''Employee Joelo details'''
    first_name = "Joelo"
    last_name = "Villanueva"
    position = "Valorant Master"

class Edward(Employee):
    '''Employee Edward details'''
    first_name = "Edward"
    last_name = "Domingo"
    position = "Programmer din siguro"

aaron = Aaron()
print(f'{aaron.get_fullname()} {aaron.get_position()}')

joelle = Joelle()
print(f'{joelle.get_fullname()} {joelle.get_position()}')

miguel = Miguel()
print(f'{miguel.get_fullname()} {miguel.get_position()}')

joelo = Joelo()
print(f'{joelo.get_fullname()} {joelo.get_position()}')

edward = Edward()
print(f'{edward.get_fullname()} {edward.get_position()}')