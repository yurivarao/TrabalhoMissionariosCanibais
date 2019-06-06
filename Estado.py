class Estado():

    # Inicializa as variáveis utilizadas na classe Estado
    def __init__(self, canibais, missionarios, barcoMargem):
        self.canibais = canibais
        self.missionarios = missionarios
        self.barcoMargem = barcoMargem
        self.antecessor = None
        self.estados = []

    # Define a representação em string de um estado.
    def __str__(self):
        return 'Canibais: {}| Missionários: {}| Margem: {}'.format(self.canibais, self.missionarios, self.barcoMargem)

    # Verifica se o estado é valido, certificando se o número de canibais é menor ou igual ao número de missionário nas margens
    def estado_valido(self):
        if ((self.missionarios < self.canibais and self.missionarios != 0) or (3-self.missionarios < 3-self.canibais and 3-self.missionarios != 0)):
            return False
        else:
            return True 

    # Verifica se a margem esquerda do estado possui nenhum missionario e canibal, ou seja, todos foram para o outro lado do rio
    def estado_final(self):
        resultado = self.missionarios == self.canibais == 0
        return resultado

    # Adiciona um estado executado pelas operações e validado na lista de estados válidos
    def add_estado(self, estado):
        estado.antecessor = self
        if estado.estado_valido():
            self.estados.append(estado)   

    # Operações Possíveis a serem executadas         
    def operacoes(self): 
        # Lista de strings composto pelas Operações Possíveis 
        operacao = ['OP1','OP2','OP3','OP4','OP5']
        # OP1 - Levar um canibal para outra margem
        # OP2 - Levar dois canibais para outra margem
        # OP3 - Levar um missionario para outra margem
        # OP4 - Levar dois missionarios para outra margem
        # OP5 - Levar um canibal e um missionario para outra margem

        # Para cada operação é verificado que tipo de mudança deve ser feita nas variáveis e depois gera um novo estado
        for op in operacao:
            # Se o barco estiver do lado esquerdo e houver pelo menos 1 canibal deste lado
            if (self.barcoMargem == 1 and self.canibais > 0 and op == 'OP1'):
                canibais = self.canibais - 1
                barcoMargem = 0
                estado = Estado(canibais, self.missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver no lado direito e houver menos que 3 canibais deste lado
            if (self.barcoMargem == 0 and self.canibais < 3 and op == 'OP1'):
                canibais = self.canibais + 1
                barcoMargem = 1
                estado = Estado(canibais, self.missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver do lado esquerdo e houver pelo menos 2 canibais deste lado
            if (self.barcoMargem == 1 and self.canibais > 1 and op == 'OP2'):
                canibais = self.canibais - 2
                barcoMargem = 0
                estado = Estado(canibais, self.missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver no lado direito e houver menos que 2 canibais deste lado
            if (self.barcoMargem == 0 and self.canibais < 2 and op == 'OP2'):
                canibais = self.canibais + 2
                barcoMargem = 1
                estado = Estado(canibais, self.missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver do lado esquerdo e houver pelo menos 1 missionario deste lado
            if (self.barcoMargem == 1 and self.missionarios > 0 and op == 'OP3'):
                missionarios = self.missionarios - 1
                barcoMargem = 0
                estado = Estado(self.canibais, missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver no lado direito e houver menos que 3 missionarios deste lado
            if (self.barcoMargem == 0 and self.missionarios < 3 and op == 'OP3'):
                missionarios = self.missionarios + 1
                barcoMargem = 1
                estado = Estado(self.canibais, missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver do lado esquerdo e houver pelo menos 2 missionarios deste lado    
            if (self.barcoMargem == 1 and self.missionarios > 1 and op == 'OP4'):
                missionarios = self.missionarios - 2
                barcoMargem = 0
                estado = Estado(self.canibais, missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver no lado direito e houver menos que 2 missionarios deste lado
            if (self.barcoMargem == 0 and self.missionarios < 2 and op == 'OP4'):
                missionarios = self.missionarios + 2
                barcoMargem = 1
                estado = Estado(self.canibais, missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver do lado esquerdo e houver pelo menos 1 missionario e 1 canibal deste lado
            if (self.barcoMargem == 1 and self.missionarios > 0 and self.canibais > 0 and op == 'OP5'):
                canibais = self.canibais - 1
                missionarios = self.missionarios - 1
                barcoMargem = 0
                estado = Estado(canibais, missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)
            # Se o barco estiver do lado direito e houver menos que 3 missionarios e 3 canibais deste lado
            if (self.barcoMargem == 0 and self.missionarios < 3 and self.canibais < 3 and op == 'OP5'):
                canibais = self.canibais + 1
                missionarios = self.missionarios + 1
                barcoMargem = 1
                estado = Estado(canibais, missionarios, barcoMargem)
                #estado.add_estado()
                estado.antecessor = self
                if estado.estado_valido():
                    self.estados.append(estado)