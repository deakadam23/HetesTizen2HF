def tizenkettes():
    # Beolvassuk a bowling állást
    bowling_allas = input(
        "Kérlek, add meg a bowling állást (0 - ledöntött bábú, minden más - helytelen dobás, szóközökkel elválasztva): ")

    # Az inputot szóközökkel elválasztott számok listájává alakítjuk
    babu_lista = bowling_allas.split()

    # Összes dobás
    osszes_dobas = len(babu_lista)

    # Helyes dobások száma (0-kat számolunk)
    helyes_dobasok = babu_lista.count('0')

    # Helytelen dobások száma (minden olyan dobás, ami nem 0)
    helytelen_dobasok = sum(1 for dobás in babu_lista if dobás != '0')

    # Kiírjuk az eredményeket
    print(f"Az összes dobás száma: {osszes_dobas}")
    print(f"A helyes dobások száma: {helyes_dobasok}")
    print(f"A helytelen dobások száma: {helytelen_dobasok}")