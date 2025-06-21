class Lista:
    def __init__(self):
        self.itens = []

    def pesquisar(self, valor):
        if valor in self.itens:
            return self.itens.index(valor)
        raise ValueError(f"Item {valor} não encontrado na lista!")

    def retirar_por_valor(self, valor):
        if valor not in self.itens:
            raise ValueError(f"Valor {valor} não presente na lista!")
        self.itens.remove(valor)

    def esta_vazia(self):
        return len(self.itens) == 0

    def inserir_apos(self, indice, valor):
        if indice < 0 or indice >= len(self.itens):
            raise IndexError(f"Não há item na posição {indice} para inserir após!")
        self.itens.insert(indice + 1, valor)

    def retirar_por_indice(self, indice):
        if indice < 0 or indice >= len(self.itens):
            raise IndexError(f"Não há item na posição {indice} para remoção!")
        return self.itens.pop(indice)

    def tamanho(self):
        return len(self.itens)

    def modificar(self, indice, novo_valor):
        if indice < 0 or indice >= len(self.itens):
            raise IndexError(f"Não há item na posição {indice} para modificação!")
        self.itens[indice] = novo_valor

    def __str__(self):
        return f"{self.itens}"
