from Logic.crud import adaugare
from Tests.test_adunarea_unei_valori import test_adunare_valoare_pt_data
from Tests.test_sume_lunare import test_get_sume_lunare
from Tests.test_crud import test_crud
from Tests.test_ordonare_descrescatoare import test_ordonare
from Tests.test_sterge_cheltuieli import test_Stergere_cheltuieli
from Tests.test_undo_and_redo import  Teste_For_All_Undo_And_Redo
from Tests.test_cea_mai_mare_cheltuiala import test_find_out_biggest_cheltuiala_for_tip
from User_interface.coomand_line_console import run_in_line_console
from User_interface.console import run_ui

def meniuri():
    print('1.Meniul vechi')
    print('2.Meniul nou')
    print('x.Exit')

def main():
    lst_cheltuieli = []
    tip_cheltuiala = ['intreținere', 'canal', 'alte cheltuieli']
    undo_list = []
    redo_list = []
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 3, 234.5, '28.11.2004', 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 1, 300, '27.11.2004', 'canal', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 3, 2, 234.5, '27.11.2004', 'intretinere', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 4, 4, 400, '27.11.2004', 'intretinere', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 5, 1, 560, '27.11.2004', 'canal', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 6, 5, 700, '30.08.2004', 'canal', undo_list, redo_list)
    while True:
        meniuri()
        optiune = input('Alegeti interfata: ')
        if optiune == '1':
            run_ui(lst_cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            run_in_line_console(lst_cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    test_crud()
    test_Stergere_cheltuieli()
    test_adunare_valoare_pt_data()
    test_find_out_biggest_cheltuiala_for_tip()
    test_ordonare()
    Teste_For_All_Undo_And_Redo()
    main()