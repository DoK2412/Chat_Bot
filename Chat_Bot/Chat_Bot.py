import random
import nltk
#чат бот 
BOT_CONFIG = {
    'itents' : {
        'hello' : {
            'examples' : ['Привет', 'Добрый вечер', 'Хай', 'Привет бот' ],
            'responses' : ['Привет, человек!', 'И вам здравствуйте.', 'Доброго времени суток'],
            },
        'bye' : {
            'examples' : ['Пока', 'Досведания', 'До сведания', 'До скорой встречи' ],
            'responses' : ['Еще увидимся!', 'Если что я всегда тут.'],
            },
        'name' : {
            'examples' : ['Как тебя завут?', 'Скажи свое имя', 'Представься',],
            'responses' : ['Меня зовут Женя'],
            },
        },

    'failure_phrases' : [
        'Непонятно. Перефразируйте пожалуйста.',
        'Я еще тольо учусь. Спросите что нибудь другое.',
        'Слишкм сложный вопрос для меня.',
        ]
    }

def claer_phrase(phrase):
    phrase = phrase.lower()

    alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю- '
    result = ''
    for symbol in alphabet:
        if symbol in alphabet:
            result += symbol
    return phrase

def classify_intent(replica):
    replica = claer_phrase(replica)

    for intent, intent_data in BOT_CONFIG['itents'].items():
        for example in intent_data['examples']:
            example = claer_phrase(example)
            distance = nltk.edit_distance(replica, example)

            if distance / len(example) < 0.4:
                return intent
    return 'hello'

def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['itents']:
        responses = BOT_CONFIG['itents'][intent]['responses']
        return random.choice(responses)

def generate_answer(replica):
    #пока что не используем
    return

def get_failure_phrase():
    failure_phrases = BOT_CONFIG ['failure_phrases']
    return random.choice(failure_phrases)

#ответ бота
def bot(replica):

    intent = classify_intent(replica)

    #генерация ответа
    #выбор ответа
    if intent is not None:
        answer = get_answer_by_intent(intent)
        if answer is not None:
            return answer

    #вызов генеративной модели
    answer = generate_answer(intent)
    if answer is not None:
        return answer

    #заглушка
    return get_failure_phrase()
  


    answer = replica
    return answer

answer = bot('добрый вечер')
print(answer)