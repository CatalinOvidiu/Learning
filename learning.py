def create_employee():
    item = input("Cine sa fie adaugat: ")
    angajati.append(item)
    x = input("La ce departament?: ")
    address = input('Adauga adresa: ')
    date = input('data nasteri: ')
    born_date[item] = date
    angajati_departament[item] = x
    address_employees[item] = address
    print(angajati_departament)

##test shit, not working
def delete_employee():
    item = input("cine sa fie sters: ")
    angajati.remove(item)
    print(angajati)
    print("\n angajat sters")
    del angajati_departament[item]


def list_employees():
    print("\n Lista angajati")
    print(angajati)
    for angajat in angajati:
        print(angajat, ' - in departamentul :', angajati_departament[angajat])
    for adresa in address_employees:
        print(adresa, '-la adresa :', address_employees[adresa])
    for date in born_date:
        print(date, '- la data :', born_date[date])


def add_department():
    global item
    item = input("Adauga departament: ")
    departament.append(item)
    manager = input('Cine sa fie manager?')
    manager_dep[item] = manager
    print(departament)
    print("\n Departament adaugat")


def delete_department():
    global item
    item = input("sterge departament: ")
    departament.remove(item)
    print(departament)
    print("\n angajat sters")


contact = {'catalin': 'catalin.theboss@gmail.com',
           ' vlad': 'vlad.thesupreemboss@yahoo.com'}
contact_cu_publicul = {' catalin' : '08:00 to 17:00',
                        'vlad' : '09:00 to 18:00'}
phone_contact = {'catalin' : '0234225151','vlad':'0251852'}
angajati = ['petru', 'marcel', 'florin', 'ovidiu', 'catalin', 'vlad']
departament = ['dep_scule', 'manager', 'dep_aprov']
manager_dep = {'catalin': 'manager la dep_scule',
               'vlad': 'manager la dep_aprov'}

address_employees = {'petru': 'strada bradului 5/38',
                     'marcel': 'strada bujorului 2/14',
                     'florin': 'strada lalelei 4/23',
                     'oviduiu': 'strada mori 3/12',
                     'catalin': 'str macului 6/50',
                     'vlad': 'str mori 7/24'}
born_date = {'petru': '01.02.90',
             'marcel': '01.12.95',
             'florin': '14.09.94',
             'oviduiu': '03.12.92',
             'catalin': '01.06.90',
             'vlad': '25.10.55'}

angajati_departament = {
    'petru': 'dep_scule',
    'marcel': 'dep_scule ',
    'florin': 'dep_aprov',
    'ovidiu': 'dep_aprov',
    'catalin': 'manager',
    'vlad': 'manager'
}

ans = True

while ans:
    print("""
   1.Adauga un angajat
   2.Sterge un angajat
   3.Arata angajatii
   4.Adauga un departament
   5.Sterge un departament
   6.Arata departamente
   7.Manageri
   8.Contact
   9.Iesire
   """)
    ans = input("Ce ai vrea sa faci? ")
    if ans == "1":
        create_employee()
    elif ans == "2":
        delete_employee()

    elif ans == "3":
        list_employees()
    elif ans == "4":
        add_department()
    elif ans == "5":
        delete_department()
    elif ans == "6":
        print("\n Departamente")
        print(departament)
        print("\n Manageri departamente")
        print(manager_dep)
    elif ans == "7":
        for manager in manager_dep:
            print(manager, manager_dep[manager])

    elif ans == "8":
        print('\n Contact bossi','si', 'plangeri')
        for cont in contact:
            print(cont,'pentru plangeri: ', contact[cont])
        for phone in phone_contact:
            print(phone,'contact at: ', phone_contact[phone])
        for public in contact_cu_publicul:
            print(public, 'contact cu publicul', contact_cu_publicul[public])



    elif ans == "9":
        print("\n La revedere!")
        break
    else:
        print("\n Optiune invalida. Incearca din nou")
