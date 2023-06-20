import requests
import pdb

class Employee:
    gender = ""
    email = ""
    age = 0
    username = ""
    phone = ""
    dob = ""


    def create_employee(self):
        """Returns the full details of a random employee"""
        name = ""
        user_list = []
        dob_list = []
        data_dict = requests.get('https://randomuser.me/api/').json()
        for data in data_dict['results']:
            for name_data in data['name']:
                """Returns the complete name of employee"""
                name += data['name'][name_data] + " "

            for dob_data in data['dob']:
                """Returns the date of birth of employee"""
                initial_dob_data = data['dob'][dob_data]
                dob_list.append(initial_dob_data)
            dob = dob_list[0]
            age = dob_list[1]

            for login_data in data['login']:
                """Returns the list of login details of employee"""
                initial_data = data['login'][login_data]
                user_list.append(initial_data)

            username = user_list[1]
            password = user_list[2]
            gender = data["gender"]
            email = data['email']
            phone = data['phone']
        userdata = f"name: {name}\ngender: {gender}\nbirthday: {dob}\nage: {age} \nphone: {phone}\nemail: {email}\nusername: {username}\npassword: {password}"
        return userdata


employee = Employee()
print(employee.create_employee())
