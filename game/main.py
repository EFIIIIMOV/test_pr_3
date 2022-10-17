from game.levels import levels
from game.player import Player


class game():
    answerDict = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
    }

    prizeDict = {
        1: 50000,
        2: 100000,
        3: 250000,
        4: 500000,
        5: 1000000,
    }

    def __init__(self):
        self.sum_question = 1
        self.answer = ""

    def print_instructions(self):
        print("Правила \n-----------------------------------------------------------------------------")
        print("1) Вам будет дано 5 вопросов, необходимо выбирать правильный вариант.")
        print("2) Если вы ответите не правильно игра закончится.")
        print("3) У вас есть 3 подсказки:")
        print("\t50:50 ......................Уберет 2 неверных ответа.")
        print("\tЗвонок другу................Вы сможете позвонить и спросить у кого-то.")
        print("\tСпросить зал............... Можете загуглить вопрос")
        print("4) Ответив на все вопросы правильно вы получите ₽1,000,000.00")
        print("Удачи :) \n-----------------------------------------------------------------------------")

    def choseQuestion(self):
        level = levels()
        if (self.sum_question == 1):
            return level.level_1()
        elif (self.sum_question == 2):
            return level.level_2()
        elif (self.sum_question == 3):
            return level.level_3()
        elif (self.sum_question == 4):
            return level.level_4()
        elif (self.sum_question == 5):
            return level.level_5()

    def createAnswers(self, answers):
        crAns = "A: " + answers[0] + "\n" + "B: " + answers[1] + "\n" + "C: " + answers[2] + "\n" + "D: " + answers[3]
        print(crAns)
        return crAns

    def getAnswer(self):
        temp = str(input())
        print("")
        if (temp == "A" or temp == "B" or temp == "C" or temp == "D"):
            self.answer = temp
            return True
        else:
            print("Ошибка ввода")
            self.getAnswer()
            return False

    def gameplay(self):
        print("Как вас зовут?")
        player = Player(input())

        while (self.sum_question < 6):
            "Вопрос №" + str(self.sum_question)
            now_question = self.choseQuestion()
            print(now_question[0])
            self.createAnswers(now_question[1])
            print("")
            print("Вариант ответа > ")
            self.getAnswer()
            print("")
            if (self.checkAnswer(self.answer, now_question) == False):
                print("Правильный ответ: " + now_question[2])
                print("ИТОГ: " + player.getName() + " результат: " + str(player.getPrize()))
                break
            print("Приз: " + str(self.prizeDict[self.sum_question]))
            player.setPrize(self.prizeDict[self.sum_question])
            print()
            self.sum_question += 1

    def checkAnswer(self, answer, now_question):
        if (now_question[1][self.answerDict[answer]] == now_question[2]):
            print("Верно!")
            return True
        else:
            print("Не верно!")
            return False


if __name__ == '__main__':
    now_game = game()
    now_game.gameplay()
