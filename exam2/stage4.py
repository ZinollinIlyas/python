from random import randint

dragon = {
    'hp': 2000,
    'defence': 120,
    'str': 500,
    'weapon': 0
}

hero = {
    'hp': 1000,
    'defence': 100,
    'str': 120,
    'weapon': 350,
    'shield': 100,
    'potion_quantity': 1,
    'has_shield': False
}


def display_dragon_info():
    print(f"Здоровье дракона: {dragon['hp']}hp")
    print("=" * 100)


def display_hero_info():
    print(f"Здоровье героя: {hero['hp']}hp")
    print("=" * 100)


def modify_health(character, dmg):
    character['hp'] += dmg
    if character['hp'] < 0:
        character['hp'] = 0


def is_alive(character):
    if character['hp'] <= 0:
        return False
    else:
        return True


def attack():
    remove_shield()
    hero_move = randint(0, 100)
    if hero_move <= 75:
        hero_damage = hero['str'] + hero['weapon'] - dragon['defence']
        if hero_damage <= 0:
            hero_damage = 0
        modify_health(dragon, -hero_damage)
        print(f"Герой нанес {hero_damage} урона")
    else:
        print("Герой промазал")


def pass_turn():
    print("Герой пропустил ход")
    print("=" * 100)


def equip_shield():
    if not hero['has_shield']:
        hero['has_shield'] = True
        hero['defence'] += hero['shield']


def remove_shield():
    if hero['has_shield']:
        hero['has_shield'] = False
        hero['defence'] -= hero['shield']


def defend():
    equip_shield()
    print("Герой защищается")
    print("=" * 100)


def hit_with_dragonball():
    dragonball_damage = dragon['str'] * 2
    if not hero['has_shield']:
        modify_health(hero, -dragonball_damage)
        print("Дракон плюется огненным шаром")
    else:
        print("Герой отразил огненный шар щитом")
        print('=' * 100)


def drink_potion():
    potion_health = 500
    if hero['potion_quantity'] > 0:
        modify_health(hero, potion_health)
        hero['potion_quantity'] -= 1
        print("Герой принял зелье")
    else:
        print("Зелья кончились\nПропуск хода")
        print("=" * 100)


def hero_turn():
    print("Что будет делать герой?\nattack - атаковать\ndefence - защищаться\ndrink potion - выпить зелье"
          "\npass - пропустит ход")
    choice = input()
    if choice == 'attack':
        attack()
        display_dragon_info()
    elif choice == 'defence':
        defend()
    elif choice == 'pass' or choice == '':
        pass_turn()
    elif choice == 'drink potion':
        drink_potion()
    else:
        print("Такой команды не существует")


def dragon_turn():
    dragon_move = randint(0, 100)
    if dragon_move <= 50:
        dragonball = randint(0, 100)
        if dragonball <= 50:
            hit_with_dragonball()
        elif dragonball >= 51:
            dragon_damage = dragon['str'] + dragon['weapon'] - hero['defence']
            if dragon_damage <= 0:
                dragon_damage = 0
            modify_health(hero, -dragon_damage)
            print(f"Дракон нанес {dragon_damage} урона")
    else:
        print("Дракон проспал свой ход")

    display_hero_info()


while True:
    hero_turn()
    if is_alive(dragon):
        dragon_turn()
        remove_shield()
    else:
        print("Герой побеждает")
        break
    if not is_alive(hero):
        print("Дракон побеждает")
        break
