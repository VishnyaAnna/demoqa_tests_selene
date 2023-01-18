import allure
from demoqa_tests_selene.model.data.student import *
from demoqa_tests_selene.model.pages import practice_form


@allure.title("demoqa форма регистрации")
def test_sending():
    a_vishnyakova = Student(
        first_name='Anna',
        last_name='Vishnyakova',
        email='mypochta@pochta.ru',
        phone='89000000000',
        address='Москва',
        birthday=date(1994, 6, 3),
        gender=Gender.Female,
        subjects=[Subject.Maths, Subject.Arts],
        hobby=[Hobby.Sports, Hobby.Music],
        image='test.png',
        state=State.Haryana,
        city=City.Panipat
    )

    with allure.step('Открываем форму регистрации'):
        practice_form.open()

    with allure.step('Заполняем данные'):
        practice_form.fill_data(a_vishnyakova)

    with allure.step('Отправляем форму'):
        practice_form.submit()

    with allure.step('Проверяем форму'):
        practice_form.validation_data('Anna Vishnyakova',
                                      'mypochta@pochta.ru',
                                      'Female',
                                      '8900000000',
                                      '03 July,1994',
                                      'Maths, Arts',
                                      'Sports, Music',
                                      'test.png',
                                      'Москва',
                                      'Haryana Panipat')
