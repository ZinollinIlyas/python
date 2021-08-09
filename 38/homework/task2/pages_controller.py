from controller import Controller
from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader(THIS_DIR)
)


class ClickController(Controller):
    counter = 0

    def get_click(self):
        body = ""
        self.response.add_header("Content-Type", "text/html")
        self.response.add_header("Connection", "close")
        template = env.get_template("templates/index.html")
        body = template.render({"counter": ClickController.counter})

        self.response.set_body(body)

    def count_click(self):
        ClickController.counter += 1
        self.response.add_header("Content-Type", "text/html")
        self.response.add_header("Connection", "close")
        self.response.add_header("Location", "/")
        self.response.set_status(self.response.HTTP_MOVED_PERMANENTLY)

