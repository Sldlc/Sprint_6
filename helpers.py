import random


def generate_name():
    list_names = ['Павел', 'Никита', 'Дмитрий', 'Александр', 'Егор', 'Ольга', 'Яна', 'Наталья', 'Светлана', 'Екатерина']
    name = random.choice(list_names)
    return name


def generate_surname():
    list_surnames = ['Кох', 'Браун', 'Павлюченко', 'Ким', 'Свон', 'Ляйсан']
    surname = random.choice(list_surnames)
    return surname


def generate_adress():
    list_adresses = ['Чугунова', 'Карла Маркса', 'Ленина', 'Сталина', 'Фрунзе', 'Микояна', 'Гагарина']
    random_adress = random.choice(list_adresses)
    random_number = random.randint(10, 99)
    adress = f"{random_adress}, {random_number}"
    return adress


def generate_metro():
    list_metro = ['Сокольники', 'Выхино', 'Митино', 'Кантемировская', 'Новокосино', 'Китай город', 'Чертановская']
    metro = random.choice(list_metro)
    return metro


def generate_phone():
    random_digits = random.randint(100000000, 999999999)
    phone_number = f"89{random_digits}"
    return phone_number


def generate_date():
    random_date_day = random.randint(1, 29)
    random_date_month = random.randint(1, 12)
    date = f"{random_date_day}.{random_date_month}.2024"
    return date


def generate_comment():
    list_comments = ['Как дела?', 'Можно побыстрее, пожалуйста', 'Позвоните заранее', '  ']
    comment = random.choice(list_comments)
    return comment


name = generate_name()
surname = generate_surname()
adress = generate_adress()
metro = generate_metro()
phone_number = generate_phone()
date = generate_date()
comment = generate_comment()
