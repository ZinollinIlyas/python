from controller import Controller


class PostController(Controller):
    def list(self):
        posts = [
            {"id": 1, "title": "First post"},
            {"id": 2, "title": "Second post"},
            {"id": 3, "title": "Third post"}
        ]
        body = "<h1>Posts page</h1>"
        for post in posts:
            body += f"<h3>{post['title']} (ID:{post['id']})"
        self.response.add_header("Content-Type", "text/html")
        self.response.set_body(body)

    def update(self):
        pass

    def retrieve(self):
        pass
