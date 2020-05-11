from api.configuration import Configuration
from api.controllers import error_handler, product_controller


app = Configuration.get_app()
app.register_blueprint(product_controller)
app.register_blueprint(error_handler)

if __name__ == '__main__':
    app.run(debug=True)
