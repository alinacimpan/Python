from Domain.cheltuieli import get_data, get_suma

def get_sume_lunare(lst_cheltuieli):
    '''
    Functia retunreaza un dictionar, cu cheia o luna ce se regaseste in data unei cel putin o chetuiala din lista iar valoarea
    o lista de sume ce apartin cheltuielilor ce sunt trecuta pe aceasta luna
    :param lst_cheltuieli:O lista de cheltuieli
    :return: Un dictionar cu cheia "luna" si valoarea o lista de int
    '''
    result = {}
    for cheltuiala in lst_cheltuieli:
        data = get_data(cheltuiala)
        luna = int(data.split('.')[1]) # luam luna din data
        if luna not in result: #avem o luna noua
            result[luna] = []
            result[luna].append(get_suma(cheltuiala))
        else:
            result[luna].append(get_suma(cheltuiala))
    return result