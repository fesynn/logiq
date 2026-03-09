def merge(esquerda, direita):
    resultado = []

    while len(esquerda) > 0 and len(direita) > 0:
        if esquerda[0]["timestamp"] < direita[0]["timestamp"]:
            resultado.append(esquerda[0])
            esquerda = esquerda[1:]
        else:
            resultado.append(direita[0])
            direita = direita[1:]

    return resultado + esquerda + direita

def sort_logs(logs):  # O(n log n)
    if len(logs) <= 1:
        return logs

    meio = len(logs) // 2
    esquerda = logs[:meio]
    direita = logs[meio:]

    esquerda = sort_logs(esquerda)
    direita = sort_logs(direita)

    return merge(esquerda, direita)