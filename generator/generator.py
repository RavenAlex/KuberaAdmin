import random

from data.data import Person, Color, Date, Value, Select, Product
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_sort_product():
    yield Product(
        product_name=["CHANNELS", "ТТММ", "EXSCUDO"]
    )

