#git is awesome
#corporate management
departament = ['dep_scule','manager','dep_aprov']
angajati = ['petru','marcel','florin','ovidiu','catalin','vlad']
angajati_departament = {
    'petru': 'dep_scule',
    'marcel': 'dep_scule ',
    'florin': 'dep_aprov',
    'ovidiu': 'dep_aprov',
    'catalin': 'manager',
    'vlad': 'manager'
}
ans=True
while ans:
    print ("""
   1.Adauga un angajat
   2.Sterge un angajat
   3.Arata angajatii
   4.Adauga un departament
   5.Sterge un departament
   6.Arata departamente
   7.Iesire
   """)
    ans=input("Ce ai vrea sa faci? ")
    if ans=="1":
        item = input("Cine sa fie adaugat: ")
        angajati.append(item)
        x = input("La ce departament?: ")
        print(angajati_departament)
        print("\n angajat adaugat")
        angajati_departament[item] = x
    elif ans=="2":
        item =input("cine sa fie sters: ")
        angajati.remove(item)
        print(angajati)
        print ("\n angajat sters")
        del angajati_departament[item]

    elif ans=="3":
      print("\n Lista angajati")
      print(angajati)
      print(angajati_departament)

      for angajat in angajati:
          print(angajat, ' - in departamentul :', angajati_departament[angajat])
    elif ans=="4":
        item =input("Adauga departament: ")
        departament.append(item)
        print(departament)

        print("\n Departament adaugat")
    elif ans=="5":
        item = input("sterge departament: ")
        departament.remove(item)
        print(departament)
        print ("\n angajat sters")
    elif ans=="6":
      print("\n Departamente")
      print(departament)

    elif ans=="7":
      print("\n La revedere!")
      break
    else:
      print("\n Optiune invalida. Incearca din nou")



