print("Что хотите заказать?")

order = input()

if order == 'шаурма':
    print("Какую положить начинку?")
    filling = input()
    if filling != 'мясо' and filling != 'курица':
        print("К сожалению такой начинки у нас нет")
    else:
        print("Сколько штук положить?")
        quantity = int(input())
        print("Нужно ли подогревать?")
        heating = input()
        if heating == 'да':
            heating = 'подогретый'
        else:
            heating = 'неподогретый'
        print("Что желаете попить?")
        drink = input()
        if drink != 'чай' and drink != 'кофе' and drink != 'кола' and drink != 'минералка' and drink != '':
            print("К сожалению у нас нет таких напитков")
        elif drink == '':
            drink = 'нет напитка'
        print(f"Вы заказали: {order}, начинка : {filling}, количество : {quantity}, температура : {heating}, напиток : {drink}")
elif order == 'самса':
    print("Какую положить начинку?")
    filling = input()
    if filling != 'мясо' and filling != 'курица' and filling != 'сыр':
        print("К сожалению такой начинки у нас нет")
    elif filling == 'сыр':
        print("К сожалению самса с сыром закончилась, но будет готова через 15 минут. Вы готовы подождать?")
        answer = input()
        if answer == 'да':
            print("Сколько штук положить?")
            quantity = int(input())
            print("Нужно ли подогревать?")
            heating = input()
            if heating == 'да':
                heating = 'подогретый'
            else:
                heating = 'неподогретый'
            print("Что желаете попить?")
            drink = input()
            if drink != 'чай' and drink != 'кофе' and drink != 'кола' and drink != 'минералка' and drink != '':
                print("К сожалению у нас нет таких напитков")
            elif drink == '':
                drink = 'нет напитка'
            print(f"Вы заказали: {order}, начинка : {filling}, количество : {quantity}, температура : {heating}, напиток : {drink}")
    else:
        print("Сколько штук положить?")
        quantity = int(input())
        print("Нужно ли подогревать?")
        heating = input()
        if heating == 'да':
            heating = 'подогретый'
        else:
            heating = 'неподогретый'
        print("Что желаете попить?")
        drink = input()
        if drink != 'чай' and drink != 'кофе' and drink != 'кола' and drink != 'минералка' and drink != '':
            print("К сожалению у нас нет таких напитков")
        elif drink == '':
            drink = 'нет напитка'
        print(f"Вы заказали: {order}, начинка : {filling}, количество : {quantity}, температура : {heating}, напиток : {drink}")
elif order == 'пирожки':
    print("Какую положить начинку?")
    filling = input()
    if filling != 'картошка' and filling != 'капуста':
        print("К сожалению такой начинки у нас нет")
    else:
        print("Сколько штук положить?")
        quantity = int(input())
        print("Нужно ли подогревать?")
        heating = input()
        if heating == 'да':
            heating = 'подогретый'
        else:
            heating = 'неподогретый'
        print("Что желаете попить?")
        drink = input()
        if drink != 'чай' and drink != 'кофе' and drink != 'кола' and drink != 'минералка' and drink != '':
            print("К сожалению у нас нет таких напитков")
        elif drink == '':
            drink = 'нет напитка'
        print(f"Вы заказали: {order}, начинка : {filling}, количество : {quantity}, температура : {heating}, напиток : {drink}")
else:
    print("К сожалению такого блюда у нас нет")
