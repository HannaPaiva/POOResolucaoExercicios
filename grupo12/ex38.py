from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.buttons = []
        self.current_player = 'X'
        self.player_scores = {'X': 0, 'O': 0}

        for row in range(3):
            for col in range(3):
                button = Button()
                button.bind(on_press=self.cell_click)
                self.buttons.append(button)
                self.add_widget(button)

        self.reset_button = Button(text="Reset Game", on_press=self.reset_game)
        self.add_widget(self.reset_button)

        self.winner_label = Label(text="")
        self.add_widget(self.winner_label)

    def cell_click(self, instance):
        if instance.text == '':
            instance.text = self.current_player
            if self.check_winner():
                self.player_scores[self.current_player] += 1
                self.winner_label.text = f'{self.current_player} wins! Score: X-{self.player_scores["X"]} O-{self.player_scores["O"]}'
                if max(self.player_scores.values()) == 3:
                    self.winner_label.text += "\nGame Over! Player reached 3 wins."
                    for button in self.buttons:
                        button.disabled = True
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if (self.buttons[i * 3].text == self.buttons[i * 3 + 1].text == self.buttons[i * 3 + 2].text != '') or \
               (self.buttons[i].text == self.buttons[i + 3].text == self.buttons[i + 6].text != ''):
                return True
        if (self.buttons[0].text == self.buttons[4].text == self.buttons[8].text != '') or \
           (self.buttons[2].text == self.buttons[4].text == self.buttons[6].text != ''):
            return True
        return False

    def reset_board(self):
        for button in self.buttons:
            button.text = ''
        self.current_player = 'X'

    def reset_game(self, instance):
        for button in self.buttons:
            button.text = ''
            button.disabled = False
        self.current_player = 'X'
        self.player_scores = {'X': 0, 'O': 0}
        self.winner_label.text = ""

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()

if __name__ == '__main__':
    TicTacToeApp().run()
