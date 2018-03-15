

class Employee(object):
    def __init__(self, name, email, bdate, level, address, phone, department):

        self.name = name
        self.email = email
        self.birth_date = bdate
        self.level = level
        self.address = address
        self.phone = phone
        self.department = department


class Department(object):
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager



employees = {'petre': Employee('petre', 'petre@petre.com', '2019-11-12', 'normal', 'str.brad bl.5 ap38', '0743234245', 'dep_scule'),
            'ion': Employee('ion', 'ion@plm.com', '1999-11-13', 'normal', 'str.pori bl 2 ap 42', '07324235343', 'dep_auto'),
             'cata' : Employee('cata', 'cata@yahoo.com' , '01.06.90', 'manager', 'str.ploi bl 1 ap1', '0723234231', 'dep_auto')

}

departments = {'dep_scule' : Department('dep_scule', 'petre'),
              'dep_auto' : Department('dep_auto' , 'cata' )


               }

def create_employee():
    # Step 1 - facem rost de datele de care avem nevoie ca sa cream un angajat
    name = input('Provide a name: ')
    email = input('Provide an email address: ')
    date = input('Provide a birth date - in whatever format you want: ')
    level = input('Provide level of the employee: ')
    address =input('Provide addres of the employee: ')
    phone = input ('What is the employee phone no.: ')
    department = input('For which department is the employee woring: ')

    # Step 2 - crearea unui angajat
    angajat = Employee(name, email, date, level, address, phone, department)
    # Cu variabila angajat acuma te potzi juca. Potzi sa zici ashe


    # Step 3
    employees[name] = angajat


def print_employees():
    for employee_name, employee in employees.items():
        print('Employee ', employee.name, ' with email: ', employee.email, ' with date of birth ', employee.birth_date, 'with function', employee.level, 'lives at: ', employee.address, 'rechable at: ', employee.phone, 'lucreaza in dep', employee.department)
# ia numele, emailul si data nastei care l-am introdus de la tastatura si le listeaza

def delete_employee():
    try:
        name = input("ce angajat sa stergem? ")
        del employees[name]
    except KeyError:
        print('Angajatul', name, 'nu exista')


def create_department():
    name = input('Department name: ')
    manager = input('Who is the manager of this dep: ')

    departament = Department(name, manager)
    print(departments)
    print(departament.manager)


    # Step 3
    departments[name] = departament


def delete_department():
    try:
        name = input("ce departament sa stergem? ")
        del departments[name]
    except KeyError:
        print('Departamentul' , name, 'nu exista')

def print_department():
    for departament_name, departament in departments.items():
        print('Departament ', departament.name, ' manager ', departament.manager)



ans = True

while ans:
    print("""
   1.Adauga un angajat
   2.Sterge un angajat
   3.Arata angajatii
   4.Adauga un departament
   5.Sterge un departament
   6.Arata departamente
   7.Iesire
   """)
    ans = input("Ce ai vrea sa faci? ")
    if ans == "1":
        create_employee()
    elif ans == "2":
        delete_employee()

    elif ans == "3":
        print_employees()

    elif ans == "4":
        create_department()


    elif ans =="5":
        delete_department()

    elif ans =="6":
        print_department()



    elif ans == "7":
        print("\n La revedere!")
        break
    else:
        print("\n Optiune invalida. Incearca din nou")
#commit
