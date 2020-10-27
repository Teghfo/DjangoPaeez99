from controllers import register, login


routing_path = {
    'login': login,
    'register': register
}


def find_route(route):
    if route in routing_path:
        return routing_path[route]
    else:
        raise ValueError("cant find route.404")
