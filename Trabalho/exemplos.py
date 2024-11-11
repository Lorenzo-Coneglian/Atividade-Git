from jogodavelha.jogovelha import JogoVelha, JogadorHumano, JogadorComputador, Tabuleiro

jogador1 = JogadorHumano('Lorenzo', 'X')
jogador2 = JogadorComputador('AstroBot', 'O', 'aleatorio')
nova_partida = JogoVelha(jogador1, jogador2)
nova_partida.jogar()