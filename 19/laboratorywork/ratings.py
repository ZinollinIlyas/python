import json
import os


class Movie:
    def __init__(self, name, ratings=None):
        if ratings is None:
            ratings = {}
        self.name = name
        print(ratings)
        self.ratings = Rating(name=ratings.keys(), rating_value=ratings.values())

    def calculate_avg(self):
        count = 0
        for rating in self.ratings.rating_value:
            count += rating
        avg = count / len(self.ratings.rating_value)
        return avg

    def get_table(self):
        name_list = []
        rating_list = []
        connected_list = []
        for key in list(self.ratings.name):
            name_list.append(key)
        for value in list(self.ratings.rating_value):
            rating_list.append(value)
        for name, rating in zip(name_list, rating_list):
            connected_list.append(f"{name} : {rating}")
        return connected_list

    def display(self):
        print(f"{'Name':<35}{'Rating':}{'Average rating':>40}")
        print(f"{self.name:<35}{', '.join(self.get_table())}{self.calculate_avg():>20}")

    def get_dict(self):
        movie = self.__dict__
        print(movie)
        return movie

    def rate(self, name, value):
        if value == 0:
            self.ratings.rating_value = ''
        elif value < 0 or value > 10:
            print("Rating value must be between 0 and 10")
        elif type(value) != int:
            print("Rating must be integer in range 0 to 10")
        elif name.isdigit():
            print("Name must not contain digits")
        else:
            self.ratings.name = name
            self.ratings.rating_value = value

    def __str__(self):
        return f"{self.name:<35}{self.calculate_avg()}"


class Rating:
    def __init__(self, name, rating_value):
        self.name = name
        self.rating_value = rating_value

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.name} - {self.rating_value}"


class MovieList:
    movie_list = []
    FILE_PATH = "films.json"

    def __init__(self):
        self.read_file()

    def update_file(self):
        with open(self.FILE_PATH, "w") as f:
            f.write(json.dumps(self.movie_list, default=lambda movie_obj: movie_obj.__dict__))

    def read_file(self):
        if os.path.isfile(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                data = f.read().strip()

                def get_object(d):
                    if "name" in d:
                        return Movie(d["name"], d["ratings"])
                    return d

                if data:
                    self.movie_list = json.loads(data, object_hook=get_object)
        else:
            with open(self.FILE_PATH, "w"):
                pass

    def search(self, name):
        for movie in self.movie_list:
            if movie.name == name:
                return movie

    def list(self):
        for movie in self.movie_list:
            print(f"{movie}")

    def find(self, name):
        movie = self.search(name)
        if movie:
            movie.display()

    def display(self):
        for movie in self.movie_list:
            movie.display()

    def add(self, name):
        movie = self.search(name)
        if movie:
            print("Movie already exists")
        else:
            new_movie = Movie(name, {})
            self.movie_list.append(new_movie)
            self.update_file()

    def rate(self, name, username, rating_value):
        movie = self.search(name)
        if movie:
            movie.rate(username, rating_value)


class Application:
    def print_menu(self):
        print("Movie List")
        print("Enter a command:")
        print(
            "list",
            "find",
            "exit",
            sep="\n"
        )

    def enter_name(self):
        name = input("Enter a name\n>> ")
        return name

    def enter_rating(self):
        rating = input("Enter a rating\n>> ")
        return

    def run(self):
        movie_list = MovieList()
        while True:
            self.print_menu()
            command = input(">> ")
            if command == "list":
                movie_list.list()
            elif command == "find":
                name = self.enter_name()
                movie_list.find(name)
            elif command == "exit":
                exit(0)
            else:
                print("This command does not exist")


movie = MovieList()
movie.list()
# movie.add("fast")
