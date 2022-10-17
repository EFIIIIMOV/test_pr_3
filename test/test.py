import unittest

from game.main import game
from game.player import Player


class TestMillionaire(unittest.TestCase):
    def test_player_init(self):
        player = Player("Andrey")
        self.assertEqual(player.getName(), "Andrey")
        self.assertEqual(player.getPrize(), 0)

    def test_player_set(self):
        player = Player("")
        player.setName("Igor")
        player.setPrize(10)
        self.assertEqual(player.getName(), "Igor")
        self.assertEqual(player.getPrize(), 10)

    def test_choseQuestion(self):
        now_game = game()
        now_game.sum_question = 1
        var_1 = ["Что означает аббревиатура 'REM'?",
                 ['random energy module', 'rapid eye movement', 'red entertainment machine', 'really energetic music'],
                 'rapid eye movement']

        self.assertEqual(now_game.choseQuestion(), var_1)

    def test_createAnswers(self):
        now_game = game()
        answers = 'random energy module', 'rapid eye movement', 'red entertainment machine', 'really energetic music'
        self.assertEqual(now_game.createAnswers(answers),
                         "A: " + answers[0] + "\n" +
                         "B: " + answers[1] + "\n" +
                         "C: " + answers[2] + "\n" +
                         "D: " + answers[3])

    def test_getAnswer(self):
        now_game = game()
        self.assertEqual(now_game.getAnswer(), True)

    def test_checkAnswer(self):
        now_game = game()
        answer_true = "B"
        answer_false = "A"
        now_question = ['Кто был первым президентом США?',
                        ['Авраам Линкольн', 'Джордж Вашингтон', 'Бенджамин Франклин', 'Джон Адамс'],
                        'Джордж Вашингтон']
        self.assertEqual(now_game.checkAnswer(answer_true, now_question), True)
        self.assertEqual(now_game.checkAnswer(answer_false, now_question), False)


if __name__ == '__main__':
    unittest.main()
