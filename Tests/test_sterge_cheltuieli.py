from Logic.sterge_cheltuieli import sterge_pt_nr_ap
from Logic.crud import read
from Tests.test_crud import get_info


def test_Stergere_cheltuieli():
    lst_cheltuieli = get_info()
    nr_ap = 3
    new_lst_cheltuieli = sterge_pt_nr_ap(lst_cheltuieli, nr_ap, [], [])
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli) - 2
    assert read(lst_cheltuieli, 3) is not None
    assert read(new_lst_cheltuieli, 3) is None # am sters prajitura de id 3, cu nr_ap 3
    alt_nr_ap = 12
    try:
        lista_noua_cheltuieli = sterge_pt_nr_ap(lst_cheltuieli, alt_nr_ap, [], [])
        assert False
    except ValueError:
        assert True