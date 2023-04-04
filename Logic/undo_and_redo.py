def do_undo(undo_list, redo_list, current_list):
    '''
    Functia ne da lista inaintea apelarii uneia din cele 6 functionalitati, cea de dinaintea
    schimbarii(asta pentru functionalitatile care returneaza o lista, pentru cele care se poate apela Undo)
    :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :param current_list: Lista curenta de cheltuieli
    :return: Lista noua in urma apelarii Undo ului
    '''
    if undo_list: #Avem din ce face undo, mai avem elemente in lista
        top_undo = undo_list.pop()
        #AICI SI undo_list SE MODIFICA, top_undo FIIND UN POINTER LA undo_list(fara ultimul element); pop are efect si asupra lui undo_list
        #top_undo si undo_list sunt una si aceeasi lista, nu sunt diferite; nu am folosit DEEPCOPY pentru a le face diferite
        redo_list.append(current_list)
        return top_undo
    return None

def do_redo(undo_list, redo_list, current_list):
    '''
    Functie ce ne da lista de cheltuieli ce trebuia sa o avem inaintea apelarii Undo ului
    (Redo ul se poate apela doar imediat dupa ce am apelat cel putin o data un Undo)
    :param undo_list: Lista de liste de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, ce se modifica in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :param current_list: Lista curenta de cheltuieli
    :return: Lista noua ce se obtine in urma apelarii Redo ului
    '''
    if redo_list: #Avem Redo imediat dupa un Undo
        top_redo = redo_list.pop()
        # AICI SI redo_list SE MODIFICA, top_redo FIIND UN POINTER LA redo_list(fara ultimul element); pop are efect si asupra lui redo_list
        # top_redo si redo_list sunt una si aceeasi lista, nu sunt diferite; nu am folosit DEEPCOPY pentru a le face diferite
        undo_list.append(current_list)
        return top_redo
    return None