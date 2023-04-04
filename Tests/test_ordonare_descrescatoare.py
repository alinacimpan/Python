from Domain.cheltuieli import get_suma
from Logic.ordonare_descrescatoare import ordonare
from Tests.test_crud import get_info


def test_ordonare():
    lista_cheltuieli = get_info()
    new_lista_cheltuieli = ordonare(lista_cheltuieli, [], [])
    assert len(new_lista_cheltuieli) == len(lista_cheltuieli)
    assert get_suma(new_lista_cheltuieli[0]) == 323 #cea mai mare suma
    assert get_suma(new_lista_cheltuieli[5]) == 100 #cea mai mica suma
    assert new_lista_cheltuieli[0] == lista_cheltuieli[3]