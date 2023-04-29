import random

from data.data import Person, Color, Date, Value, Select, Product, Type, Kyc
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_sort_product():
    yield Product(
        product_name=["CHANNELS", "ТТММ", "EXSCUDO"]
    )


def generated_sort_type():
    yield Type(
        type_name=["INVOICE_PAYMENT", "DEPOSIT", "WITHDRAWAL", "TRANSFER", "REFUND", "REGISTRATION_OF_COLOR_COIN",
                   "REGISTRATION_OF_EON_ID", "CURRENCY_EXCHANGE", "VOTE", "COMPLEX"]
    )

def generated_kys_type():
    yield Kyc(
        kyc_name=["EMAIL", "FORM", "PERSONAL_PHONE", "HOME_ADDRESS", "IDENTIFICATION_DOCUMENT"]
    )


