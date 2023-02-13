import random
from itertools import cycle

def main():
    print(f'Hi, please enter your names:')
    first = input('player1 : \n')
    second = input('player2 : \n')
    players = cycle([first,second])
    letters = ['1','2','3','4']
    random.shuffle(letters)
    print(letters)
    a = Bekr(letters)
    co = True
    while co:
        current_player = next(players)
        answer = input(f'enter your answer {current_player}!\n')
        co = a.check_input(answer,current_player)

    continue_question = input('do you want to continue this game?(y/n)')
    if continue_question == 'y':
        main()
    else:
        print('good bye!')

class Bekr:
    def __init__(self,letters):
        self.letters = letters
        self.answer = False
        self.u_answer = []
    def check_input(self,input,player):
        if len(input)>len(self.letters):
            print('maximum letters are 4!')
        else:
            self.u_answer = list(input)
            return self.compute_answer(player)

    def compute_answer(self,player):
        correct = 0
        incorrect = 0
        for an ,u_an in zip(self.letters,self.u_answer):
            if an == u_an:
                correct += 1
            else:
                incorrect += 1

        if correct == 4:
            print(f'{player} was wined!')
            return False
        else:
            print(correct*'0',incorrect*'x')
            return True


if __name__ == '__main__':
    main()
