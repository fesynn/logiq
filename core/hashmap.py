class LogHashMap:
    def __init__(self):
        self.logs = {} #Começa com um dic vazio

    def insert(self, log):
        self.logs[log["id"]] = log  #Recebe um log inteiro, pega o id dele como chave e guarda no dic. Vai direto no endereço — O(1).

    def get(self, id):
        return self.logs[id]  #Recebe um id, vai direto naquele endereço do dicionário e retorna o log. Não percorre nada — O(1).

    def delete(self, id):
        del self.logs[id]  #Recebe um id e deleta aquela entrada do dicionário. Vai direto — O(1).

    def get_all(self):
        return self.logs.values()  #Retorna todos os logs. Precisa passar por cada um — quanto mais logs, mais demora — O(n).


