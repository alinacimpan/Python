def creeaza_cheltuiala(id:int, nr_apartament: int, suma: float, data: str, tipul: str):
    '''
    Creeaza o cheltuiala in care sa fie specificata nr_apartament, suma, data(in format string: 'DD.MM.YYYY') si tipul
    care poate fi:cheltuiala, intretinere sau alte cheltuieli
    :param nr_apartament:Numarul apartaentului
    :param suma:Suma cheltuielii
    :param data:Data in care se face cheltuiala
    :param tipul:Tipul cheltuielii(va fi precizat, in format string)
    :return: Creeaza cheltuiala cu datele introduse
    '''
    return [id, nr_apartament, suma, data, tipul]

def get_id(cheltuiala):
    '''
    Returneaza id ul cheltuielii
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Id ul cheltuielii
    '''
    return cheltuiala[0]

def get_nr_ap(cheltuiala):
    '''
    Returneaza nr_ap al cheltuielii
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Nr apartamentului in care e trecut cheltuiala
    '''
    return cheltuiala[1]

def get_suma(cheltuiala):
    '''
    Returneaza suma cheltuielii
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Suma acesteia
    '''
    return cheltuiala[2]

def get_data(cheltuiala):
    '''
    Returneaza data cheltuielii
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Data acesteia
    '''
    return cheltuiala[3]

def get_tipul(cheltuiala):
    '''
    Returneaza tipul cheltuielii(cum este)
    :param cheltuiala: O cheltuiala introdusa de utilizator
    :return: Tipul acesteia
    '''
    return cheltuiala[4]

def get_str(cheltuiala):
    return f'Id ul cheltuielii este {get_id(cheltuiala)}, cu Nr_apartamentului {get_nr_ap(cheltuiala)}, suma {get_suma(cheltuiala)}, data {get_data(cheltuiala)} si tipul {get_tipul(cheltuiala)}'