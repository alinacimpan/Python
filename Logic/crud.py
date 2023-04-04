from Domain.cheltuieli import creeaza_cheltuiala, get_id, get_data, get_tipul


def doar_cifre(sir):
    '''
    Subprogramul determina daca intr un str avem doar cifre sau nu
    :param sir: Un string
    :return: True daca e format doar din cifre sau False in caz contrar
    '''
    lst_cifre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for litera in sir:
        if litera not in lst_cifre:
            return False#am gasit un caracter care nu e cifra
    return True

def format_data(data):
    '''
    Functia verifica daca un tip data de forma DD.MM.YYYY este introdus corect
    :param data: Un string de forma specificata
    :return: None daca string ul este in format corect
    '''
    data_split = data.split('.')
    if len(data_split) < 3:
        raise ValueError(f'Data cheltuieliii {data} introdusa nu este corecta ca si format')
    if len(data_split[0]) != 2 or len(data_split[1]) != 2 or len(data_split[2]) != 4:
        raise ValueError(f'Data cheltuieliii {data} introdusa nu este corecta ca si format')
    if doar_cifre(data_split[0]) == False or doar_cifre(data_split[1]) == False or doar_cifre(data_split[2]) == False:
        raise ValueError(f'Data cheltuielii {data} introdusa nu este corecta ca si format')
    zi = int(data_split[0])
    luna = int(data_split[1])
    if (luna % 2 == 0 and zi > 30) or (luna % 2 == 1 and zi > 31) or (luna == 2 and zi > 28):
        raise ValueError(f'Data cheltuielii  {data} introdusa nu este corecta ca si format')

def adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip, undo_list, redo_list) -> list:
    '''
    Subprogramul adauga in lista "cheltuieli" noua cheltuiele cu datele introduse de utilizator
    :param lst_cheltuieli: O lista de cheltuieli
    :param id: Id ul cheltuielii
    :param nr_ap: Nr. apartamentului noii cheltuieli
    :param suma: Suma noii cheltuieli
    :param data: Data noii cheltuieli
    :param tip: Tipul acesteia
    :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :return: O lista noua, obtinuta prin adaugarea noii cheltuielii
    '''
    if id < 0: #nu am introdus id de tip intreg
        raise ValueError(f'Id ul cheltuielii {id} introdus nu este corect ca si format')
    if read(lst_cheltuieli, id) is not None:
        raise ValueError(f'Exista deja o cheltuiala cu id ul {id}')
    if nr_ap < 0:
        raise ValueError(f'Nr_apartamentului cheltuielii {nr_ap} introdus nu este corect ca si format')
    format_data(data)#verificam daca data e introdusa corect
    if tip != 'canal' and tip != 'intretinere' and tip != 'alte cheltuieli':
        raise ValueError(f'Tipul cheltuielii {tip} nu se afla printre cele precizate')
    new_cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return lst_cheltuieli + [new_cheltuiala]

def stergere(lst_cheltuieli, id, undo_list, redo_list):
    '''
    Sterge din lista cheltuiala cu un id al cheltuielii dat
    :param lst_cheltuieli: O lista de cheltuieli
    :param id: Id ul unei cheltuieli dat
    :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :return: Lista obtinuta prin eliminarea cheltuielii anume
    '''
    if read(lst_cheltuieli, id) is None:#nu avem ce sterge, nu exista cheltuiala
        raise ValueError(f'Nu avem o cheltuiala cu id ul {id}, deci nu avem ce sterge')
    result_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id:
            result_cheltuieli.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return result_cheltuieli

def modif(lst_cheltuieli, new_cheltuiala, undo_list, redo_list):
    '''
    Functia modifica (inlocuieste) cheltuiala pentru un anumit id de nr de aprtament cu o alta
    :param lst_cheltuieli: O lista de cheltuieli
    :param new_cheltuiala: Noua cheltuiala pentru un numar de apartament stiut
    :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :return: Lista noua obtinuta prin inlocuire
    '''
    new_lst_cheltuiala = []
    if read(lst_cheltuieli, get_id(new_cheltuiala)) is None:
        raise ValueError(f'Nu putem modifica cheltuiala cu id ul {get_id(new_cheltuiala)} fiindca nu exista!')
    format_data(get_data(new_cheltuiala)) #verificam daca data este introdusa corect in "noua cheltuiala"
    tip = get_tipul(new_cheltuiala)
    if tip != 'canal' and tip != 'intretinere' and tip != 'alte cheltuieli':
        raise ValueError(f'Tipul cheltuielii {tip} nu se afla printre cele precizate')
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_lst_cheltuiala.append(cheltuiala)
        else:
            new_lst_cheltuiala.append(new_cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_lst_cheltuiala

def read(lst_cheltuieli, id_ap_cheltuiala = None):
    '''
    Functia verifica daca apare in lista de cheltuieli o anumita cheltuiala, cu id dat
    :param lst_cheltuieli:O lista de cheltueieli
    :param id_ap_cheltuiala:Numarul apartamentului a cheltuielii
    :return:Returneaza cheltuiala cautata (daca exista in lista)
            toata lista daca id_ap_cheltuiala = None
            None daca nu exista cheltuiala cautata
    '''
    if id_ap_cheltuiala is None:#nu s a introdus un id
        return lst_cheltuieli
    cheltuiala_cu_nr_ap = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_ap_cheltuiala: #am gasit cheltuiala
            cheltuiala_cu_nr_ap = cheltuiala
    if cheltuiala_cu_nr_ap:
        return cheltuiala_cu_nr_ap
    return None #nu am gasit cheltuiala