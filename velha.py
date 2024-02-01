from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class JogoDaVelha(GridLayout):
    def __init__(self, **kwargs):
        super(JogoDaVelha, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for linha in range(3):
            for coluna in range(3):
                botao = Button(font_size=40)
                botao.bind(on_press=self.on_press_botao)
                self.add_widget(botao)
                self.botoes[linha][coluna] = botao

        self.label_pontuacao = Label(text="Jogador X: 0  Jogador O: 0", font_size=20)
        self.add_widget(self.label_pontuacao)

        self.label_resultado = Label(text="", font_size=20)
        self.add_widget(self.label_resultado)

        self.botao_jogar_novamente = Button(text="Jogar Novamente", font_size=20)
        self.botao_jogar_novamente.bind(on_press=self.jogar_novamente)
        self.botao_jogar_novamente.disabled = True
        self.add_widget(self.botao_jogar_novamente)

        self.resetar_jogo()

    def resetar_jogo(self):
        self.jogador_atual = 'X'
        self.fim_de_jogo = False
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.label_resultado.text = ""
        self.botao_jogar_novamente.disabled = True

    def on_press_botao(self, instancia):
        if not self.fim_de_jogo and instancia.text == '':
            linha, coluna = self.obter_posicao_botao(instancia)
            self.tabuleiro[linha][coluna] = self.jogador_atual
            instancia.text = self.jogador_atual

            if self.verificar_vencedor():
                self.label_resultado.text = f"Jogador {self.jogador_atual} vence!"
                self.atualizar_pontuacao()
                self.fim_de_jogo = True
            elif self.verificar_empate():
                self.label_resultado.text = "É um empate!"
                self.fim_de_jogo = True
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

        if self.fim_de_jogo:
            self.botao_jogar_novamente.disabled = False

    def obter_posicao_botao(self, botao):
        for linha in range(3):
            for coluna in range(3):
                if self.botoes[linha][coluna] == botao:
                    return linha, coluna

    def verificar_vencedor(self):
        for i in range(3):
            if (self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] == self.jogador_atual
                    or self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] == self.jogador_atual):
                return True
        if (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == self.jogador_atual
                or self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == self.jogador_atual):
            return True
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for celula in linha:
                if celula == '':
                    return False
        return True

    def atualizar_pontuacao(self):
        if self.fim_de_jogo:
            contagem_x = sum(linha.count('X') for linha in self.tabuleiro)
            contagem_o = sum(linha.count('O') for linha in self.tabuleiro)
            self.label_pontuacao.text = f"Jogador X: {contagem_x}  Jogador O: {contagem_o}"

    def jogar_novamente(self, instancia):
        if not self.fim_de_jogo:
            return  # Evita reiniciar o jogo antes de terminar

        for linha in self.botoes:
            for botao in linha:
                if isinstance(botao, Button):  # Verifica se é um botão
                    botao.text = ''

        self.resetar_jogo()

class AplicativoJogoDaVelha(App):
    def build(self):
        return JogoDaVelha()

if __name__ == '__main__':
    AplicativoJogoDaVelha().run()
