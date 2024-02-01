from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class JogoDaVelha(GridLayout):
    def __init__(self, **kwargs):
        super(JogoDaVelha, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.botoes = []
        self.jogador_atual = 'X'
        self.pontuacao_jogadores = {'X': 0, 'O': 0}

        for linha in range(3):
            for coluna in range(3):
                botao = Button()
                botao.bind(on_press=self.celula_clicada)
                self.botoes.append(botao)
                self.add_widget(botao)

        self.botao_reset = Button(text="Reiniciar Jogo", on_press=self.reiniciar_jogo)
        self.add_widget(self.botao_reset)

        self.rotulo_vencedor = Label(text="")
        self.add_widget(self.rotulo_vencedor)

    def celula_clicada(self, instancia):
        if instancia.text == '':
            instancia.text = self.jogador_atual
            if self.jogador_atual == 'X':
                instancia.background_color = (0, 1, 0, 1)  # Verde para X
            else:
                instancia.background_color = (0, 0, 1, 1)  # Azul para O
            if self.verificar_vencedor():
                self.pontuacao_jogadores[self.jogador_atual] += 1
                self.rotulo_vencedor.text = f'{self.jogador_atual} venceu! Pontuação: X-{self.pontuacao_jogadores["X"]} O-{self.pontuacao_jogadores["O"]}'
                if max(self.pontuacao_jogadores.values()) == 3:
                    self.rotulo_vencedor.text += "\nFim de Jogo! Jogador atingiu 3 vitórias."
                    for botao in self.botoes:
                        botao.disabled = True
                        botao.background_color = (1, 1, 1, 1)  # Resetar cor de fundo para branco
                self.reiniciar_tabuleiro()
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def verificar_vencedor(self):
        # Verifica linhas, colunas e diagonais para um vencedor
        for i in range(3):
            if (self.botoes[i * 3].text == self.botoes[i * 3 + 1].text == self.botoes[i * 3 + 2].text != '') or \
               (self.botoes[i].text == self.botoes[i + 3].text == self.botoes[i + 6].text != ''):
                return True
        if (self.botoes[0].text == self.botoes[4].text == self.botoes[8].text != '') or \
           (self.botoes[2].text == self.botoes[4].text == self.botoes[6].text != ''):
            return True
        return False

    def reiniciar_tabuleiro(self):
        for botao in self.botoes:
            botao.text = ''
            botao.background_color = (1, 1, 1, 1)  # Redefine cor de fundo para branco
        self.jogador_atual = 'X'

    def reiniciar_jogo(self, instancia):
        for botao in self.botoes:
            botao.text = ''
            botao.background_color = (1, 1, 1, 1)  # Redefine cor de fundo para branco
            botao.disabled = False
        self.jogador_atual = 'X'
        self.pontuacao_jogadores = {'X': 0, 'O': 0}
        self.rotulo_vencedor.text = ""

class AppJogoDaVelha(App):
    def build(self):
        return JogoDaVelha()

if __name__ == '__main__':
    AppJogoDaVelha().run()
