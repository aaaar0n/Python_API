import requests
from unidecode import unidecode
import pdb

class Employee:
    age = 0
    username = ""
    email = ""
    password = ""
    phone = ""
    userdata = ""

    def create_user_data(self):
        data_dict = requests.get('https://randomuser.me/api/').json()
        name = ""
        login = ""
        login_list = []
        for data in data_dict['results']:
            for name_data in data['name']:
                initial_name = data['name'][name_data]
                name += initial_name + " "
            #pdb.set_trace()

        for data in data_dict['results']:
            for login_data in data['login']:
                initial_login_info = data['login'][login_data]
                login_list.append(initial_login_info)
            username = login_list[1] 
            password = login_list[2]  

        for data in data_dict['results']:
            gender = data["gender"]
            email = data['email']
            phone = data['phone']
        userdata = f"name: {name}\ngender: {gender}\nphone: {phone}\nemail: {email}\nusername: {username}\npassword: {password}"
        return userdata
            
class Employee_One(Employee):
    pass

employee = Employee_One()
print(employee.create_user_data())