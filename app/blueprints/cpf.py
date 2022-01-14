import json
from flask import Blueprint, jsonify

from app.service.cpf import CPFCheckBlacklist

cpf_blueprint = Blueprint('cpfs', __name__)


@cpf_blueprint.route('/<cpf>') 
def cpf(cpf):
    try:
        cpf = CPFCheckBlacklist(cpf)
    except TypeError as e:
        return jsonify({'error': e.args}),400

    if cpf.check():
        return jsonify({'status': 'BLOCK'})
    return jsonify({'status': 'FREE'})