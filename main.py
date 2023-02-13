import random


def main():
    print(f'Hi, user')
    a = Bekr()
    co = True
    while co:
        answer = input('enter your answer!\n')
        co = a.check_input(answer)

    continue_question = input('do you want to continue this game?(y/n)')
    if continue_question == 'y':
        main()
    else:
        print('good bye!')

class Bekr:
    def __init__(self):
        self.letters = ['1','2','3','4']
        self.answer = False
        self.u_answer = []
    def check_input(self,input):
        if not self.answer:
            random.shuffle(self.letters)
            self.answer = True
        if len(input)>len(self.letters):
            print('maximum letters are 4!')
        else:
            self.u_answer = list(input)
            return self.compute_answer()

    def compute_answer(self):
        correct = 0
        incorrect = 0
        for an ,u_an in zip(self.letters,self.u_answer):
            if an == u_an:
                correct += 1
            else:
                incorrect += 1

        if correct == 4:
            print('you win')
            return False
        else:
            print(correct*'0',incorrect*'x')
            return True


if __name__ == '__main__':
    main()
