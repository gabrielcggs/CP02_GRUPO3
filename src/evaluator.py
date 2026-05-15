def medir_acuracia(resposta, esperado):

    resposta = resposta.lower().strip()
    esperado = esperado.lower().strip()

    if esperado in resposta:
        return 1

    return 0