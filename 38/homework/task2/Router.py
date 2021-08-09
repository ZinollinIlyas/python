import errors


class Router:
    def __init__(self):
        self.routes = {
            "GET": [],
            "POST": []
        }

    def add(self, http_method, uri, controller, method):
        self.routes[http_method.upper()].append({
            "uri": uri,
            "controller": controller,
            "method": method
        })

    def get(self, *args):
        self.add("GET", *args)

    def post(self, *args):
        self.add("POST", *args)

    def run(self, request, response):
        http_method = request.method
        method_routes = self.routes[http_method]

        route = None
        for r in method_routes:
            if r["uri"] == request.uri:
                route = r
                break
        if not route:
            return errors.not_found(request, response)

        try:
            controller = route["controller"](request, response)

            getattr(controller, route["method"])()
        except Exception:
            return errors.internal_server_error(request, response)
