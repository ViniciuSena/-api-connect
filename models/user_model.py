usuarios = []
proximo_id = 1


def gerar_proximo_id():
    global proximo_id
    id_gerado = proximo_id
    proximo_id += 1
    return id_gerado