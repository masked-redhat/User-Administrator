from app.routes.users import users_blueprint
from app.routes.root import root_blueprint

route_blueprints = [
    ["/", root_blueprint],
    ["/users", users_blueprint],
]
