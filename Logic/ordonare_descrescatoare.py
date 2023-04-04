from Domain.cheltuieli import get_suma


def ordonare(lista, undo_list, redo_list):
     '''
     Functia returneaza o lista de cheltuieli ordonate descrescator in functie de sumele acestora
     :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
     :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
     :param lista: O lista de cheltuieli
     :return: Lista ordonata descrescator, "cheia" find sumelele cheltuielilor
     '''
     undo_list.append(lista)
     redo_list.clear()
     return sorted(lista, key = get_suma, reverse  = True)