from faker import Faker
import random
from data.data import *
faker_ru = Faker('ru_RU')
Faker.seed()

def get_person():
    yield Person(
        full_name = faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address(),
        first_name = faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(1, 100),
        department=faker_ru.job(),
        salary=random.randint(100, 1000000),
        mobile=faker_ru.msisdn() #дает разные числа
    )

def generated_file():
    path = rf"/Users/sergeyl/Documents/autotest_python{random.randint(0, 999)}.txt"
    with open(path, 'w+') as f:
        f.write(f"""Hello World{random.randint(0, 999)}""")
        f.close()
    return f.name, path

def generated_subject():
    subject = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
                "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    random.shuffle(subject)
    new_list = []
    for i in range(random.randint(1, 4)):
        new_list.append(subject[i])
    return new_list

def generated_city():
    random_list = random.choice(["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"])
    city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer", ]
    }
    return random_list, city[random_list]

def generator_color():
    yield Color(
        color_name=["Red", "Blue", "Yellow", "Purple", "White", "Violet",
                        "Indigo", "Black", "Magenta", "Aqua", "Green"]
    )

