from controller import Controller
from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader(THIS_DIR)
)


class PagesController(Controller):
    def home(self):
        body = ""
        self.response.add_header("Content-Type", "text/html")
        self.response.add_header("Connection", "close")
        template = env.get_template("templates/index.html")
        body = template.render()

        self.response.set_body(body)

    def one(self):
        body = ""
        self.response.add_header("Content-Type", "text/html")
        self.response.add_header("Connection", "close")
        template = env.get_template("templates/one.html")
        body = template.render()

        self.response.set_body(body)

    def two(self):
        body = ""
        self.response.add_header("Content-Type", "text/html")
        self.response.add_header("Connection", "close")
        template = env.get_template("templates/two.html")
        body = template.render()

        self.response.set_body(body)

    def three(self):
        body = ""
        self.response.add_header("Content-Type", "text/html")
        self.response.add_header("Connection", "close")
        template = env.get_template("templates/three.html")
        body = template.render()

        self.response.set_body(body)
