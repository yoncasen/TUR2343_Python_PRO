import random

# karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"1234567890"
# sifre_uzunlugu = int(input("Şifre Uzunluğunuzu Girin: "))

# sifre = ""
# for i in range(sifre_uzunlugu):
#     sifre += random.choice(karakterler)

# print(sifre)


def sifre_olustur(pass_length):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

# parola = gen_pass(10)
# print(parola)
