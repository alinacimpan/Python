from Domain.cheltuieli import get_nr_ap


def sterge_pt_nr_ap(lst_cheltuieli, nr_ap, undo_list, redo_list):
    '''
    Functia returneaza lista care se obtine in urma stergerii tututor cheltuielilor pentru un apartament dat
    :param lst_cheltuieli: O lista de cheltuieli
    :param nr_ap: Un numar de apartament, introdus de utilizator
    :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :return: Lista nou obtinuta in urma stergerilor dorite
    '''
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_ap(cheltuiala) != nr_ap:
            new_lst_cheltuieli.append(cheltuiala)
    if len(new_lst_cheltuieli) == len(lst_cheltuieli):#inseamna ca nu am efectuat nici o stergere, deci nu exista cheltuieli cu acest numar de apartament
        raise ValueError('Nu exista nici o cheltuiala cu acest numar de apartament, deci nu avem ce sterge!')
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_lst_cheltuieli