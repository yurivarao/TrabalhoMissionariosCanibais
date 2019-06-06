import Arvore_Busca

def main():
    # Instancia o problema e gera sua solução
    print (' Problema Missionários e Canibais')
    input (' Pressione QUALQUER TECLA para iniciar a busca.')
    input (' Barco na margem Esquerda = 1; margem Direita = 0')
    problema = Arvore_Busca()
    problema.gerar_solucao()
    # Exibe a solução em tela, separando cada passo
    for est in problema.solucao:
        print (' ')
        print (est)
    print (' A solução foi encontrada!')
    print (' Fim do Programa')
if __name__ == '__main__':
    main()