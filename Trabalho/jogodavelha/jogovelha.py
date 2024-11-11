class Jogador:
    def __init__(self, nome: str, simbolo: str) -> None:
        """Inicializa as instâncias da classe Jogador

        Args:
            nome (str): Nome do jogador
            simbolo (str): Simbolo do jogador na partida

        Returns:
            None
        """
        self.nome = nome
        self.simbolo = simbolo

    def fazer_jogada(self) -> tuple:
        """Função vazia

        Args:
            None

        Returns:
            None
        """
        #A função será definida nas classes que herdam dessa
        pass


class JogadorHumano(Jogador):
    def fazer_jogada(self) -> tuple:
        """Pede para o jogador escolher uma casa

        Args:
            None

        Returns:
            tuple: Tupla que mostra as coordenadas da casa marcada
        """
        print('Por favor, digite o primeiro número da coordenada da casa:')
        num1 = input()
        print('Por favor, digite o segundo número da coordenada da casa:')
        num2 = input()
        jogada = (num1, num2)
        return jogada


class JogadorComputador(Jogador):
    
    def __init__(self, nome: str, simbolo: str, estrategia: str) -> None:
        """Inicializa as intâncias da classe JogadorComputador

        Args:
            estrategia (str): Define a estrategia do computador

        Returns:
            None
        """
        self.nome = nome
        self.simbolo = simbolo
        self.estrategia = estrategia

    def fazer_jogada(self) -> tuple:
        """O computador escolhe uma casa de acordo com a sua estratégia

        Args:
            None

        Returns:
            None
        """
        if self.estrategia == aleatoria:
            num1 = random.randint(1, 3)
            num2 = random.randint(1, 3)
            jogada = (num1, num2)
            return jogada


class Tabuleiro:
    def __init__(self) -> None:
        """Inicializa as intâncias da classe Tabuleiro

        Args:
            None

        Returns:
            None
        """
        #O tabuleiro sempre começará vazio
        self.casas = ['', '', '', '', '', '', '', '', '']

    def pegar_tabuleiro(self) -> list:
        """Cria uma lista mostrando o tabuleiro

        Args:
            None

        Returns:
            list: Lista de listas que mostram o tabuleiro com base nas linhas dele
        """
        primeira_fileira = []
        segunda_fileira = []
        terceira_fileira = []
        #O loop colocará cada valor de casa em sua devida linha
        for i in range(0, 9):
            if i <= 2:
                primeira_fileira.append(self.casas[i])
            elif 2<i<=5:
                segunda_fileira.append(self.casas[i])
            else:
                terceira_fileira.append(self.casas[i])
        tabuleiro_listas = []
        tabuleiro_listas.append(primeira_fileira)
        tabuleiro_listas.append(segunda_fileira)
        tabuleiro_listas.append(terceira_fileira)
        return tabuleiro_listas

    def marcar_casa(self, jogada: tuple, marcador: str) -> None:
        """Marca uma casa do tabuleiro

        Args:
            jogada (tuple): As coordenadas da casa que será marcada
            marcador (str): Símbolo do jogador que marcou a casa

        Returns:
            None
        """
        #Sequência de if e elifs que verificam se a casa está vazia
        if jogada == (1, 1):
            if self.casas[0] == '':
                self.casas[0] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (1, 2):
            if self.casas[1] == '':
                self.casas[1] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (1, 3):
            if self.casas[2] == '':
                self.casas[2] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (2, 1):
            if self.casas[3] == '':
                self.casas[3] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (2, 2):
            if self.casas[4] == '':
                self.casas[4] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (2, 3):
            if self.casas[5] == '':
                self.casas[5] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (3, 1):
            if self.casas[6] == '':
                self.casas[6] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (3, 2):
            if self.casas[7] == '':
                self.casas[7] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')
        elif jogada == (3, 3):
            if self.casas[8] == '':
                self.casas[8] = marcador
            else:
                print('Por favor, escolha outra casa. Essa já foi escolhida!')

    def imprimir_tabuleiro(self) -> None:
        """Imprime o tabuleiro atual

        Args:
            None

        Returns:
            None
        """
        tabuleiro_impresso = '/'.join(self.casas)
        print(tabuleiro_impresso)


class JogoVelha:
    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:
        """Inicializa as intâncias da classe JogoVelha

        Args:
            jogador1 (Jogador): Primeiro jogador
            jogador2 (Jogador): segundo jogador

        Returns:
            None
        """
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogadores = [jogador1, jogador2]
        self.tabuleiro = Tabuleiro()
        self.turno = 2

    def jogador_atual(self) -> Jogador:
        """Muda o turno e identific o jogador atual

        Args:
            None

        Returns:
            Jogador: Jogador atual
        """
        #O turno será mudado a cada jogada
        if self.turno == 1:
            jogadorAtual = self.jogadores[1]
            self.turno = 2
        else:
            jogadorAtual = self.jogadores[0]
            self.turno = 1
        return jogadorAtual

    def checar_fim_de_jogo(self) -> str:
        """Checa se o jogo acabou

        Args:
            None

        Returns:
            str: O jogo acabou de algum modo
            None: O jogo não acabou
        """
        is_casa_vazia_list = []
        for i in range(0,9):
            if tabuleiro.casas[i] == '':
                is_casa_vazia_list.append(1)
            else:
                is_casa_vazia_list.append(0)
        if 1 in is_casa_vazia_list:
            is_not_casas_vazias = False
        else:
            is_not_casas_vazias = True
        #Bools que verificam se uma condição para o jogo acabar foi completa
        is_linha_completa = tabuleiro.casas[0] == tabuleiro.casas[1] == tabuleiro.casas[2] != '' or tabuleiro.casas[3] == tabuleiro.casas[4] == tabuleiro.casas[5] != '' or tabuleiro.casas[6] == tabuleiro.casas[7] == tabuleiro.casas[8] != ''
        is_coluna_completa = tabuleiro.casas[0] == tabuleiro.casas[3] == tabuleiro.casas[6] != '' or tabuleiro.casas[1] == tabuleiro.casas[4] == tabuleiro.casas[7] != '' or tabuleiro.casas[2] == tabuleiro.casas[5] == tabuleiro.casas[8] != ''
        is_diagonal_completa = tabuleiro.casas[0] == tabuleiro.casas[4] == tabuleiro.casas[8] != '' or tabuleiro.casas[2] == tabuleiro.casas[4] == tabuleiro.casas[6] != ''
        if is_linha_completa:
            return 'Um jogador completou uma linha'
        elif is_coluna_completa:
            return 'Um jogador completou uma coluna'
        elif is_diagonal_completa:
            return 'Um jogador completou uma diagonal'
        elif (not is_linha_completa) and (not is_coluna_completa) and (not is_diagonal_completa) and is_not_casas_vazias:
            return 'O jogo deu velha'
        else:
            #Se o jogo não acabou, retorna None
            return None

    def jogar(self) -> None:
        """Inicia uma partida de jogo da velha

        Args:
            None

        Returns:
            None
        """
        #Loop que só acaba quando o jogo terminar
        while True:
            atual = self.jogador_atual()
            print(f'Sua vez, {atual}!')
            if self.turno == 1:
                jogada = self.jogador1.fazer_jogada()
                self.tabuleiro.marcar_casa(jogada, self.jogador1.simbolo)
            else:
                jogada = self.jogador2.fazer_jogada()
                self.tabuleiro.marcar_casa(jogada, self.jogador2.simbolo)
            self.tabuleiro.imprimir_tabuleiro()
            is_fim_do_jogo = self.checar_fim_de_jogo()
            if is_fim_do_jogo.isalpha() == True:
                print(is_fim_do_jogo)
                break
            else:
                continue