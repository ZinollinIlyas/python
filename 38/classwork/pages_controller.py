from controller import Controller


class PagesController(Controller):
    def home(self):
        self.response.add_header("Content-Type", "text/html")
        self.response.set_body("<h1>This is home page</h1>")

    def about(self):
        self.response.add_header("Content-Type", "text/html")
        self.response.set_body("<h1>This is about page</h1>")
