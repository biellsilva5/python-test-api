from flask import Flask

from app.blueprints.cpf import cpf_blueprint

def create_app():
    app = Flask("CPF Validator")
    app.config.from_object('config')
    
    app.register_blueprint(cpf_blueprint)

    return app