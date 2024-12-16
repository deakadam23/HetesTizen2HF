def hetedik():
    # Beolvassuk a fájlt
    with open('dal.txt', 'r', encoding='utf-8') as f:
        sorok = f.readlines()

    # A sorokat fordított sorrendben tároljuk
    forditott_sorok = sorok[::-1]

    # Kiírjuk a fordított sorokat a képernyőre
    for sor in forditott_sorok:
        print(sor.strip())  # .strip() eltávolítja az esetleges új sor karaktereket

    # Kiírjuk a fordított sorokat egy új fájlba
    with open('forditott_dal.txt', 'w', encoding='utf-8') as f:
        f.writelines(forditott_sorok)