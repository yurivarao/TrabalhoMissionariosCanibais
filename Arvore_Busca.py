import Estado

class Arvore_Busca():

    # Inicializa as variáveis utilizadas na classe Arvore_Busca
    def __init__(self):

        # Insere o primeiro estado na fila de execução, sendo o estado inicial do problema (3 Canibais, 3 Missionarios, 1 Barco na margem Esquerda)
        self.fila_execucao = [Estado(3, 3, 1)]
        self.solucao = None

    # Gera a solução utilizando uma busca em largura na árvore gerada com os estados contidos na fila de execução.    
    def gerar_solucao(self):

        for obj in self.fila_execucao:
            # Busca na árvore os estados pertencentes a um desterminado antecessor
            if obj.estado_final():
                self.solucao = [obj]
                while obj.antecessor:
                    self.solucao.insert(0, obj.antecessor)
                    obj = obj.antecessor
                break;
            obj.operacoes()
            self.fila_execucao.extend(obj.estados)