from Domain.cheltuieli import get_tipul, get_suma


def find_out_biggest_cheltuiala_for_tip(lst_cheltuieli):
    '''
    Functia returneaza cheltuiala ce are cea mai mare suma pentru fiecare tip de cheltuiala
    :param lst_cheltuieli:O lista de cheltuieli
    :return:Un dictionar, unde cheia este "tipul cheltuielii" iar valoarea este "cheltuiala"(elementul listei)
    '''
    result = {}  # un dictionar cu cheia:tipul cheltuielii, si valoarea:cheltuiala(elementul din lista)
    for cheltuiala in lst_cheltuieli:
        tip = get_tipul(cheltuiala)
        cost = get_suma(cheltuiala)
        if tip not in result:  # prima cheltuiala ce acest tip
            result[tip] = cheltuiala
        else:
            if cost > get_suma(result[tip]):
                result[tip] = cheltuiala
    return result