from faker import Faker
import random
from python_autotests.data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()

def get_person():
    yield Person(
        full_name = faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address()

    )



# from faker.providers import internet


# fake = Faker()
# faker_ru = Faker('ru_RU')
# fake.add_provider(internet)



# print(fake.name())
# print(fake.address())
# print(faker_ru.name())
# print(faker_ru.address())
# print(fake.text())
# print(faker_ru.text())
# print(fake.ipv4_private())