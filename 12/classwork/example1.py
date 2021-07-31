class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        self.initials = f"{first_name.capitalize()[0]}.{last_name.capitalize()[0]}"

