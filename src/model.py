from openai import OpenAI

from src.read_cv import read_cv


def predict(path_cv: str, api_key) -> str:
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )

    cv = read_cv(path_cv)

    raw_json_for_write = open("../examples/case_1_data_for_members.json").read()

    raw_promt = f"""Выше я написал резюме, которое надо разбить в json-файл: {raw_json_for_write}. Также я дам тебе пример резюме и json-файл по которому ты должен сделать подобное с новым резюме.
    1. Типы контактов - contact_type:
        1: Телефон
        2: Email
        3: Skype
        4: Telegram
        5: Github
    
    2. Виды образования - education_type:
        1: Начальное
        2: Повышение квалификации
        3: Сертификаты
        4: Основное
    
    3. Уровень образования - education_level:
        1: Среднее
        2: Среднее специальное
        3: Неоконченное высшее
        4: Высшее
        5: Бакалавр
        6: Магистр
        7: Кандидат наук
        8: Доктор наук
    
    3. Уровень знания языка - language_level:
        1: Начальный
        2: Элементарный
        3: Средний
        4: Средне-продвинутый
        5: Продвинутый
        6: В совершенстве
        7: Родной"""

    example_text = read_cv("../examples/AHMAT SULEIMENOV.docx")
    example_json = open("../examples/ahmat_suleimonov.json").read()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": cv
                + "\n"
                + raw_promt
                + "\n"
                + f"Пример:\nрезюме: {example_text}\njson-file: {example_json}",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content
