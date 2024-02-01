from abc import ABC, abstractmethod
import random

class Jogo(ABC):
  
    def __init__(self):
        print('bom jogo ...')
        self.inicializa_tabuleiro()

    @abstractmethod
    def joga_humano(self, jogador):
        """Método que solicita ao humano (jogador) a próxima jogada e coloca-a no tabuleiro.

        Args:
            jogador (int): Número do jogador (0 ou 1)
        """
        pass

    @abstractmethod
    def terminou(self):
        """Devolve True se foi verificada a condição de paragem, i.e., um jogador ganhou. False caso contrário."""
        pass

    @abstractmethod
    def mostra_tabuleiro(self):
        """Desenha o tabuleiro."""
        pass

    @abstractmethod
    def inicializa_tabuleiro(self):
        """Inicializa o tabuleiro de jogo."""
        pass

    @abstractmethod
    def ha_jogadas_possiveis(self):
        """Verifica se ainda há jogadas possíveis ou se o jogo está empatado."""
        pass

    def jogar(self):
        """Corre o jogo..."""
        jogador = random.randint(0, 1)
        while True:
            self.mostra_tabuleiro()
            self.joga_humano(jogador)
            if self.terminou():
                self.mostra_tabuleiro()
                print(f'o jogador {jogador} ganhou!!')
                return
            elif not self.ha_jogadas_possiveis():
                print('Empataram!!!')
                return
            jogador = (jogador + 1) % 2

class QuatroEmLinha(Jogo):
    def inicializa_tabuleiro(self):
        self.tabuleiro = [[' ' for _ in range(7)] for _ in range(6)]

    def joga_humano(self, jogador):
        print(f'Jogador {jogador} insira a sua jogada:')
        while True:
            coluna = int(input('Coluna (0-6): '))
            if 0 <= coluna <= 6 and ' ' in [linha[coluna] for linha in self.tabuleiro]:
                linha = max(i for i in range(6) if self.tabuleiro[i][coluna] == ' ')
                self.tabuleiro[linha][coluna] = ['X', 'O'][jogador]
                return
            else:
                print('Jogada inválida. Tente novamente.')

    def terminou(self):
        # Verifica a vitória na horizontal --------------------------
        for linha in self.tabuleiro:
            for i in range(len(linha) - 3):
                if linha[i] == linha[i + 1] == linha[i + 2] == linha[i + 3] != ' ':
                    return True

        # Verifica a vitória na vertical  ||||||||||||||||||||||||||
        for coluna in range(len(self.tabuleiro[0])):
            for i in range(len(self.tabuleiro) - 3):
                if (self.tabuleiro[i][coluna] == self.tabuleiro[i + 1][coluna] ==
                        self.tabuleiro[i + 2][coluna] == self.tabuleiro[i + 3][coluna] != ' '):
                    return True

        # Verifica a vitória na diagonal (esquerda para a direita) \\\\\\\\\\\\\\\\\\\\\
        for linha in range(len(self.tabuleiro) - 3):
            for coluna in range(len(self.tabuleiro[0]) - 3):
                if (self.tabuleiro[linha][coluna] == self.tabuleiro[linha + 1][coluna + 1] ==
                        self.tabuleiro[linha + 2][coluna + 2] == self.tabuleiro[linha + 3][coluna + 3] != ' '):
                    return True

        # Verifica a vitória na diagonal (direita para a esquerda) //////////////////
        for linha in range(len(self.tabuleiro) - 3):
            for coluna in range(3, len(self.tabuleiro[0])):
                if (self.tabuleiro[linha][coluna] == self.tabuleiro[linha + 1][coluna - 1] ==
                        self.tabuleiro[linha + 2][coluna - 2] == self.tabuleiro[linha + 3][coluna - 3] != ' '):
                    return True

        return False


    def mostra_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|', end='')
            for celula in linha:
                print(celula, '|', end='')
            print()
        print('---------------')

    def ha_jogadas_possiveis(self):
        return any(' ' in linha for linha in self.tabuleiro)

# Teste do jogo Quatro em Linha
quatro_em_linha = QuatroEmLinha()
quatro_em_linha.jogar()
