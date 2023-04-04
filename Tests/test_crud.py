from Domain.cheltuieli import creeaza_cheltuiala, get_id
from Logic.crud import adaugare, stergere, modif, doar_cifre
from Logic.crud import read

def get_info():
    return [
        creeaza_cheltuiala(1, 1, 250, '12.10.2002', 'intretinere'),#Primul e ID-ul, al DOILEA e Numarul Apartamentului!
        creeaza_cheltuiala(2, 2, 100, '12.10.2002', 'intretinere'),
        creeaza_cheltuiala(3, 3, 175, '12.10.2002', 'alte cheltuieli'),
        creeaza_cheltuiala(4, 4, 323.0, '07.07.2020', 'canal'),
        creeaza_cheltuiala(5, 5, 123.3, '08.12.2010', 'alte cheltuieli'),
        creeaza_cheltuiala(6, 3, 275, '08.12.2010', 'alte cheltuieli')
        ]
def test_doar_cifre():
    assert doar_cifre('abc') == False
    assert doar_cifre('12a') == False
    assert doar_cifre('123') == True

def test_adaugare():
    lst_cheltuieli = get_info()
    params = (7, 6, 222, '12.10.2002', 'canal', [], [])
    new_cheltuiala = creeaza_cheltuiala(*params[:-2])
    new_lst_cheltuieli = adaugare(lst_cheltuieli, *params)
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli) + 1
    assert new_cheltuiala not in lst_cheltuieli
    assert new_cheltuiala in new_lst_cheltuieli
    params2 = (6, 10, 1, '11.11.2002', 'canal', [], [])
    try:
        lista_noua = adaugare(new_lst_cheltuieli, *params2)
        assert False
    except ValueError:
        assert True #Se prinde intr adevar o eroare; Daca pui "assert False", vei vedea ca nu iti merge, fiindca EXISTA o eroare care trebuie prinsa
    params3 = (7, 11, 1, '11.13.2001', 'intretinere', [], [])
    try:
        lista_noua = adaugare(lst_cheltuieli, *params3)
        assert True
    except ValueError:
        assert True

def test_read():
    lst_cheltuieli = get_info()
    nr_apartament = lst_cheltuieli[2] # sau direct nr_apartament = 3, a 3 a cheltuiala din lista(care, evident, se afla in lista)
    caut_cheltuiala = read(lst_cheltuieli, get_id(nr_apartament))
    assert caut_cheltuiala in lst_cheltuieli
    assert read(lst_cheltuieli, None) == lst_cheltuieli
    assert read(lst_cheltuieli, 11) is None

def test_modif():
    lst_cheltuieli = get_info()
    schimbat_cheltuiala = (3, 3, 375, '12.10.2002', 'intretinere')
    new_cheltuiala = creeaza_cheltuiala(*schimbat_cheltuiala)
    new_lst_cheltuieli = modif(lst_cheltuieli, new_cheltuiala, [], [])
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli)#evident, am modificat o cheltuiala, deci au aceeasi lungime
    assert new_cheltuiala not in lst_cheltuieli
    assert new_cheltuiala in new_lst_cheltuieli
    try:
        params2 = (13, 3, 375, '12.10.2002', 'intretinere')
        cheltuiala_noua = creeaza_cheltuiala(*params2)
        lst_cheltuieli = modif(lst_cheltuieli, cheltuiala_noua, [], [])
        assert False
    except ValueError:
        assert True

def test_stergere():
    lst_cheltuieli = get_info()
    id_ap = 3
    new_lst_cheltuiala = stergere(lst_cheltuieli, id_ap, [], [])
    assert len(new_lst_cheltuiala) == len(lst_cheltuieli)- 1
    aparitie_cheltuiala = read(lst_cheltuieli, id_ap)
    assert aparitie_cheltuiala not in new_lst_cheltuiala
    assert aparitie_cheltuiala in lst_cheltuieli
    try:
        lst_cheltuieli = stergere(lst_cheltuieli, 11, [], [])
        assert False
    except ValueError:#se prinde eroarea
        assert True

def test_crud():
    test_doar_cifre()
    test_modif()
    test_read()
    test_adaugare()
    test_stergere()

