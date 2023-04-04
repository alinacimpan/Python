from Logic.adunarea_unei_valori import adunare_valoare_for_data
from Tests.test_crud import get_info


def test_adunare_valoare_pt_data():
    lista_cheltuieli = get_info()
    data = '12.10.2002'
    val = 100
    new_lista_cheltuieli = adunare_valoare_for_data(lista_cheltuieli, data, val, [], [])
    assert len(new_lista_cheltuieli) == len(lista_cheltuieli)
    try:
        alta_data = '01.01.10000' # data e gresita
        new_lista_cheltuieli = adunare_valoare_for_data(new_lista_cheltuieli, alta_data, val, [], [])
        assert False
    except ValueError:
        assert True
    try:
        alta_data = '01.01.1010' #nu exista cheltuiala cu o asemenea data
        new_lista_cheltuieli = adunare_valoare_for_data(new_lista_cheltuieli, alta_data, val, [], [])
        assert False
    except ValueError:
        assert True
