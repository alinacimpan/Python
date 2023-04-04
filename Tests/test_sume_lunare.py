from Logic.sume_lunare import get_sume_lunare
from Tests.test_crud import get_info


def test_get_sume_lunare():
    lst_cheltuieli = get_info()
    result_sume = get_sume_lunare(lst_cheltuieli)
    result = {}
    result[10] = [250, 100, 175]
    result[7] = [323]
    result[12] = [123.3, 275]
    assert len(result) == len(result_sume)
    assert result_sume == result
    result[11] = [233]
    assert (result_sume == result) == False
