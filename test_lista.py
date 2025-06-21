from lista import Lista

def test_lista():
    lista = Lista()
    lista.itens = [1, 2, 3]

    assert lista.pesquisar(2) == 1
    lista.inserir_apos(1, 4)
    assert lista.itens == [1, 2, 4, 3]
    lista.modificar(0, 99)
    assert lista.itens[0] == 99
    lista.retirar_por_valor(4)
    assert 4 not in lista.itens
    assert not lista.esta_vazia()
    lista.retirar_por_indice(0)
    lista.retirar_por_indice(0)
    lista.retirar_por_indice(0)
    assert lista.esta_vazia()

if __name__ == "__main__":
    test_lista()
    print("Todos os testes passaram!")
