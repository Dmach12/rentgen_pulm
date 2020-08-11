# Обширное затемнение (extensive_darkening) - затемнение всего легочного
# поля или большей его части(не менее 2/3). Прозрачной может остаться
# лишь область верхушки или основания легкого
shift_mediastinum = int(input('Органы средостения смещены'
                                  ' - поставьте 1, '
                                  'если не смещены поставьте 0: '))
# extensive_darkening = int(input('Enter 1, если есть обширное затемнение -'
#                                 'extensive_darkening,'
#                               ' 0 - если нет: '))
shadow_shape = 0  # форма тени
intensity_shadow = 0  # интенсивность тени
structure_shadow = 0  # структура тени
other_lung = 0


dark_entir_half = 0

if shift_mediastinum == 0:
    print('Имеется внутри- или внелегочное поражение')
    extensive_darkening = int(input('Enter 1, если есть обширное затемнение -'
                                    'extensive_darkening,'
                                    ' 0 - если нет: '))
    if extensive_darkening == 0:
        print('Не тотальное затемнение')
    if extensive_darkening == 1:
        dark_entir_half = int(input('Enter 1, если есть затемнение всей половины грудной клетки, '
                                    '0 - если тень меньше половины грудной клетки с косым верхним краем: '))
        if dark_entir_half == 1:   # Затемнена вся половина грудной клетки
            print('Поражение легкого или уплотнение плевры')
            intensity_shadow = int(input('Enter 1, если интенсивность тени большая, 0 - если интенсивность малая или средняя'))
            if intensity_shadow == 1:
                print('Острое воспаление легкого')
                shadow_shape = int(input('Enter 1, 0 - если тень однородна'))
                if structure_shadow == 1:
                    print('В зоне инфильтрации некроз и распад')
                    other_lung = int(input('Enter 1 если очаговые, и(или) другие тени, 0 если ограниченные и(или) кольцевидные тени, пневмоторакс'))
                    if other_lung == 1:
                        print('Острая туберкулезная творожистая пневмония')
                    if other_lung == 0:
                        print('Острая стафилококковая пневмония')

                if structure_shadow == 0:
                    print('Распада и полостей нет')
            if intensity_shadow == 0:
                    print('Уплотнение плевры')

        if dark_entir_half == 0: #Тень меньше половины грудной клетки с
            # косым верхним краем
            print('Выпотной плеврит')

