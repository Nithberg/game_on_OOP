from questions_settings import Question
import json
import random


def main():
    with open("data_questions.json", "r") as file:
        data_question = json.load(file)

    questions = []
    for value in data_question.values():
        for item in value:
            questions.append(Question(
                item["q"],
                int(item["d"]),
                item["a"]
            ))
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input("Введите ваш ответ на вопрос: ")
        question.user_answer = user_answer
        if question.is_correct():
            print(question.build_posotove_feedback())
        else:
            print(question.build_negative_feedback())

    true_answer_count = 0
    points = 0
    for question in questions:
        if question.is_correct():
            true_answer_count += 1
            points += question.get_points()

    print('Вот и все!')
    print(f'Отвечено {true_answer_count} вопроса из {len(questions)}')
    print(f'Набрано баллов: {points}')


main()