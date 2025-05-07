from faker import Faker
from datetime import datetime

def get_personal_data():
    fake = Faker('ru_RU')
    return (
        fake.first_name(),
        fake.last_name(),
        fake.city(),
        fake.numerify('+7##########')
    )

def get_comment():
    fake = Faker('ru_RU')
    return fake.sentence(nb_words=5)
