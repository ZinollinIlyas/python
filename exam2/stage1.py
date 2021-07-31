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


def modify_health(character, dmg):
    character['hp'] += dmg
    if character['hp'] < 0:
        character['hp'] = 0


def hero_turn():
    hero_move = randint(0, 100)
    if hero_move <= 75:
        damage = hero['str'] + hero['weapon'] - dragon['defence']
        modify_health(dragon, -damage)
        print(f"Герой нанес {damage} урона")
    else:
        print("Герой промазал")
    display_dragon_info()


while True:
    hero_turn()
    if dragon['hp'] <= 0:
        print("Дракон мертв")
        break
