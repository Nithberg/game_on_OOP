class Question:
    def __init__(self, question_text, question_difficult, true_answer):
        self.question_text = question_text
        self.question_difficult = question_difficult
        self.true_answer = true_answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.question_difficult * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.user_answer == self.true_answer

    def build_question(self):
        get_question = f'Вопрос: {self.question_text}\n' \
                       f'Сложность: {self.question_difficult}/5'
        return get_question

    def build_posotove_feedback(self):
        answer_result = f'\nОтвет верный, получено {self.points} баллов'
        return answer_result

    def build_negative_feedback(self):
        answer_result = f'\nОтвет неверный, верный ответ {self.true_answer}'
        return answer_result

    def __repr__(self):
        return f'{self.question_text}? - {self.true_answer} ({self.question_difficult}/5)'
