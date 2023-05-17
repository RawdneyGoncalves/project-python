from flask import Flask

from controllers.clientController import user_controller

app = Flask(__name__)

# Registrar os blueprints dos controllers
app.register_blueprint(user_controller)

if __name__ == '__main__':
    app.run()
