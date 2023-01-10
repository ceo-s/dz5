"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. баланс

4. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

5. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json

def open_data(func):
    def wrapper():
        with open("data.json", "r") as file:
            a = func(file)
        return a
    return wrapper

@open_data
def get_json(file):
    json_r = json.loads(file.read())
    return json_r

print(get_json())

def write_data(func):
    def wrapper(sum, clas):
        with open("data.json", "w") as file:
            file.write(json.dumps(func(sum, clas)))
    return wrapper

"""with open("data.json", "w") as file:
            file.write(json.dumps({'wallet': 6, 'history': []}))"""


class Person:
    goods = ["1. Вода", "2. Квас", "3. Молоко", "4. Лимонад", "5. Чай", "6. Кофе"]
    prices = [10, 15, 15, 12, 20, 20]




def balance_add(sum):
    json1 = get_json()
    json1['wallet'] += int(sum)
    with open("data.json", "w") as file:
            file.write(json.dumps(json1))

def market(clas):    
    for good in clas.goods:
        print(good, clas.prices[clas.goods.index(good)])

def buy(number, clas):
    chosen_price = clas.prices[int(number)-1]
    json1 = get_json()
    if chosen_price <= json1['wallet']:
        json1['wallet'] -= chosen_price
        json1['history'] += [clas.goods[int(number)-1]]
        with open("data.json", "w") as file:
            file.write(json.dumps(json1))
        print(f"Вы купили {clas.goods[int(number)-1]}")
    else:
        print("\nНедостаточно средств!")

def get_history():
    if get_json()['history'] == []:
        print("Вы ещё ничего не купили!")
    else:
        print("-"*20,"\nИстория покупок: ")
        [print(i) for i in get_json()['history']]
        print("-"*20)
    

def check_balance():
    print(f"\nВаш баланс = {get_json()['wallet']}")


while True:
    print("  Главное меню!")
    print('|1. пополнение счета')
    print('|2. покупка')
    print('|3. баланс')
    print('|4. история покупок')
    print('|5. выход')

    choice = input('\nВыберите пункт меню: ')
    if choice == '1':
        balance_add(input("\nВведдите сумму пополнения: "))
    elif choice == '2':
        market(Person)
        buy(input("\nВведите номер товара: "), Person)
    elif choice == '3':
        check_balance()
    elif choice == '4':
        get_history()
    elif choice == '5':
        break
    else:
        print('\nНеверный пункт меню!')