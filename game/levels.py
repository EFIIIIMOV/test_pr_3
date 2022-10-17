import random


class levels():

    def choseQuestion(self, questionCount):
        return random.randrange(1, questionCount + 1)

    def level_1(self):
        # Lists containing questions, mutliple-choice options, and answers
        questions = {1: "Кто был первым президентом США?",
                     2: "Что означает аббревиатура 'REM'?",
                     3: "Для какого заболевания характерна неспособность организма правильно метаболизировать глюкозу?"}
        possible_answers = {1: ['Авраам Линкольн', 'Джордж Вашингтон', 'Бенджамин Франклин', 'Джон Адамс'],
                            2: ['random energy module', 'rapid eye movement', 'red entertainment machine',
                                'really energetic music'],
                            3: ['Грипп', 'Септицемия', 'Диабет', 'Артрит']}
        answers = {1: 'Джордж Вашингтон', 2: 'rapid eye movement', 3: 'Диабет'}

        questionNumb = self.choseQuestion(len(questions))
        packQuestion = [questions[questionNumb], possible_answers[questionNumb], answers[questionNumb]]

        return packQuestion

    def level_2(self):
        # Lists containing questions, mutliple-choice options, and answers
        questions = {1: "Из какого языка происходит термин 'RSVP'?",
                     2: "Какое животное считается священным в Индии?",
                     3: "Генри Джеймс однажды заметил, что «два самых красивых слова в английском языке» — это то, что?"}
        possible_answers = {1: ['Русский', 'Итальянский', 'Португальский', 'Французский'],
                            2: ['Овца', 'Корова', 'Курица', 'Собака'],
                            3: ['Полная тишина', 'Летний полдень', 'Летнее кафе', 'Журчание ручья']}
        answers = {1: 'Французский', 2: 'Корова', 3: 'Летний полдень'}

        questionNumb = self.choseQuestion(len(questions))
        packQuestion = [questions[questionNumb], possible_answers[questionNumb], answers[questionNumb]]

        return packQuestion

    def level_3(self):
        # Lists containing questions, mutliple-choice options, and answers
        questions = {1: "На какой из этих достопримечательностей США есть надпись 'Pass and Stow'?",
                     2: "'Pua alohalo' официальный штат Гавайев?",
                     3: "Знаменитая мелодия какой песни была написана в 1893 году сестрами Пэтти и Милдред Хилл?"}
        possible_answers = {1: ['Статуя Свободы', 'Плимут Рок', 'Мемориал Линкольна', 'Колокол Свободы'],
                            2: ['Птица', 'Цветок', 'Рыба', 'Драгоценный камень'],
                            3: ['Греби, греби, греби на своей лодке', 'С днем рождения тебя',
                                "Не останавливайся, пока не наберешься",
                                'Колокольчики']}
        answers = {1: 'Колокол Свободы', 2: 'Цветок', 3: 'С днем рождения тебя'}

        questionNumb = self.choseQuestion(len(questions))
        packQuestion = [questions[questionNumb], possible_answers[questionNumb], answers[questionNumb]]

        return packQuestion

    def level_4(self):
        # Lists containing questions, mutliple-choice options, and answers
        questions = {1: "При президенте Форде 34-летний Дик Чейни стал самым молодым человеком на какой должности?",
                     2: "Какой очень высокий писатель когда-то использовал псевдоним Джон Ланге, немецкая фамилия, означающая «длинный»?",
                     3: "Рожденный с менее крутым именем Уолтер, кто из этих актеров предпочитает носить свое второе имя?"}
        possible_answers = {
            1: ['Глава администрации Белого дома', 'Генеральный прокурор', 'Советник по национальной безопасности',
                'Госсекретарь'],
            2: ['Роберт Ладлум', 'Стивен Кинг', 'Джон Ирвинг', 'Майкл Крайтон'],
            3: ['Харрисон Форд', 'Мэтт Дэймон', 'Брюс Уиллис', 'Николас Кейдж']}
        answers = {1: 'Глава администрации Белого дома', 2: 'Майкл Крайтон', 3: 'Брюс Уиллис'}

        questionNumb = self.choseQuestion(len(questions))
        packQuestion = [questions[questionNumb], possible_answers[questionNumb], answers[questionNumb]]

        return packQuestion

    def level_5(self):
        # Lists containing questions, mutliple-choice options, and answers
        questions = {
            1: "В египетской мифологии криосфинкс — это фигура с телом льва и головой какого-то зверя?",
            2: "Первым рентгеновским снимком человеческого тела было изображение руки жены ученого?",
            3: "Аристотель писал, что какое животное, хотя и невосприимчивое к другим болезням, иногда подвержено «метеоризму»?"}
        possible_answers = {1: ['Баран', 'Орел', 'Лошадь', 'Собакаy'],
                            2: ['Ганс Гейгер', 'Энрико Ферми', 'Вильгельм Рентген', 'Нильс Бор'],
                            3: ['Слон', 'Собака', 'Лев', 'Коза']}
        answers = {1: 'Баран', 2: 'Вильгельм Рентген', 3: 'Слон'}

        questionNumb = self.choseQuestion(len(questions))
        packQuestion = [questions[questionNumb], possible_answers[questionNumb], answers[questionNumb]]

        return packQuestion
