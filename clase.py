employees = {}
department = {}


class Employee(object):
    def __init__(self, name, email, bdate):
        # Mai sus: self - ii un parametru "magic". El se refera la angajatul care se creeaza acuma
        # name, email, si bdate is 3 argumente pe care tre sa i le dai tu, ca sa itzi poata crea
        # un angajat.

        # Astea 3 linii ajuta la creearea angajatului
        # angajatul ii "self", si pe el vor fi puse astea 3 atribute
        self.name = name
        self.email = email
        self.birth_date = bdate

        # Dupa ce s-o executat liniile de mai sus, vei avea un angajat sanatos!


class Department(object):
    def __init__(self, name, manager):
        # Mai sus: self - ii un parametru "magic". El se refera la angajatul care se creeaza acuma
        # name, email, si bdate is 3 argumente pe care tre sa i le dai tu, ca sa itzi poata crea
        # un angajat.

        # Astea 3 linii ajuta la creearea angajatului
        # angajatul ii "self", si pe el vor fi puse astea 3 atribute
        self.name = name
        self.manager = manager

        # Dupa ce s-o executat liniile de mai sus, vei avea un angajat sanatos!


def create_employee():
    # Step 1 - facem rost de datele de care avem nevoie ca sa cream un angajat
    name = input('Provide a name: ')
    email = input('Provide an email address: ')
    date = input('Provide a birth date - in whatever format you want: ')

    # Step 2 - crearea unui angajat
    angajat = Employee(name, email, date)
    # Cu variabila angajat acuma te potzi juca. Potzi sa zici ashe
    print(angajat)
    print(angajat.birth_date)
    print(angajat.email)

    # Step 3
    employees[name] = angajat


def print_employees():
    for employee_name, employee in employees.items():
        print('Employee ', employee.name, ' with email: ', employee.email, ' with date of birth ', employee.birth_date)


def delete_employee():
    name = input("ce angajat sa stergem? ")
    del employees[name]

def create_department():
    name = input('Department name: ')
    manager = input('Who is the manager of this dep: ')

    departament = Department(name, manager)
    print(department)
    print(departament.manager)


    # Step 3
    department[name] = departament


def delete_department():
    name = input("ce departament sa stergem? ")
    del department[name]

def print_department():
    for departament_name, departament in department.items():
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
