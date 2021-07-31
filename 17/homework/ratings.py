import json


def save_films():
    with open("films.json", "w") as f:
        f.write(json.dumps(movies))


def load_films():
    with open("films.json", "r") as f:
        deserealized_films = json.loads(f.read())
        return deserealized_films


movies = load_films()


def notify():
    print("Film does not exists")


def search(name):
    for film in movies:
        if name == film['name']:
            return film



def get_list():
    movies.sort(key=lambda movie: movie['name'])
    print(f"{'Name'.center(30)} {'Rating'.center(30)}")
    for film in movies:
        if len(film['ratings']) == 0:
            print(f"{film['name'].center(30)} {'No rating'.center(30)}")
        else:
            avg = sum(film['ratings'].values()) / len(film['ratings'])
            if avg.is_integer():
                print(f"{film['name'].center(30)} {str(round(avg)).center(30)}")
            else:
                print(f"{film['name'].center(30)} {str(avg).center(30)}")


def get_films_sorted_by_rating():
    print(f"{'Name'.center(30)} {'Rating'.center(30)}")
    for film in movies:
        avg = sum(film['ratings'].values()) / len(film['ratings'])
        avg_list = []
        avg_list.append(avg)
        avg_list.sort()
        if len(film['ratings']) == 0:
            print(f"{film['name'].center(30)} {'No rating'.center(30)}")
        else:
            for value in avg_list:
                if value.is_integer():
                    print(f"{film['name'].center(30)} {str(round(avg)).center(30)}")
                else:
                    print(f"{film['name'].center(30)} {str(avg).center(30)}")


def add(name):
    film = search(name)
    if film in movies:
        print("This film already exists")
    else:
        movies.append({'name': name, 'ratings': {}})
        save_films()


def delete(name):
    film = search(name)
    if film in movies:
        movies.remove(film)
        save_films()
    else:
        notify()


def rate(name):
    film = search(name)
    if film in movies:
        ratings = film['ratings']
        print("Enter your name and your rate to this film")
        username = input()
        rating = int(input())
        if rating == 0:
            del ratings[username]
            save_films()
        elif rating < 0 or rating > 10:
            print("Rating value must be between 0 and 10")
        else:
            ratings.update({username: rating})
            save_films()
    else:
        notify()


def find(name):
    film = search(name)
    if film not in movies:
        notify()
    else:
        ratings = film['ratings']
        print("Name:")
        print(film['name'])
        print("Ratings:")
        for item in ratings:
            print(f"{item}'s rating is : {ratings[item]}")
        print("Average rating:")
        avg = sum(ratings.values()) / len(ratings)
        if avg.is_integer():
            print(round(avg))
        else:
            print(avg)


while True:
    print("Enter the command you want to execute:\nlist\nfind\nadd\ndelete\nrate\navg rating\nTo quit enter: exit")
    command = input()
    if command == "list":
        get_list()
    elif command == "find":
        print("Enter name of film you want to find")
        film_name = input().capitalize()
        find(film_name)
    elif command == "add":
        print("Enter name of film you want to add")
        film_name = input().capitalize()
        add(film_name)
    elif command == "delete":
        print("Enter name of film you want to delete")
        film_name = input().capitalize()
        delete(film_name)
    elif command == "rate":
        print("Enter name of film you want to rate")
        film_name = input().capitalize()
        rate(film_name)
    elif command == 'avg rating':
        get_films_sorted_by_rating()
    elif command == "exit":
        break
    else:
        print("There's no such command")
