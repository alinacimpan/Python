from Domain.cheltuieli import get_suma, get_id
from Logic.adunarea_unei_valori import adunare_valoare_for_data
from Logic.ordonare_descrescatoare import ordonare
from Logic.sterge_cheltuieli import sterge_pt_nr_ap
from Logic.undo_and_redo import do_undo, do_redo
from Logic.crud import adaugare, read
from Tests.test_crud import get_info


def test_undo_and_redo():
    undo_list = []
    redo_list = []
    lista = []
    lista = adaugare(lista, 1, 1, 250, '12.10.2002', 'intretinere', undo_list, redo_list)
    lista = adaugare(lista, 2, 2, 100, '12.10.2002', 'intretinere', undo_list, redo_list)
    lista = adaugare(lista, 3, 3, 175, '12.10.2002', 'alte cheltuieli', undo_list, redo_list)
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [2, 2, 100, '12.10.2002', 'intretinere']
    assert read(lista, 3) is None
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert read(lista, 2) is None
    assert read(lista, 3) is None
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert read(lista, 1) is None
    assert read(lista, 2) is None
    assert read(lista, 3) is None
    if len(undo_list) > 0:  #tot nimic nu face
        lista = do_undo(undo_list, redo_list, lista)
    assert read(lista, 1) is None
    assert read(lista, 2) is None
    assert read(lista, 3) is None
    lista = adaugare(lista, 1, 1, 250, '12.10.2002', 'intretinere', undo_list, redo_list)
    lista = adaugare(lista, 2, 2, 100, '12.10.2002', 'intretinere', undo_list, redo_list)
    lista = adaugare(lista, 3, 3, 175, '12.10.2002', 'alte cheltuieli', undo_list, redo_list)
    if len(redo_list) > 0:  #avem Redo dupa un Undo
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [2, 2, 100, '12.10.2002', 'intretinere']
    assert lista[2] == [3, 3, 175, '12.10.2002', 'alte cheltuieli']
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [2, 2, 100, '12.10.2002', 'intretinere']
    assert read(lista, 3) is None
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert read(lista, 2) is None
    assert read(lista, 3) is None
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [2, 2, 100, '12.10.2002', 'intretinere']
    assert read(lista, 3) is None
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [2, 2, 100, '12.10.2002', 'intretinere']
    assert lista[2] == [3, 3, 175, '12.10.2002', 'alte cheltuieli']
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [2, 2, 100, '12.10.2002', 'intretinere']
    assert read(lista, 3) is None
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert read(lista, 2) is None
    assert read(lista, 3) is None
    lista = adaugare(lista, 4, 4, 323.0, '07.07.2020', 'canal', undo_list, redo_list)
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [4, 4, 323.0, '07.07.2020', 'canal']
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert read(lista, 4) is None
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert read(lista, 1) is None
    assert read(lista, 4) is None
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert read(lista, 4) is None
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [4, 4, 323.0, '07.07.2020', 'canal']
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']
    assert lista[1] == [4, 4, 323.0, '07.07.2020', 'canal']

def test_Delete_for_nr_ap_undo_si_redo():
    undo_list = []
    redo_list = []
    lista = get_info()
    lista = sterge_pt_nr_ap(lista, 1, undo_list, redo_list)
    assert read(lista, 1) is None
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert lista[0] == [1, 1, 250, '12.10.2002', 'intretinere']  #a pus cheltuiala inapoi, a devenit lista initiala
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert read(lista, 1) is None


def test_add_for_data_undo_si_redo():
    lista = get_info()
    undo_list = []
    redo_list = []
    assert get_suma(lista[0]) == 250
    assert get_suma(lista[1]) == 100
    lista = adunare_valoare_for_data(lista, '12.10.2002', 10000, undo_list, redo_list)
    assert get_suma(lista[0]) == 10250
    assert get_suma(lista[1]) == 10100
    if len(undo_list) > 0:
        lista = do_undo(undo_list, redo_list, lista)
    assert get_suma(lista[0]) == 250
    assert get_suma(lista[1]) == 100
    if len(redo_list) > 0:
        lista = do_redo(undo_list, redo_list, lista)
    assert get_suma(lista[0]) == 10250

def test_ordonare_undo_and_redo():
    lista = get_info()
    undo_list = []
    redo_list = []
    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    new_lista =  ordonare(lista, undo_list, redo_list)
    assert get_id(new_lista[0]) == 4
    assert get_id(new_lista[1]) == 6
    if len(undo_list) > 0:
        new_lista = do_undo(undo_list, redo_list, new_lista)
    assert get_id(new_lista[0]) == 1
    assert get_id(new_lista[1]) == 2
    if len(redo_list) > 0:
        new_lista = do_redo(undo_list, redo_list, new_lista)
    assert get_id(new_lista[0]) == 4
    assert get_id(new_lista[1]) == 6



def Teste_For_All_Undo_And_Redo():
    test_undo_and_redo()
    test_Delete_for_nr_ap_undo_si_redo()
    test_add_for_data_undo_si_redo()
    test_ordonare_undo_and_redo()



