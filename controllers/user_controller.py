from flask import jsonify, request
from models.user_model import usuarios, gerar_proximo_id


def criar_usuario():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"error": "Corpo da requisição ausente ou inválido"}), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not str(nome).strip():
        return jsonify({"error": "O campo 'nome' é obrigatório"}), 400

    if not email or not str(email).strip():
        return jsonify({"error": "O campo 'email' é obrigatório"}), 400

    novo_usuario = {
        "id": gerar_proximo_id(),
        "nome": nome,
        "email": email
    }

    usuarios.append(novo_usuario)

    return jsonify({"data": novo_usuario}), 201


def listar_usuarios():
    return jsonify({"data": usuarios}), 200


def buscar_usuario(id_usuario):
    usuario = next((u for u in usuarios if u["id"] == id_usuario), None)

    if usuario is None:
        return jsonify({"error": "Usuário não encontrado"}), 404

    return jsonify({"data": usuario}), 200


def atualizar_usuario(id_usuario):
    dados = request.get_json(silent=True)

    indice = next((i for i, u in enumerate(usuarios) if u["id"] == id_usuario), None)

    if indice is None:
        return jsonify({"error": "Usuário não encontrado"}), 404

    if not dados:
        return jsonify({"error": "Corpo da requisição ausente ou inválido"}), 400

    usuarios[indice]["nome"] = dados.get("nome", usuarios[indice]["nome"])
    usuarios[indice]["email"] = dados.get("email", usuarios[indice]["email"])

    return jsonify({"data": usuarios[indice]}), 200


def deletar_usuario(id_usuario):
    indice = next((i for i, u in enumerate(usuarios) if u["id"] == id_usuario), None)

    if indice is None:
        return jsonify({"error": "Usuário não encontrado"}), 404

    usuarios.pop(indice)

    return '', 204