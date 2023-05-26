class Employee:
    first_name =''
    last_name = ""
    age = 0
    position = ''
    gender = ''

    def get_position(self):
        return self.position

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'


class Aaron(Employee):
    first_name = "Aaron"
    last_name = "Dela Cruz"
    position = "Tambay"

class Joelle(Employee):
    first_name = "Joelle"
    last_name = "Villanueva"
    position = "Python Developer"

class Miguel(Employee):
    first_name = "Miguel"
    last_name = "Santos"
    position = "Java Developer"

class Joelo(Employee):
    first_name = "Joelo"
    last_name = "Villanueva"
    position = "Valorant Master"

class Edward(Employee):
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