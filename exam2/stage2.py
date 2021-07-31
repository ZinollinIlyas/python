from random import randint

dragon = {
    'hp': 2000,
    'defence': 120,
    'str': 150,
    'weapon': 0
}

hero = {
    'hp': 1000,
    'defence': 100,
    'str': 120,
    'weapon': 350,
    'shield': 150
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


def hero_turn():
    hero_move = randint(0, 100)
    if hero_move <= 75:
        hero_damage = hero['str'] + hero['weapon'] - dragon['defence']
        modify_health(dragon, -hero_damage)
        print(f"Герой нанес {hero_damage} урона")
    else:
        print("Герой промазал")
    display_dragon_info()


def dragon_turn():
    dragon_move = randint(0, 100)
    if dragon_move <= 50:
        dragon_damage = dragon['str'] + dragon['weapon'] - hero['defence']
        modify_health(hero, -dragon_damage)
        print(f"Дракон нанес {dragon_damage} урона")
    else:
        print("Дракон проспал свой ход")
    display_hero_info()


while True:
    hero_turn()
    if is_alive(dragon):
        dragon_turn()
    else:
        print("Дракон мертв")
        break
    if not is_alive(hero):
        print("Герой мертв")
        break
