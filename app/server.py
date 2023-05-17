from flask import Flask

from controllers.clientController import user_controller

app = Flask(__name__)

# Registrando os blueprints dos controllers
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(user_controller)

if __name__ == '__main__':
    app.run()
